import markdown
from markdown.extensions.wikilinks import WikiLinkExtension


def apply(site, page) -> None:
    page['html'] = markdown.markdown(
        page['content'],
        extensions=[
            'markdown.extensions.tables',
            WikiLinkExtension(base_url='/', end_url=''),
            'pymdownx.arithmatex',
            'pymdownx.highlight',
            'pymdownx.magiclink',
            'pymdownx.superfences',
        ],
    )
