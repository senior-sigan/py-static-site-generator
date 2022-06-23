from pathlib import Path

from tqdm import tqdm

from ssg.assets_pipeline import copy_assets
from ssg.backlinks import inject_backlinks
from ssg.graph import compile_graph
from ssg.html_pipeline import HtmlRenderer
from ssg.markdown_pipeline import compile_markdown
from ssg.models import Site, Page
from ssg.scripts_pipeline import copy_scripts
from ssg.styles_pipeline import compile_sass


def compile_content(site: Site):
    src = Path(site['markdown']['src'])
    site['pages'] = [
        Page(idx=idx, path=entry)
        for idx, entry in enumerate(sorted(src.rglob('*.md')))
    ]
    for page in tqdm(site['pages']):
        compile_markdown(page, site)

    inject_backlinks(site)

    html_renderer = HtmlRenderer(site)
    for page in tqdm(site['pages']):
        html_renderer.render(page)


def compile_all(site: Site):
    compile_content(site)
    compile_graph(site)
    compile_sass(site)
    copy_assets(site)
    copy_scripts(site)
