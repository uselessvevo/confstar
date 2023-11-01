import types
import os.path
import importlib
import importlib.util


def import_by_path(path: str) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(os.path.basename(path).split(".")[0], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
