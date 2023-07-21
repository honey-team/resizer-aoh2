import cv2
import os
from typing import Literal
import math
import pathlib

# config

# all
FLAGS_H = (68, 44)
FLAGS = (27, 18)

# only width
ICONS = 18
H = 18
XH = 24
XXH = 30
XXXH = 30
XXXXH = 42

def __flags_mode():
    return [FLAGS_H, FLAGS]

def __crowns_mode():
    return [XXXXH, XXXH, XH, H]

def __adaptive_height(width: int, src):
    now_width = src.shape[1]
    now_height = src.shape[0]

    K = now_width / width
    height = now_height / K

    return (width, math.floor(height))

def resizePhotos(mode: Literal['f', 'c']): # f - flags, c - crowns
    photos = os.listdir('Storage')

    for i in photos:
        src = cv2.imread(f'Storage/{i}', cv2.IMREAD_UNCHANGED)

        if mode == 'f':
            sizes = __flags_mode()

            for dsize in sizes: # width and height
                output = cv2.resize(src, dsize)

                folder = 'flagsH' if dsize == FLAGS_H else 'flags'

                cv2.imwrite(f'Output/flags/{folder}/{i}', output)
        else:
            for width in __crowns_mode(): # width
                dsize = __adaptive_height(width, src)

                output = cv2.resize(src, dsize)

                width_dict = {
                    H: 'H',
                    XH: 'XH',
                    XXXH: 'XXXH',
                    XXXXH: 'XXXXH'
                }
                folder = width_dict[width]

                if width in [XXXH, XXH]:
                    for folder in ['XXXH', 'XXH']:
                        cv2.imwrite(f'Output/crowns/{folder}/{i}', output)
                elif width in [ICONS, H]:
                    for folder in ['ICONS', 'H']:
                        cv2.imwrite(f'Output/crowns/{folder}/{i}', output)
                else:
                    cv2.imwrite(f'Output/crowns/{folder}/{i}', output)

    cwd = os.getcwd()
    path = pathlib.Path(cwd, 'Output')

    if mode == 'f':
        path = path.joinpath('flags')
    elif mode == 'c':
        path = path.joinpath('crowns')
    return path
