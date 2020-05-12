# -*- coding: utf-8 -*-
# Öncelik sınıfları farklı kişiler ID numarası vererek randevu alır.

from abc import ABC, abstractmethod
import inspect

def get_class_from_frame(fr): #https://stackoverflow.com/a/17065724/8149411
  args, _, _, value_dict = inspect.getargvalues(fr)
  # we check the first parameter for the frame function is
  # named 'self'
  if len(args) and args[0] == 'self':
    # in that case, 'self' will be referenced in value_dict
    instance = value_dict.get('self', None)
    if instance:
      # return its class
      return getattr(instance, '__class__', None)
  # return None otherwise
  return None

class Livings:
    def __init__(self,cry=None):
        frame = inspect.stack()[1][0]
        caller = str(get_class_from_frame(frame))
        if(caller == '__main__.Human' or caller == '__main__.Cat'):
            self._cry=cry
        else:
            frame = inspect.stack()[1][0]
            caller = str(get_class_from_frame(frame))
            print('\n\n Caller ', caller)
            raise ValueError
    def getCry(self):
        return self._cry
class Human(Livings):
    def __init__(self,cry):
        frame = inspect.stack()[1][0]
        caller = str(get_class_from_frame(frame))
        if(caller == '<class \'__main__.HumanMom\'>'):
            self._cry=cry
        else:
            frame = inspect.stack()[1][0]
            caller = str(get_class_from_frame(frame))
            print('\n\n Caller ', caller)
            raise ValueError
class Cat(Livings):
    def __init__(self,cry):
        frame = inspect.stack()[1][0]
        caller = str(get_class_from_frame(frame))
        if(caller == '<class \'__main__.CatMom\'>'):
            self._cry=cry
        else:
            frame = inspect.stack()[1][0]
            caller = str(get_class_from_frame(frame))
            print('\n\n Caller ', caller)
            raise ValueError
class Mother(ABC):
    @abstractmethod
    def giveBirth(self,cry):
        pass
class HumanMom(Mother):
    def giveBirth(self,cry):
        return Human(cry)
class CatMom(Mother):
    def giveBirth(self,cry) ->Livings :
        return Cat(cry)




humanEmre = HumanMom().giveBirth(cry='aaa')
catEmre = CatMom().giveBirth(cry='meow')
print('Humans are  cry like: ', humanEmre.getCry())
print('Cats are cry like: ', catEmre.getCry())

#Cat('meow')
#Human('aaa')

