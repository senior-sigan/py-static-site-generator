import frontmatter


def apply(site, page):
    text = page['path'].read_text()
    metadata, content = frontmatter.parse(text)
    page['metadata'] = metadata
    page['content'] = content
