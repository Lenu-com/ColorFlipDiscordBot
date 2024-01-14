from typing import Final
import cv2
from now import fetch_now

INPUT_PATH: Final[str] = 'images/input/'
OUTPUT_PATH: Final[str] = 'images/output/'

class ColorFlip:
    def __init__(self, img_path: str) -> None:
        if img_path is None:
            raise ValueError('img_path is None')
        self.__img = cv2.imread(INPUT_PATH + img_path)
        if self.__img is None:
            raise ValueError('img_path is invalid')
        
        
    def flip(self) -> None:
        self.__img = cv2.bitwise_not(self.__img)
        
        
    def write(self) -> None:
        cv2.imwrite(f"{OUTPUT_PATH}{fetch_now()}.jpg", self.__img)
        
