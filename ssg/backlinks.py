import logging
from html.parser import HTMLParser
from typing import Dict, Set
from urllib.parse import urlparse

from ssg.models import Page, Site

logger = logging.getLogger()


class InternalLinksExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: Set[str] = set()

    def handle_starttag(self, tag, attrs) -> None:
        if tag == 'a':
            for k, v in attrs:
                if k == 'href':
                    url = urlparse(v)
                    if not url.scheme and not url.netloc:
                        self.links.add(v)


def inject_internal_links(page: Page) -> None:
    '''Finds all local links and save them as 'links'.
    Local link is the link with empty scheme and empty netloc.
    Examples: "<a href="/internal_link/">", "<a href="internal_link/">.
    '''
    parser = InternalLinksExtractor()
    parser.feed(page['html'])
    page['links'] = parser.links


def inject_backlinks(site: Site) -> None:
    backlinks: Dict[str, Set[str]] = {}
    pages_dict: Dict[str, Page] = {}
    for page in site['pages']:
        backlinks[page['url']] = set()
        pages_dict[page['url']] = page

    for page in site['pages']:
        for link in page['links']:
            if backlinks.get(link) is None:
                logger.warning(
                    f"Bad link {link} at {page['path']}")
            else:
                backlinks[link].add(page['url'])

    for page in site['pages']:
        links = backlinks.get(page['url'], set())
        page['backlinks'] = [pages_dict[link] for link in links]
