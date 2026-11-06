#!/usr/bin/env bash
# Download the free official PeaceMaker desktop build (as linked from
# peacemakergame.com) and unpack it into harvest_raw/ (git-ignored).
#
# Requirements: curl, bsdtar (libarchive-tools) — bsdtar reads both the outer
# xar .pkg and the inner gzip/cpio Payload.
#
# Usage: tools/harvest/fetch.sh [OUT_DIR]   (default: ./harvest_raw)
set -euo pipefail

OUT="${1:-harvest_raw}"
MAC_PKG_URL="https://www.dropbox.com/s/cueotk99lj6yf6b/PeaceMaker_Israeli_Palestinian_Conflict_Download.pkg?dl=1"

mkdir -p "$OUT/installer" "$OUT/pkg" "$OUT/app"

if [ ! -s "$OUT/installer/peacemaker.pkg" ]; then
  echo "Downloading macOS build (~200 MB)…"
  curl -fL --retry 4 -o "$OUT/installer/peacemaker.pkg" "$MAC_PKG_URL"
fi
sha256sum "$OUT/installer/peacemaker.pkg" | tee "$OUT/installer/SHA256SUMS"

echo "Unpacking xar package…"
bsdtar -xf "$OUT/installer/peacemaker.pkg" -C "$OUT/pkg"
echo "Unpacking payload…"
bsdtar -xf "$OUT/pkg/com.impactgames.peacemaker.osx.pkg/Payload" -C "$OUT/app"

DATA="$OUT/app/PeaceMaker.app/Contents/Resources/Data"
test -f "$DATA/StreamingAssets/peacemaker.db" || { echo "Unexpected layout: $DATA" >&2; exit 1; }
echo "Done. Unity data folder: $DATA"
echo "Next: python3 tools/harvest/extract.py --raw $OUT"
