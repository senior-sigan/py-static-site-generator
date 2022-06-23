import shutil


def apply(site) -> None:
    for target in site['copy']:
        shutil.copytree(
            target['src'],
            target['dst'],
            dirs_exist_ok=True,
        )
