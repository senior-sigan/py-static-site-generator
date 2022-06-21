import argparse

import toml

from ssg.main_pipeline import compile_all
from ssg.models import Site, default_site


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Static site generator',
    )
    parser.add_argument(
        '--config',
        default='config.toml',
        help='Path to the toml config',
    )

    return parser.parse_args()


def site_from_config(config_path: str) -> Site:
    config = toml.load(config_path)
    site = default_site()
    site.update(config)
    return site


def main() -> None:
    args = parse_args()
    site = site_from_config(args.config)
    compile_all(site)


if __name__ == '__main__':
    main()
