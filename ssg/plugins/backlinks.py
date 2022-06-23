import logging
from typing import Any, Dict, Set

logger = logging.getLogger()


def apply(site) -> None:
    backlinks: Dict[str, Set[str]] = {}
    pages_dict: Dict[str, Dict[str, Any]] = {}
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

            if pages_dict.get(link) is None:
                logger.warning(
                    f"Page {page['path']} has link to non-existing document {link}")
            else:
                page.setdefault('linked_pages', []).append(pages_dict[link])

    for page in site['pages']:
        links = backlinks.get(page['url'], set())
        page['backlinks'] = [pages_dict[link] for link in links]
