# Confstar

## What is this library?

Confstar is a config loader (*similar to django settings loader*) with ✨**magic-annotations**✨ handlers. <br> Also, Confstar is a part of [pie-audio](https://github.com/uselessvevo/pie-audio) project. I just wanted to make an independent repository for it.

## What is ✨magic-annotation✨?
Basically, it's micro-handlers that let's you to control field behaviour  via [type annotations](https://peps.python.org/pep-0484/).

For example, you can specify how many elements list must have, lock the field to prevent it from editing and etc.

## How to use confstar?

It's really that simple:
* Import `Config` instance of `ConfLoader` (*or define your own*)
* Import it wherever you want


## Configuration module
```py
# configs/consts.py
from confstar.types import *

PRIVATE_INT_FIELD: Lock = 100
PUBLIC_MIN_FIELD: Min[3] = [1, 2]
PUBLIC_MAX_FIELD: Max[3] = [1, 2, 3]
PUBLIC_RANGE_FIELD: Range[1, 5] = 2
```

## Your application
```py
from confstar.loader import Config, ConfLoader


Config.add_handlers(Lock, Min, Max)
Config.import_module("configs.config")

# Or load configuration module by using relative file path
MyConfig = ConfLoader()
MyConfig.load_by_path("configs/myconfig.py")

# Will throw an error
Config.PRIVATE_INT_FIELD = 321
Config.PUBLIC_MIN_FIELD = [1, 2, 3, 4]
Config.PUBLIC_MAX_FIELD.extend([4, 5, 6])
Config.PUBLIC_RANGE_FIELD = 6
```

## Writing your own handler

Of course, we have built-in magic-annotations, but if you want to write your own, it's really that easy:

1. Define your own handler

```py
from __future__ import annotations

from typing import Any, Type

from confstar import AnnotatedHandler


class MagicHandler(AnnotatedHandler):

    def set(self, field: str, value: Any) -> Any:
        """
        Set or throw and error if validation fail
        """
        if not value % 2 == 0:
            raise ValueError(f"An error has been occurred in {self.__class__.__name__}")

        self._attributes[field] = value

    def get(self, field: str) -> Any:
        """
        Return field from `_attributes`
        """
        return self._attributes[field]  # or via `dict.get` method

    def __class_getitem__(cls, value: Any) -> Type[MagicHandler]:
        """
        Provide the type annotation logic
        
        Field: HandlerType[<values>]
        """
```

2. Define alias to ignore linter (*which is optional*)

```py
Magic = type("Magic", (MagicHandler,), {})
```


3. Apply your handler on some field

```py
from my_handlers import Magic


MAGIC_FIELD: Magic = ...
```
