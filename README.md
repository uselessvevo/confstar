# Confstar - Extended Constants

## Why?

Confstar is a settings loader (similar to django settings) with ✨magic-annotations✨. <br> Also, Confstar is a part of [piekit](https://github.com/uselessvevo/pie-audio) project. I just wanted to make a dedicated repository for this piece of software.

<br>

## How to use it?

It's really that simple:
* Import `ConstLoader` from `confstar`
* Define your own loader instance
* Import it wherever you want

<br>

## Example
```py
# consts.py
from confstar import Lock, Min, Max

PRIVATE_INT_FIELD: Lock = 123
PUBLIC_MIN_FIELD: Min[3] = [1, 2]
PUBLIC_MAX_FIELD: Max[3] = [1, 2, 3]

# loader.py
Const = ConstLoader()

# setup.py
Const.import_module("consts")

# app.py
from loader import Const

# Will throw an error
Const.PRIVATE_INT_FIELD = 321
Const.PUBLIC_MIN_FIELD = [1, 2, 3, 4]
Const.PUBLIC_MAX_FIELD.extend([4, 5, 6])
```

## More about magic annotations

Of course, we have built-in magic-annotations, but if you want to write your own, it's really that easy:

1. Define your own handler

```py
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

2. Define alias which is optional

```py
Magic = type("Magic", (MagicHandler,), {})
```


3. Apply your handler on some field

```py
from confstar import Magic


MAGIC_FIELD: Magic = ...
```
