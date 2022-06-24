def apply(site, page):
    permalink = page['metadata'].get('permalink')
    if permalink == '/':
        permalink = '/index'
    if permalink and not permalink.startswith('/'):
        permalink = '/' + permalink

    if permalink is not None:
        page['url'] = permalink
