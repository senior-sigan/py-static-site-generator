import shutil

from ssg.models import Site


def copy_scripts(site: Site):
    shutil.copytree(
        site['scripts']['src'],
        site['scripts']['dst'],
        dirs_exist_ok=True,
    )
