from pathlib import Path


def apply(site, page) -> None:
    if page.get('url') is None:
        rel_path = page['path'].relative_to(site['md']['src'])
        page['url'] = '/' + str(rel_path.with_suffix(''))

    target_path = site['md']['dst'] + page['url']
    page['target_path'] = Path(target_path).with_suffix('.html')
