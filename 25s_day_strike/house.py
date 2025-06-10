# draw house 
import math
import random


def main():
    x, y = 100, 100
    width, height = 200, 200

    draw_house(x, y, width, height)

def draw_house(x, y, width, height) -> None:
    """Функція, яка малює дім, ширини width і висоти height від опорної точки (x, y)
        яка знаходиться в середині нижній точці фундаменту 
        x  - координата x середини домика 
        y - координата y низу домика 
        width - повна ширина домика (фундамент або вильоти даху включені)
        height - повна висота (від низу фундамента) """
        
    print('Imagine how i draw a house')
    foundation_height = 0.05 * height
    walls_width = 0.9 * width 
    walls_height = 0.5 * height
    roof_height = height - walls_height - foundation_height

    draw_house_fundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height + walls_height, width, roof_height )

    pass

def draw_house_fundation(x, y, width, height):
    """Основание домика від опорної точки (x, y)
        x - координати середини фундамента
        y - координата низу фундаменту 
        width - повна ширина фундаменту 
        height - повна висота фундаменту """
    print('Imagine how i draw a foundation of house', x, y, width, height)
    pass
def draw_house_walls(x, y, width, height):
    print('Imagine how i draw a house walls', x, y, width, height)
    pass
def draw_house_roof(x, y, width, height):
    print('Imagine how i draw a house roof', x, y, width, height)
    pass


main()
