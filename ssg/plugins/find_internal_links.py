from html.parser import HTMLParser
from urllib.parse import urlparse
from typing import Set


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


def apply(site, page) -> None:
    '''Finds all local links and save them as 'links'.
    Local link is the link with empty scheme and empty netloc.
    Examples: "<a href="/internal_link/">", "<a href="internal_link/">.
    '''
    parser = InternalLinksExtractor()
    parser.feed(page['html'])
    page['links'] = parser.links
