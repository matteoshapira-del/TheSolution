#!/usr/bin/env python3
"""Render a research report (Markdown) to a designed PDF with headless Chromium.

    python3 tools/research/build_pdf.py "reports/<title>.md" "reports/<title>.pdf" \
        --spectrum tools/research/spectrum.json --subtitle "..."

Requires: pip install markdown; Playwright with Chromium (preinstalled in Claude Code cloud sessions).
Fonts (Archivo, Source Serif 4; SIL OFL) are downloaded once into tools/research/.fonts/ (git-ignored).
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
FONT_DIR = HERE / ".fonts"
FONT_CSS_URL = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800"
                "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def ensure_fonts() -> str:
    """Return @font-face CSS with fonts inlined as data URIs (downloads on first run)."""
    FONT_DIR.mkdir(exist_ok=True)
    local = FONT_DIR / "local.css"
    if not local.exists():
        css = subprocess.run(["curl", "-sS", "-A", UA, FONT_CSS_URL], capture_output=True, text=True, check=True).stdout
        out = []
        for i, (subset, block) in enumerate(re.findall(r"/\*\s*(\S+)\s*\*/\s*(@font-face\s*{[^}]+})", css)):
            if subset not in ("latin", "latin-ext"):
                continue
            url = re.search(r"url\((https://[^)]+)\)", block).group(1)
            fn = f"{subset}-{i}.woff2"
            subprocess.run(["curl", "-sS", "-o", str(FONT_DIR / fn), url], check=True)
            out.append(block.replace(url, fn))
        local.write_text("\n".join(out), encoding="utf-8")
    css = local.read_text(encoding="utf-8")

    def inline(m):
        data = base64.b64encode((FONT_DIR / m.group(1)).read_bytes()).decode()
        return f"url(data:font/woff2;base64,{data})"

    return re.sub(r"url\(([^)]+\.woff2)\)", inline, css)


CSS = r"""
:root {
  --ink: #1b2224; --muted: #5a666c; --rule: #cfd8d9; --soft: #f1f4f4; --accent: #24566e;
  --a: #7a2e2e; --b: #9a6a12; --c: #2c6e5a; --d: #24566e; --e: #5b3f86;
}
@page { size: A4; margin: 20mm 17mm 20mm 17mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
html { font-family: "Source Serif 4", "DejaVu Serif", Georgia, serif; font-size: 10.2pt; color: var(--ink); line-height: 1.5; }
body { margin: 0; }
h1, h2, h3, h4 { font-family: "Archivo", "DejaVu Sans", Arial, sans-serif; line-height: 1.15; text-wrap: balance; color: var(--ink); }
h1 { font-size: 22pt; font-weight: 800; font-stretch: 72%; margin: 0 0 6mm; }
h2 { font-size: 16pt; font-weight: 760; font-stretch: 78%; margin: 9mm 0 3mm; padding-top: 2.5mm; border-top: 1.4pt solid var(--ink); break-after: avoid; }
h3 { font-size: 11.6pt; font-weight: 700; font-stretch: 88%; margin: 6mm 0 2mm; break-after: avoid; color: var(--accent); }
h4 { font-size: 10.4pt; font-weight: 700; font-stretch: 92%; margin: 4mm 0 1.5mm; break-after: avoid; }
p { margin: 0 0 2.6mm; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 3mm; padding-left: 5.5mm; }
li { margin: 0 0 1.2mm; }
a { color: var(--accent); text-decoration: none; overflow-wrap: anywhere; }
strong { font-weight: 650; }
code { font-family: "JetBrains Mono", "DejaVu Sans Mono", monospace; font-size: 0.86em; }
blockquote { margin: 3mm 0; padding: 2mm 4mm; border-left: 2.5pt solid var(--accent); background: var(--soft); }
hr { border: 0; border-top: 0.6pt solid var(--rule); margin: 5mm 0; }
table { width: 100%; border-collapse: collapse; margin: 2mm 0 4.5mm; font-size: 8.4pt; line-height: 1.38; }
thead { display: table-header-group; }
th { font-family: "Archivo", "DejaVu Sans", sans-serif; font-weight: 700; font-stretch: 90%; text-align: left; border-bottom: 1pt solid var(--ink); padding: 1.6mm 1.8mm; vertical-align: bottom; }
td { border-bottom: 0.5pt solid var(--rule); padding: 1.5mm 1.8mm; vertical-align: top; overflow-wrap: break-word; hyphens: auto; }
td a, li a { overflow-wrap: anywhere; }
tr { break-inside: avoid; }
table.wide { font-size: 7.5pt; line-height: 1.33; }
table.wide th, table.wide td { padding: 1.2mm 1.4mm; }
tbody tr:nth-child(even) td { background: var(--soft); }
sup, .footnote-ref { font-size: 0.72em; }
.footnote { font-size: 8.2pt; color: var(--muted); }
.footnote ol { padding-left: 5mm; }
.footnote li { margin-bottom: 0.8mm; overflow-wrap: anywhere; }

/* cover */
.cover { height: 297mm; padding: 26mm 22mm 20mm; display: flex; flex-direction: column; justify-content: space-between; break-after: page;
  background: #f1f4f4; position: relative; overflow: hidden; }
.cover .kicker { font-family: "Archivo", sans-serif; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; font-size: 9pt; color: var(--muted); }
.cover h1 { font-size: 40pt; font-stretch: 66%; text-transform: uppercase; line-height: 0.95; margin: 6mm 0 6mm; max-width: 160mm; }
.cover .sub { font-size: 13pt; max-width: 135mm; line-height: 1.45; }
.cover .band { display: flex; height: 7mm; margin: 12mm 0 4mm; border-radius: 1mm; overflow: hidden; }
.cover .band i { flex: 1; }
.cover .bandlab { display: flex; justify-content: space-between; font-family: "Archivo", sans-serif; font-size: 8.5pt; color: var(--muted); font-stretch: 90%; }
.cover .meta { font-family: "Archivo", sans-serif; font-size: 9pt; color: var(--muted); display: grid; gap: 1.5mm; }
.cover .meta b { color: var(--ink); }

/* spectrum figure */
.figure { break-inside: avoid; margin: 0 0 6mm; }
.figure .cap { font-family: "Archivo", sans-serif; font-size: 8.6pt; color: var(--muted); margin-top: 2mm; }
.spec { display: grid; grid-template-columns: 9mm 1fr; gap: 0 3mm; }
.spec .axis { position: relative; }
.spec .axis::before { content: ""; position: absolute; left: 3.5mm; top: 1mm; bottom: 1mm; width: 2pt; background: linear-gradient(var(--a), var(--b), var(--c), var(--d), var(--e)); border-radius: 1pt; }
.spec .row { display: grid; grid-template-columns: 7mm 46mm 1fr; gap: 2.5mm; align-items: baseline; padding: 1.25mm 0; border-bottom: 0.5pt solid var(--rule); break-inside: avoid; }
.spec .n { font-family: "JetBrains Mono", monospace; font-size: 8pt; color: var(--muted); }
.spec .nm { font-family: "Archivo", sans-serif; font-weight: 700; font-stretch: 88%; font-size: 9.6pt; }
.spec .ds { font-size: 8.6pt; line-height: 1.38; }
.spec .grp { font-family: "Archivo", sans-serif; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; font-size: 7.6pt; padding: 2.4mm 0 0.6mm; border-bottom: 0.8pt solid var(--ink); }
.spec .grp span { display: inline-block; width: 2.4mm; height: 2.4mm; border-radius: 50%; margin-right: 2mm; vertical-align: 0; }

/* toc */
.toc { break-after: page; }
.toc ul { list-style: none; padding: 0; margin: 0; }
.toc > ul > li { margin: 0; padding: 1.6mm 0; border-bottom: 0.5pt solid var(--rule); font-family: "Archivo", sans-serif; font-weight: 650; font-stretch: 92%; font-size: 10.2pt; }
.toc > ul > li > ul { margin-top: 1mm; padding-left: 5mm; }
.toc > ul > li > ul > li { font-weight: 400; font-size: 9pt; color: var(--muted); padding: 0.4mm 0; border: 0; }
.toc a { color: inherit; }
.note { font-size: 8.6pt; color: var(--muted); border-top: 0.6pt solid var(--rule); padding-top: 2mm; margin-top: 4mm; }
"""

GROUP_COLORS = {"a": "var(--a)", "b": "var(--b)", "c": "var(--c)", "d": "var(--d)", "e": "var(--e)"}


def spectrum_html(spec: dict) -> str:
    rows, n = [], 0
    for g in spec["groups"]:
        rows.append(f'<div class="grp"><span style="background:{GROUP_COLORS[g["band"]]}"></span>{html.escape(g["name"])}</div>')
        for m in g["models"]:
            n += 1
            rows.append(f'<div class="row"><div class="n">{n:02d}</div><div class="nm">{html.escape(m["name"])}</div>'
                        f'<div class="ds">{html.escape(m["gist"])}</div></div>')
    return (f'<div class="figure"><h2 style="border-top:0;margin-top:0">{html.escape(spec["title"])}</h2>'
            f'<p>{html.escape(spec["intro"])}</p>'
            f'<div class="spec"><div class="axis"></div><div>{"".join(rows)}</div></div>'
            f'<div class="cap">{html.escape(spec["caption"])}</div></div>')


def build(md_path: Path, pdf_path: Path, spectrum: Path | None, subtitle: str, kicker: str, title: str | None = None) -> None:
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"\s*#\s+(.+)\n", text)
    if title:
        # Keep the report's own H1 (its thesis) as the opening heading of the body.
        if m:
            text = "## " + m.group(1).strip() + "\n" + text[m.end():]
    else:
        title = m.group(1).strip() if m else md_path.stem
        if m:
            text = text[m.end():]
    md = markdown.Markdown(extensions=["tables", "toc", "footnotes", "sane_lists", "attr_list", "fenced_code"],
                           extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}})
    body = md.convert(text)
    # Dense tables (5+ columns) get a smaller font so they fit A4 portrait.
    body = re.sub(r"<table>(\s*<thead>\s*<tr>(?:\s*<th[^>]*>.*?</th>){5,})", r'<table class="wide">\1', body, flags=re.S)
    toc = md.toc
    spec_html = spectrum_html(json.loads(spectrum.read_text(encoding="utf-8"))) if spectrum else ""
    today = dt.date.today().strftime("%d %B %Y")
    head = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{ensure_fonts()}{CSS}</style></head><body>"""
    cover = f"""<section class="cover">
  <div>
    <div class="kicker">{html.escape(kicker)}</div>
    <h1>{html.escape(title)}</h1>
    <div class="sub">{html.escape(subtitle)}</div>
    <div class="band"><i style="background:var(--a)"></i><i style="background:var(--b)"></i><i style="background:var(--c)"></i><i style="background:var(--d)"></i><i style="background:var(--e)"></i></div>
    <div class="bandlab"><span>Israeli sovereignty over all the land</span><span>Partition and shared arrangements</span><span>A single state for all, or a Palestinian state over all the land</span></div>
  </div>
  <div class="meta"><div><b>Prepared for</b> The Solution · game design research</div><div><b>Date</b> {today}</div>
  <div><b>Scope</b> Proposals documented in scholarly, legal, policy and press sources, presented descriptively. Inclusion is not endorsement.</div></div>
</section>"""
    rest = f"""<section class="toc"><h2 style="border-top:0">Contents</h2>{toc}</section>
{spec_html}
{body}"""
    page = head + cover + rest + "</body></html>"
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "report.html"
        src.write_text(head + rest + "</body></html>", encoding="utf-8")
        csrc = Path(td) / "cover.html"
        csrc.write_text(head + cover + "</body></html>", encoding="utf-8")
        cpdf, bpdf = Path(td) / "cover.pdf", Path(td) / "body.pdf"
        footer = ('<div style="font-family:Arial,sans-serif;font-size:7pt;color:#5a666c;width:100%;padding:0 17mm;'
                  'display:flex;justify-content:space-between"><span>' + html.escape(title) +
                  '</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
        js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{csrc}', {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {json.dumps(str(cpdf))}, format: 'A4', printBackground: true, preferCSSPageSize: true, pageRanges: '1' }});
  await p.goto('file://{src}', {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {json.dumps(str(bpdf))}, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: {json.dumps(footer)} }});
  await b.close();
}})();"""
        (Path(td) / "r.js").write_text(js, encoding="utf-8")
        subprocess.run(["node", str(Path(td) / "r.js")], check=True)
        from pypdf import PdfReader, PdfWriter
        w = PdfWriter()
        for f in (cpdf, bpdf):
            for pg in PdfReader(str(f)).pages:
                w.add_page(pg)
        w.add_metadata({"/Title": title, "/Subject": subtitle, "/Creator": "The Solution research pipeline"})
        with open(pdf_path, "wb") as fh:
            w.write(fh)
        if "--keep-html" in sys.argv:
            (pdf_path.with_suffix(".html")).write_text(page, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("pdf")
    ap.add_argument("--spectrum")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--kicker", default="Research report")
    ap.add_argument("--keep-html", action="store_true")
    ap.add_argument("--title")
    a = ap.parse_args()
    build(Path(a.md), Path(a.pdf), Path(a.spectrum) if a.spectrum else None, a.subtitle, a.kicker, a.title)
    print("Wrote", a.pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main())
