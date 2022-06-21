from pathlib import Path

from tqdm import tqdm

from ssg.assets_pipeline import copy_assets
from ssg.backlinks import inject_backlinks
from ssg.html_pipeline import HtmlRenderer
from ssg.markdown_pipeline import compile_markdown, new_page
from ssg.models import Site
from ssg.styles_pipeline import compile_sass


def compile_content(site: Site):
    src = Path(site['markdown']['src'])
    dst = Path(site['markdown']['dst'])
    site['pages'] = [
        new_page(entry, src, dst)
        for entry in sorted(src.rglob('*.md'))
    ]
    for page in tqdm(site['pages']):
        compile_markdown(page, site)

    inject_backlinks(site)

    html_renderer = HtmlRenderer(site)
    for page in tqdm(site['pages']):
        html_renderer.render(page)


def compile_all(site: Site):
    compile_content(site)
    compile_sass(site)
    copy_assets(site)
