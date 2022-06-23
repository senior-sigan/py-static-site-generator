def apply(site, page) -> None:
    page['title'] = page.get('metadata', {}).get('title')
