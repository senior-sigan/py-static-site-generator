def apply(site, page) -> None:
    tags = page['metadata'].get('tags', [])
    page['metadata']['tags'] = set(tags)
