import os
from typing import Final
from color_flip import ColorFlip


def main():
    cf = ColorFlip('20240114195024.jpg')
    cf.flip()
    cf.write()
    
if __name__ == '__main__':
    main()

