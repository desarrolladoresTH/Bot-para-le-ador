from numpy import *
from PIL import ImageGrab, ImageOps
import pyautogui as py
import time

def izquierda():
    py.press('left')
    py.press('left')
#    time.sleep(0.01)
#    py.keyUp('left')
def derecha():
    py.press('right')
    py.press('right')
#    time.sleep(0.01)
#    py.keyUp('right')

def calcularAreaD():
    Box = (1060, 312, 1070, 322)
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def calcularAreaI():
    Box = (900, 506, 910, 516)
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def calcularAreaArbol():
    #Box = (930, 180, 940, 475) #cafe
    Box = (740, 465, 750, 475) #azul
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()
#azul = 337 arbol = 223 azulf=566
def run():
    time.sleep(3)

    a1 = calcularAreaD()
    a2 = a1
    derecha()

    while True:
       # time.sleep(0.005)
        a1 = calcularAreaD()
        if a2 == 337:
            derecha()

        else :#if a1 == b :
            izquierda()
        a2 = a1


   
run()