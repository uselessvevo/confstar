from __future__ import annotations

import sys
import inspect
from typing import Any, Type, Union


Numeric = Union[int, float, complex]
NUMERIC_TYPES = (int, float, complex)


class AnnotatedHandler:

    def __init__(self) -> None:
        self._attributes: dict[str, Any] = {}

    def set(self, field: str, value: Any) -> Any:
        raise NotImplementedError("Method \"set\" must be implemented")

    def get(self, field: str) -> Any:
        raise NotImplementedError("Method \"get\" must be implemented")


class LockHandler(AnnotatedHandler):

    def set(self, field: str, value: Any) -> Any:
        if field in self._attributes:
            raise KeyError(f"{field} is locked - you can't change its value")

        self._attributes[field] = value

    def get(self, field: str) -> Any:
        return self._attributes.get(field)


class MaxHandler(AnnotatedHandler):

    def set(self, field: str, value: Any) -> Any:
        if len(value) > self.__max:
            raise ValueError(f"Field {field} bigger than max value ({self.__max})")

        self._attributes[field] = value

    def get(self, field: str) -> Any:
        return self._attributes.get(field)

    def __class_getitem__(cls, max_value: Numeric) -> Type[MaxHandler]:
        if not isinstance(max_value, NUMERIC_TYPES):
            raise TypeError("Max value must be integer")

        cls.__max = max_value
        return cls


class MinHandler(AnnotatedHandler):

    def set(self, field: str, value: Any) -> Any:
        if len(value) < self.__min:
            raise ValueError(f"Field {field} is smaller than min value ({self.__min})")

        self._attributes[field] = value

    def get(self, field: str) -> Any:
        return self._attributes.get(field)

    def __class_getitem__(cls, min_value: Numeric) -> Type[MinHandler]:
        if not isinstance(min_value, NUMERIC_TYPES):
            raise TypeError("Min value must be integer")

        cls.__min = min_value
        return cls


class RangeHandler(AnnotatedHandler):
    """
    Check if value in range of A and B numerics
    """

    def set(self, field: str, value: Any) -> Any:
        if value < self.__num_range[0] or value > self.__num_range[1]:
            raise ValueError(f"Number \"{value}\" not in range of {self.__num_range[0]} and {self.__num_range[1]}")

        self._attributes[field] = value

    def get(self, field: str) -> Any:
        return self._attributes.get(field)

    def __class_getitem__(cls, num_range: list[Numeric, Numeric]) -> Type[RangeHandler]:
        if len(num_range) != 2:
            raise ValueError(f"Range must be a range of {NUMERIC_TYPES}")
        if not (isinstance(num_range[0], NUMERIC_TYPES), isinstance(num_range[1], NUMERIC_TYPES)):
            raise TypeError("Min value must be integer")

        cls.__num_range = num_range
        return cls


# Define these aliases to ignore linter errors
Max = type("Max", (MaxHandler,), {})
Min = type("Min", (MinHandler,), {})
Lock = type("Lock", (LockHandler,), {})
Range = type("Range", (RangeHandler,), {})

__all__ = list(i[0] for i in inspect.getmembers(sys.modules[__name__], inspect.isclass) if not i[0].endswith("Handler"))
