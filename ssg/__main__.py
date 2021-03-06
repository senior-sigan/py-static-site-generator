import argparse

import toml

from ssg.models import default_site
from ssg.pipeline import run


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


def site_from_config(config_path: str):
    config = toml.load(config_path)
    site = default_site()
    site.update(config)
    return site


def main() -> None:
    args = parse_args()
    site = site_from_config(args.config)
    run(site)


if __name__ == '__main__':
    main()
