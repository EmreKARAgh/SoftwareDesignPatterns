# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:08:36 2020

@author: EmreKARA
"""
import abc
import math
class Employer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def getPosition(self):
        return self.position
class MediatorMeta(metaclass = abc.ABCMeta):
    def __init__(self):
        pass
    def notify(self):
        pass
    def addEmployer(self):
        pass
    def calculateDistance(self):
        pass
class Mediator(MediatorMeta):
    def __init__(self):
        MediatorMeta.__init__(self)
        self.employers = []
    def notify(self, position):
        min_distance = float("inf")
        optimumEmployer = None
        for employer in self.employers:
            distance = self.calculateDistance(position, employer.getPosition())
            if(distance < min_distance):
                min_distance = distance
                optimumEmployer = employer
        return optimumEmployer
        
    def addEmployer(self, employer):
        self.employers.append(employer)
    def calculateDistance(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distance = math.sqrt((math.pow((x2-x1),2)+math.pow((y2-y1),2)))
        return distance
class Employee:
    def __init__(self,name, position, mediator):
        self.name = name
        self.position = position
        self.mediator = mediator
        self.employer = None
    def notify(self):
        self.employer = self.mediator.notify(self.position)

mediator = Mediator()

allEmployers = []
for i in range(1,6,2):
    name = 'Employer'+str(i)
    position = (i,i)
    employer = Employer(name,position)
    mediator.addEmployer(employer)
    allEmployers.append(employer)
    


allEmployees = []
for i in range(1,6):
    name = 'Employee'+str(i)
    position = (i,i)
    allEmployees.append(Employee(name,position, mediator))
    
for employee in allEmployees:
    employee.notify()
    print(employee.name+'\'s', 'employer is', employee.employer.name)


        
