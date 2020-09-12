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
    for y in range(0, height, chunk[1]):
        counter = 0
        c_counter = 0
        for x in range(0, width, chunk[0]):
            section = img[y:y + chunk[1], x:x + chunk[0], :]
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

    print(instruction_set)
    save(instruction_set)


def derive_color_bw(color: np.ndarray):
    return int(127 > color.mean())


def save(instructions):
    with open('arduino/main/img.h', 'w') as file:
        file.write('#define len ' + str(len(instructions)) + '\n')
        for key, name in enumerate(('axises', 'colors', 'distances')):
            file.write('int ' + name + '[] = { ')
            for instruction in instructions:
                file.write(str(instruction[key]) + ', ')
            file.write('};\n')