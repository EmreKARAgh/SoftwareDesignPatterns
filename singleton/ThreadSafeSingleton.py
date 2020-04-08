# -*- coding: utf-8 -*-
from __future__ import annotations
from threading import Lock, Thread
from typing import Optional

class CodeMeta(type):
    _instance: Optional[Code] = None

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Code(metaclass=CodeMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

def test_singleton(value: str) -> None:
    singleton = Code(value)
    print(singleton.value)


process1 = Thread(target=test_singleton, args=("Protected",))
process2 = Thread(target=test_singleton, args=("Private",))
process1.start()
process2.start()