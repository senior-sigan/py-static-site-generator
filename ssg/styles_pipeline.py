from pathlib import Path

import sass

from ssg.models import Site


def compile_sass(site: Site):
    src = Path(site['sass']['src']) / 'app.scss'
    dst = Path(site['sass']['dst'])
    css = sass.compile(
        filename=str(src.absolute()),
        output_style=site['sass']['style'],
        include_paths=str(src.parent.absolute()),
    )

    dst.parent.mkdir(exist_ok=True)
    dst.write_text(css)
