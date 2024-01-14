import os
import cv2
from filepath import INPUT_PATH, OUTPUT_PATH


class ColorFlip:
    def __init__(self, img_name: str) -> None:
        if not img_name:
            raise ValueError('img_name is invalid')
        self.__img_name = img_name
        self.__img = cv2.imread(os.path.join(INPUT_PATH, img_name))
        if self.__img is None:
            raise ValueError('Failed to read image')
        
        
    def flip(self) -> None:
        self.__img = cv2.bitwise_not(self.__img)
        
        
    def write(self) -> str:
        output_path = os.path.join(OUTPUT_PATH, self.__img_name)
        cv2.imwrite(output_path, self.__img)
        return output_path
    
    
    @staticmethod
    def fetch_output_img(input_path: str) -> str:
        cf = ColorFlip(input_path)
        cf.flip()
        return cf.write()