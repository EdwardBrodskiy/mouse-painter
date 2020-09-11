import numpy as np


def convert(img: np.ndarray, size=None):
    height, width, *_ = img.shape
    if type(size) is int:
        size = (size, size * height // width)
    elif not size:
        size = (width, height)
    else:
        assert type(size) == tuple
    chunk = (width // size[0], height // size[1])
    instruction_set = []

    counter = 0
    prev_color = 0
    for c in range(0, height - chunk[1], chunk[1]):
        for r in range(0, width - chunk[0], chunk[0]):
            color = derive_color_bw(img[r:r + chunk[1], c:c + chunk[0], :])
            if prev_color != color:
                instruction_set.append([0, prev_color, counter])
                counter = 0
            counter += 1
            prev_color = color
        instruction_set.append([0, prev_color, counter])
        counter = 0
        instruction_set.append([0, 0, -size[0]])
        instruction_set.append([1, 0, 1])

    display(instruction_set)


def derive_color_bw(color: np.ndarray):
    return int(127 > color.mean())


def display(instructions):
    print('{')
    for instruction in instructions:
        print('{ ' + str(instruction[0]) + ', ' + str(instruction[1]) + ', ' + str(instruction[2]) + ' },')
    print('}')
