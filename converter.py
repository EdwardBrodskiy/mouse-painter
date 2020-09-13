import numpy as np


def convert(img: np.ndarray, size=None):
    height, width, *_ = img.shape
    if type(size) is int:
        size = (size, size * height // width)
    elif not size:
        size = (width, height)
    else:
        assert type(size) == tuple

    instruction_set = []

    img = scale_down_to(img, size)

    prev_color = 0
    for y in range(size[1]):
        counter = 0
        color = 0
        for x in range(size[0]):
            color = derive_color_bw(img[y, x, :])
            if prev_color != color:
                instruction_set.append([prev_color, counter])
                counter = 0
            counter += 1
            prev_color = color
        instruction_set.append([color, counter])

    print(instruction_set)
    save(instruction_set, size[0])
    return img


def derive_color_bw(color: np.ndarray):
    return int(127 > color.mean())


def scale_down_to(img, size):
    height, width, *_ = img.shape
    chunk = (width // size[0], height // size[1])

    new_img = np.ndarray(list(reversed([3, *size])))

    for y in range(size[1]):
        for x in range(size[0]):
            sector_x = x * chunk[0]
            sector_y = y * chunk[1]
            for color in range(3):  # rgb
                new_img[y, x, color] = img[sector_y: sector_y + chunk[1], sector_x: sector_x + chunk[0], color].mean()

    return new_img


def save(instructions, width):
    with open('arduino/main/img.h', 'w') as file:
        file.write(f'#define len {len(instructions)} \n')
        file.write(f'#define width {width} \n')

        file.write('byte colors[] = { ')
        for instruction in instructions:
            file.write(str(instruction[0]) + ', ')
        file.write('};\n')

        file.write('byte distances[] = { ')
        for instruction in instructions:
            file.write(str(instruction[1]) + ', ')
        file.write('};\n')
