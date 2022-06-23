from datetime import datetime
from pathlib import Path

import frontmatter
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from ssg.backlinks import inject_internal_links
from ssg.models import Page, Site


def inject_title(page: Page) -> None:
    page['title'] = page['metadata'].get('title')


def inject_date(page: Page, site: Site) -> None:
    date = page['metadata'].get('date')
    if date is None:
        return None
    date_format = page['metadata'].get('date_format', site['date_format'])
    page['date'] = datetime.strptime(date, date_format)


def inject_date_iso8601(page: Page) -> None:
    # 2013-05-16T08:36:00+00:00
    date = page.get('date')
    if date is not None:
        page['date_iso8601'] = date.isoformat()


def new_page(
    src: Path,
    idx: int,
) -> Page:
    return Page(
        idx=idx,
        path=src,
    )


def inject_raw_markdown(page: Page) -> None:
    text = page['path'].read_text()
    metadata, content = frontmatter.parse(text)
    page['metadata'] = metadata
    page['content'] = content


def inject_html(page: Page) -> None:
    page['html'] = markdown.markdown(
        page['content'],
        extensions=[
            'markdown.extensions.tables',
            WikiLinkExtension(base_url='/', end_url=''),
            'pymdownx.arithmatex',
            'pymdownx.highlight',
            'pymdownx.magiclink',
            'pymdownx.superfences',
        ],
    )


def inject_layout(page: Page) -> None:
    layout = page['metadata'].get('layout', 'default')
    layout = layout + '.html'
    page['layout'] = layout


def inject_target_path(page: Page, site: Site) -> None:
    permlink = page['metadata'].get('permalink')
    if permlink is not None:
        page['url'] = permlink
    else:
        rel_path = page['path'].relative_to(site['markdown']['src'])
        page['url'] = '/' + str(rel_path.with_suffix(''))

    if page['url'] == '/':
        page['url'] = '/index'

    target_path = site['markdown']['dst'] + page['url']
    page['target_path'] = Path(target_path).with_suffix('.html')


def compile_markdown(page: Page, site: Site):
    inject_raw_markdown(page)
    inject_title(page)
    inject_date(page, site)
    inject_date_iso8601(page)
    inject_target_path(page, site)
    inject_html(page)
    inject_internal_links(page)
    inject_layout(page)
