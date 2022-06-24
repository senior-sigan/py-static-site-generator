# class Sass(TypedDict, total=False):
#     src: str
#     style: str
#     dst: str


# class Graph(TypedDict, total=False):
#     dst: str
#     data: Dict[str, Any]


# class Copy(TypedDict, total=False):
#     src: str
#     dst: str


# class Markdown(TypedDict, total=False):
#     src: str
#     dst: str
#     layouts: str
#     plugins: List[str]


# class Site(TypedDict, total=False):
#     title: str
#     url: str
#     date_format: str

#     copy: List[Copy]
#     md: Markdown
#     sass: Sass
#     graph: Graph
#     plugins: List[str]

#     pages: List['Page']

# class Metadata(TypedDict, total=False):
#     date_format: str  # if None get vaue from the site.date_format
#     date: str
#     title: str
#     layout: str
#     permalink: str


# class Page(TypedDict, total=False):
#     idx: int
#     url: str  # link to the page
#     path: Path  # absolute path to the source file
#     target_path: Path  # absolute path where to save the rendered page
#     metadata: Metadata  # frontmatter data
#     content: str  # markdown text
#     html: str  # raw html
#     layout: str  # 'default.html'
#     date: Optional[datetime]
#     date_iso8601: Optional[str]  # 2006-01-02T15:04:05+07:00
#     title: Optional[str]
#     links: List[str]
#     backlinks: List['Page']
#     linked_pages: List['Page']


def default_site():
    return {
        'title': 'Site',
        'url': '/',
        'date_format':'%Y-%m-%d %H:%M:%S %z',
        'md': {
            'src': 'content',
            'dst': 'build',
            'layouts': 'theme/layouts',
            'plugins': [
                'ssg.plugins.frontmatter_parser',
                'ssg.plugins.inject_title',
                'ssg.plugins.inject_date',
                'ssg.plugins.inject_date_iso8601',
                'ssg.plugins.inject_layout',
                'ssg.plugins.permalink',
                'ssg.plugins.set_target_path',
                'ssg.plugins.markdown_to_html',
            ],
        },
        'plugins': [
            'ssg.plugins.parse_markdown',
            'ssg.plugins.render_html',
        ],
    }
