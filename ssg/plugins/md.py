from pathlib import Path
from tqdm import tqdm
from ssg.plugin_loader import load_plugins


def apply(site):
    config = site['md']
    plugins = load_plugins(config.get('plugins', []))
    src = Path(config['src'])
    site['pages'] = [
        {'idx': idx, 'path': entry}
        for idx, entry in enumerate(sorted(src.rglob('*.md')))
    ]
    for page in tqdm(site['pages']):
        for plugin in plugins:
            plugin.apply(site, page)
