from types import ModuleType
from typing import List
import importlib


def load_plugins(plugin_names: List[str]) -> List[ModuleType]:
    return [importlib.import_module(name) for name in plugin_names]
