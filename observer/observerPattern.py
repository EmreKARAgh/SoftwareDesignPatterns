# -*- coding: utf-8 -*- Stabilizer Active and Passive
import abc
from threading import Thread
from random import randint
import time

class StabiliserMeta(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    def notify(self):
        pass
class A_Stabiliser(Thread, StabiliserMeta):
    def __init__(self, name, motionSensor):
        Thread.__init__(self)
        StabiliserMeta.__init__(self)
        self._counter = 5
        self._name = name
        self._motionSensor = motionSensor
    def notify(self):
        self.run()
    def run(self):
        print(self._name, 'Oh! I\'m notified')
        self._counter -= 1
        if self._counter == 0:
            self._motionSensor.unRegisterObserver(self, 'A_Type')
class B_Stabiliser(Thread, StabiliserMeta):
    def __init__(self,name, motionSensor):
        Thread.__init__(self)
        StabiliserMeta.__init__(self)
        self._name = name
        self._counter = 2
        self._motionSensor = motionSensor
    def notify(self):
        self.run()
    def run(self):
        print(self._name, 'Oh! I\'m notified')
        self._counter -= 1
        if self._counter == 0:
            self._motionSensor.unRegisterObserver(self, 'B_Type')
class MotionSensor(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._observersA =  []
        self._observersB =  []
        self._motion = 0
    def registerObserver(self, stabiliser: StabiliserMeta, typeInfo: str):
        if typeInfo == 'A_Type':
            self._observersA.append(stabiliser)
        elif typeInfo == 'B_Type': 
            self._observersB.append(stabiliser)    
    def unRegisterObserver(self, stabiliser: StabiliserMeta, typeInfo:str):
        if typeInfo == 'A_Type':
            self._observersA.remove(stabiliser)
        elif typeInfo == 'B_Type': 
            self._observersB.remove(stabiliser)    
    def _notifyObservers(self):
        if self._motion < 50:
            observers = self._observersA
        else:
            observers = self._observersB
        for observer in observers:
            observer.notify()
    def run(self):
        while(len(self._observersA) !=0 and len(self._observersB) !=0):
            self._motion = randint(1,100)
            self._notifyObservers()
            time.sleep(0.2)

ms = MotionSensor()
for i in range(5):
    sta = A_Stabiliser(('A_Stabiliser'+str(i+1)),ms)
    ms.registerObserver(sta, 'A_Type')
    stb = B_Stabiliser(('B_Stabiliser'+str(i+1)),ms)
    ms.registerObserver(stb, 'B_Type')
ms.start()

