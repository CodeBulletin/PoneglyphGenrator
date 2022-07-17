import numpy
import numpy as np
import pygame
import HamiltonianCycle
import random
import sys
import os
import math
from PIL import Image

chars = [chr(i) for i in range(32, 127)]


def generate_poneglyph(x, y, size_x, size_y, pad_x, pad_y):
    directory = "Poneglyph"
    seed = 6900415180638485488
    path = os.path.join(os.getcwd(), directory)
    if not os.path.exists(path):
        os.mkdir(path)
        print("Saving Poneglyph char at: " + path)
        print(f"seed: {seed}")
        random.seed(seed)

        char_to_cycle_dict = dict()
        char_to_points = dict()

        for i in chars:
            x0 = 0
            y0 = 0
            char_to_cycle_dict[i] = HamiltonianCycle.generate_hamiltonian_cycle(x, y, x0, y0)
            y0 += 1
            if y0 == y:
                y0 = 0
                x0 += 1
                if x0 == x:
                    x0 = 0

        for i in chars:
            points = []
            for pos, _ in char_to_cycle_dict[i].items():
                x1 = pad_x + (pos[0]) * (size_x - pad_x * 2) / x + (size_x - pad_x * 2) / (2 * x)
                y1 = pad_y + (pos[1]) * (size_y - pad_y * 2) / y + (size_y - pad_y * 2) / (2 * y)
                points.append((x1, y1))

            char_to_points[i] = points

        pygame.init()

        size = width, height = size_x, size_y
        screen = pygame.display.set_mode(size)
        i = 32
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            screen.fill((0, 0, 0, 255))
            pygame.draw.polygon(screen, (255, 255, 255, 255), char_to_points[chr(i)])

            pygame.image.save(screen, f"{path}\\{directory}_{i}.png")
            pygame.display.flip()
            i += 1
            if i == 127:
                break

    if not os.path.isfile(os.getcwd() + "\\" + f"{directory}.png"):
        pygame.init()

        size = width, height = size_x * 5 + 500, size_y * 19
        screen = pygame.display.set_mode(size)

        i = 0
        j = 0

        font = pygame.font.Font('freesansbold.ttf', 64)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            screen.fill((0, 0, 0, 255))
            while 1:
                img = pygame.image.load(f"{path}\\{directory}_{32 + j * 5 + i}.png")
                text = font.render(chr(32 + j * 5 + i), True, (255, 255, 255, 255), (0, 0, 0, 255))
                text_rect = text.get_rect()
                text_rect.center = (100 * i + 70 + i * 280, j * 200 + 100)
                screen.blit(text, text_rect)
                screen.blit(img, (100 * (i + 1) + i * 280, j * 200))
                i += 1
                if i == 5:
                    i = 0
                    j += 1
                    if j == 19:
                        break
            pygame.image.save(screen, os.getcwd() + "\\" + f"{directory}.png")
            pygame.display.flip()
            break


def get_files(directory):
    files = []
    files_name = []
    for (directory_path, directory_names, file_names) in os.walk(os.getcwd() + "\\" + directory):
        files += [os.path.join(directory_path, file) for file in file_names]
        files_name += [file for file in file_names]
    return files, files_name


def divide_num(num):
    length = num
    a = int(math.sqrt(length))
    b = int(length / a)
    while a >= 1 and length % a != 0:
        a -= 1
        b = int(length / a)
    return a, b


def generate_poneglyph_file(file_directory, file_name, size_x, size_y):
    with open(file_directory, mode='r') as file:
        data = file.read()
        processed_data = list(''.join([c for c in data if c in chars]))
        num = len(processed_data)
        a, b = divide_num(num)
        while a == 1 or b == 1:
            num += 1
            a, b = divide_num(num)

        x = min(a, b)
        y = max(a, b)
        a = x
        b = y

        width, height = size_x * a, size_y * b
        col_images = []
        for i in range(0, b):
            row_images = []
            for j in range(0, a):
                directory = os.getcwd() + f"\\Poneglyph\\Poneglyph_{ord(processed_data[i * a + j])}.png"
                row_images += [Image.open(directory)]
            widths, heights = zip(*(i.size for i in row_images))
            total_width = sum(widths)
            max_height = max(heights)
            row = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            for im in row_images:
                row.paste(im, (x_offset, 0))
                x_offset += im.size[0]
            col_images += [row]

        widths, heights = zip(*(i.size for i in col_images))
        max_width = max(widths)
        total_height = sum(heights)
        img = Image.new('RGB', (max_width, total_height))
        y_offset = 0
        for im in col_images:
            img.paste(im, (0, y_offset))
            y_offset += im.size[1]

        file = file_name.split('.')[0]

        img.save(f"DataOut\\{file}.png")


generate_poneglyph(12, 8, 280, 200, 20, 20)

f, fs = get_files("Data")
for fx, fy in zip(f, fs):
    print(fx, fy)
    generate_poneglyph_file(fx, fy, 280, 200)
