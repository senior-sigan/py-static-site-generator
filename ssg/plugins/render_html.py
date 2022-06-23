from jinja2 import Environment, FileSystemLoader, select_autoescape

from ssg.models import Page, Site
from tqdm import tqdm


class HtmlRenderer:
    def __init__(self, site: Site) -> None:
        self.jinja_env = Environment(
            loader=FileSystemLoader(site['md']['layouts']),
            autoescape=select_autoescape()
        )
        self.site = site

    def render(self, page: Page):
        template = self.jinja_env.get_template(page['layout'])
        full_html = template.render(
            site=self.site,
            page=page,
        )
        page['target_path'].parent.mkdir(exist_ok=True, parents=True)
        page['target_path'].write_text(full_html)


def apply(site):
    html_renderer = HtmlRenderer(site)
    for page in tqdm(site['pages']):
        html_renderer.render(page)
