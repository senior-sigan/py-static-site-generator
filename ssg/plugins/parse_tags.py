def apply(site, page) -> None:
    tags = page['metadata'].get('tags', [])
    page['metadata']['tags'] = set(tags)
    print(f"{page['url']} {page['metadata']['tags']}")
