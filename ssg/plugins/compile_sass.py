from pathlib import Path

import sass


def apply(site):
    for sass_cfg in site['sass']:
        src = Path(sass_cfg['src']) / 'app.scss'
        dst = Path(sass_cfg['dst'])
        css = sass.compile(
            filename=str(src.absolute()),
            output_style=sass_cfg['style'],
            include_paths=str(src.parent.absolute()),
        )

        dst.parent.mkdir(exist_ok=True)
        dst.write_text(css)
