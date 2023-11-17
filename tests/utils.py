"""
ConfStar test utils
"""


def setup_confstar_default():
    from confstar import Config, Lock, Min, Max

    # Load config module
    Config.add_handlers(Lock, Min, Max)
    Config.import_module("tests.config")

    return Config
