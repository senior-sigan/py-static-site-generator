import shutil

from ssg.models import Site


def copy_assets(site: Site):
    shutil.copytree(
        site['assets']['src'],
        site['assets']['dst'],
        dirs_exist_ok=True,
    )
