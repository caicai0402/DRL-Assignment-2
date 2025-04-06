def rot90(coords, board_size=4):
    return [(y, board_size - 1 - x) for x, y in coords]

def rot180(coords, board_size=4):
    return [(board_size - 1 - x, board_size - 1 - y) for x, y in coords]

def rot270(coords, board_size=4):
    return [(board_size - 1 - y, x) for x, y in coords]

def reflect_horiz(coords, board_size=4):
    return [(x, board_size - 1 - y) for x, y in coords]

def reflect_vert(coords, board_size=4):
    return [(board_size - 1 - x, y) for x, y in coords]

def reflect_diag(coords, board_size=4):
    return [(y, x) for x, y in coords]

def reflect_anti_diag(coords, board_size=4):
    return [(board_size - 1 - y, board_size - 1 - x) for x, y in coords]

def ids2coords(ids):
    id2coord = [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 1), (3, 2), (3, 3),
    ]
    return tuple(id2coord[id] for id in ids)
