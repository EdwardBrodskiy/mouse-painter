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
    for r in range(0, height - chunk[1], chunk[1]):
        counter = 0
        c_counter = 0
        for c in range(0, width - chunk[0], chunk[0]):
            section = img[r:r + chunk[1], c:c + chunk[0], :]
            color = derive_color_bw(section)
            if prev_color != color:
                instruction_set.append([0, prev_color, counter])
                c_counter += counter
                counter = 0
            counter += 1
            prev_color = color
        instruction_set.append([0, prev_color, counter])

        instruction_set.append([0, 0, -(c_counter + counter)])
        instruction_set.append([1, 0, 1])

    save(instruction_set)


def derive_color_bw(color: np.ndarray):
    return int(127 > color.mean())


def save(instructions):
    with open('arduino/main/img.h', 'w') as file:
        file.write('#define len ' + str(len(instructions)) + '\n')
        file.write('int path[len][3] = {\n')
        for instruction in instructions:
            file.write('{ ' + str(instruction[0]) + ', ' + str(instruction[1]) + ', ' + str(instruction[2]) + ' },\n')
        file.write('};\n')
