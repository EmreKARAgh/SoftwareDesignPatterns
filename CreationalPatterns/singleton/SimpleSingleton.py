# -*- coding: utf-8 -*-
#1: Optional[...] is a shorthand notation for Union[..., None], telling the type checker that either an object of the specific type is required, or None is required.  Whenever you have a keyword argument with default value None, you should use Optional.
#2 https://stackoverflow.com/a/9663601/8149411
from __future__ import annotations
from typing import Optional


class CodeMeta(type):
    
    _instance: Optional[Code] = None  #1
    _data = 0
    def __call__(self,data=0) -> Code: #2
        if self._instance is None:
            self._instance = super().__call__()
            self._data = data
        return self._instance


class Code(metaclass=CodeMeta):
    def setData(self,data):
        self._data = data
    


s1 = Code()
s2 = Code()
print('s1._data:',s1._data, '  s2._data:',s2._data)
print()
print('s1.setData(5)')
s1.setData(5)
print()
print('s1._data:',s1._data, '  s2._data:',s2._data)
print()
print('id(s1):',id(s1), '\nid(s2):',id(s2))

