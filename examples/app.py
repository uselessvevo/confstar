from confstar.types import Lock, Min, Max, Range
from confstar.loader import Config, ConfLoader


Config.add_handlers(Lock, Min, Max, Range)
Config.import_module("config")

# Or load config module by using file path
MyConfig = ConfLoader()
MyConfig.load_by_path("config.py")

print(Config.PUBLIC_RANGE_FIELD)
print(Config.PRIVATE_INT_FIELD)
print(Config.PUBLIC_MIN_FIELD)
print(Config.PUBLIC_MAX_FIELD)

# Will throw an error
Config.PUBLIC_RANGE_FIELD = 6
Config.PRIVATE_INT_FIELD = 321
Config.PUBLIC_MIN_FIELD = [1]
Config.PUBLIC_MAX_FIELD.extend([4, 5, 6])
