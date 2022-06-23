from ssg.models import Site, Page
import frontmatter


def apply(site: Site, page: Page):
    text = page['path'].read_text()
    metadata, content = frontmatter.parse(text)
    page['metadata'] = metadata
    page['content'] = content
