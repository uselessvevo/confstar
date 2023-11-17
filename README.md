# ConfStar - Extended Config Loader

## Why?

ConfStar is a config loader (*similar to django settings loader*) with ✨magic-annotations✨. <br> Also, ConfStar is a part of [pie-audio](https://github.com/uselessvevo/pie-audio) project. I just wanted to make an independent repository for it.

## What is ✨magic-annotations✨?
Basically, it's just a field handler that helps you to control field behaviour. 
For example, you can specify how many elements list must have. Or you can even lock the field to prevent it from editing.

## How to use it?

It's really that simple:
* Import `Config` instance of `ConfLoader` (*or define your own*)
* Import it wherever you want


## Example
```py
# configs/consts.py
from confstar import Lock, Min, Max, Config, ConfLoader

PRIVATE_INT_FIELD: Lock = 123
PUBLIC_MIN_FIELD: Min[3] = [1, 2]
PUBLIC_MAX_FIELD: Max[3] = [1, 2, 3]

# app.py
Config.import_module("configs.config")

# Or load config module by using file path
MyConfig = ConfLoader()
MyConfig.load_by_path("configs/myconfig.py")

# Will throw an error
Config.PRIVATE_INT_FIELD = 321
Config.PUBLIC_MIN_FIELD = [1, 2, 3, 4]
Config.PUBLIC_MAX_FIELD.extend([4, 5, 6])
```

## More about magic annotations

Of course, we have built-in magic-annotations, but if you want to write your own, it's really that easy:

1. Define your own handler

```py
from typing import Any

from confstar import AnnotatedHandler


class MagicHandler(AnnotatedHandler):

    def __init__(self) -> None:
        self.__attributes: dict[str, Any] = {}

    def set(self, field: str, value: Any) -> Any:
        # Provide your own logic
        ...

    def get(self, field: str) -> Any:
        return self.__attributes.get(field)
```

2. Define alias (*which is optional*)

```py
Magic = type("Magic", (MagicHandler,), {})
```


3. Apply your handler on some field

```py
from confstar import Magic


MAGIC_FIELD: Magic = ...
```
