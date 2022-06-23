from ssg.plugin_loader import load_plugins


def run(site):
    plugins = load_plugins(site['plugins'])
    for plugin in plugins:
        plugin.apply(site=site)
