def apply(site, page):
    permalink = page['metadata'].get('permalink')
    if permalink == '/':
        permalink = '/index'

    if permalink is not None:
        page['url'] = permalink
