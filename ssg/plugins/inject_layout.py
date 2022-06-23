def apply(site, page) -> None:
    layout = page.get('metadata', {}).get('layout', 'default')
    layout = layout + '.html'
    page['layout'] = layout
