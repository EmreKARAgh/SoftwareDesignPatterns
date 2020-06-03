# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:00:08 2020

@author: EmreKARA
"""
import abc
class KeyboardMeta(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    def pressD(self):
        pass
    def pressS(self):
        pass
    def pressW(self):
        pass
    def pressA(self):
        pass
class GamepadMeta(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    def pressX(self):
        pass
    def pressA(self):
        pass
    def pressY(self):
        pass
    def pressB(self):
        pass
class KeyboardController(KeyboardMeta):
    def __init__(self):
        KeyboardMeta.__init__(self)
    def pressD(self):
        print('shooting.')
    def pressS(self):
        print('passing.')
    def pressW(self):
        print('loft passing')
    def pressA(self):
        print('throughing')

class GamepadController(GamepadMeta):
    def __init__(self):
        GamepadMeta.__init__(self)
    def pressX(self):
        print('shooting.')
    def pressA(self):
        print('passing.')
    def pressY(self):
        print('loft passing')
    def pressB(self):
        print('throughing')

class Adapter(KeyboardMeta):
    def __init__(self, gamepadController):
        KeyboardMeta.__init__(self)
        self.gamepadController = gamepadController
    def pressD(self):
        self.gamepadController.pressX()
    def pressS(self):
        self.gamepadController.pressA()
    def pressW(self):
        self.gamepadController.pressY()
    def pressA(self):
        self.gamepadController.pressB()
        

keyC = KeyboardController()
keyC.pressD()
keyC.pressS()
keyC.pressW()
keyC.pressA()


print('\nAfter Addapting:-------------------------------------------- ')
gamepadC = GamepadController()
adapter = Adapter(gamepadC)
adapter.pressD()
adapter.pressS()
adapter.pressW()
adapter.pressA()



