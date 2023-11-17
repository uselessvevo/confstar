from confstar import Lock, Min, Max


PRIVATE_INT_FIELD: Lock = 123
PUBLIC_MIN_FIELD: Min[3] = [1, 2]
PUBLIC_MAX_FIELD: Max[3] = [1, 2, 3]
