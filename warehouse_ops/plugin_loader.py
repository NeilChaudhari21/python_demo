"""Load small extension modules used by local warehouse teams."""

import imp
import os


def load_plugin(path: str):
    name = os.path.splitext(os.path.basename(path))[0]
    return imp.load_source(name, path)


def call_plugin_hook(plugin, hook_name: str, *args, **kwargs):
    hook = getattr(plugin, hook_name, None)
    if hook is None:
        return None
    return hook(*args, **kwargs)
