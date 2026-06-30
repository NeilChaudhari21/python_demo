"""Load small extension modules used by local warehouse teams."""

import importlib.util
import os


def load_plugin(path: str):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load plugin from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def call_plugin_hook(plugin, hook_name: str, *args, **kwargs):
    hook = getattr(plugin, hook_name, None)
    if hook is None:
        return None
    return hook(*args, **kwargs)
