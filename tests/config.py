from confstar import Lock, Min, Max, Range


PRIVATE_INT_FIELD: Lock = 123
PUBLIC_MIN_FIELD: Min[3] = [1, 2]
PUBLIC_MAX_FIELD: Max[3] = [1, 2, 3]
PUBLIC_RANGE_FIELD: Range[1, 5] = 4
