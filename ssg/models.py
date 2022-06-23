from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from typing_extensions import TypedDict


class Sass(TypedDict, total=False):
    src: str
    style: str
    dst: str


class Markdown(TypedDict, total=False):
    src: str
    dst: str


class Assets(TypedDict, total=False):
    src: str
    dst: str


class Scripts(TypedDict, total=False):
    src: str
    dst: str


class Layouts(TypedDict, total=False):
    src: str


class Graph(TypedDict, total=False):
    dst: str
    data: Dict[str, Any]


class Site(TypedDict, total=False):
    title: str
    url: str
    date_format: str

    markdown: Markdown
    sass: Sass
    layouts: Layouts
    assets: Assets
    scripts: Assets
    graph: Graph

    pages: List['Page']


def default_site() -> Site:
    return Site(
        title='Site',
        url='/',
        date_format='%Y-%m-%d %H:%M:%S %z',
        markdown=Markdown(
            src='content',
            dst='build',
        ),
        assets=Assets(
            src='content/assets',
            dst='build/assets',
        ),
        scripts=Scripts(
            src='theme/scripts',
            dst='build/scripts',
        ),
        layouts=Layouts(
            src='theme/layouts',
        ),
        sass=Sass(
            src='theme/styles',
            style='compressed',
            dst='build/app.css',
        ),
    )


class Metadata(TypedDict, total=False):
    date_format: str  # if None get vaue from the site.date_format
    date: str
    title: str
    layout: str
    permalink: str


class Page(TypedDict, total=False):
    idx: int
    url: str  # link to the page
    path: Path  # absolute path to the source file
    target_path: Path  # absolute path where to save the rendered page
    metadata: Metadata  # frontmatter data
    content: str  # markdown text
    html: str  # raw html
    layout: str  # 'default.html'
    date: Optional[datetime]
    date_iso8601: Optional[str]  # 2006-01-02T15:04:05+07:00
    title: Optional[str]
    links: List[str]
    backlinks: List['Page']
    linked_pages: List['Page']
