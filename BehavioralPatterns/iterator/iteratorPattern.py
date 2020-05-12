from __future__ import annotations
from collections.abc import Iterable, Iterator
import abc
from typing import Any, List
from random import randint
from threading import Thread

def printPlayers(collection, iterator):
    while True:
        try:
            nextPlayer = next(iterator)
            print(nextPlayer.getInfo())
        except StopIteration:
            break
    print("")
class PlayerHandlerMeta(metaclass=abc.ABCMeta):
    def __init__(self, collection):
        pass
    def createIterator(self):
        pass
class PlayerHandler(PlayerHandlerMeta):
    def __init__(self, collection):
        self._collection = collection
        self._straight_iter = None
        self._reverse_iter = None
        self.createIterator()
    def createIterator(self):
         self._straight_iter = self._collection.__iter__()
         self._reverse_iter = self._collection.get_reverse_iterator()
    def handle(self):
        t1 = Thread(target=printPlayers, args=(self._collection, self._straight_iter,))
        t2 = Thread(target=printPlayers, args=(self._collection, self._reverse_iter,))
        
        print("Straight traversal:\n")
        t1.start()
        t1.join()
        
        print("Reverse traversal:\n")
        t2.start()
        t2.join()
class Player:
    def __init__(self, name: str, priority: int):
        self._priority = priority
        self._name = name
    def getInfo(self):
        return [self._priority, self._name]
    def getPriority(self):
        return self._priority

class PriorityOrderIterator(Iterator):
    _reverse: bool = False
    _position = 0
    def __init__(self, collection: PlayersCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._collection = sorted(self._collection, key = lambda player: player.getPriority(), reverse=self._reverse)        
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class PlayersCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> PriorityOrderIterator:
        return PriorityOrderIterator(self._collection)

    def get_reverse_iterator(self) -> PriorityOrderIterator:
        return PriorityOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)




if __name__ == "__main__":
    collection = PlayersCollection()
    for i in range(5):
        plr = Player(name=('Player'+str(i+1)),priority = randint(1,5))
        collection.add_item(plr)
    
    ph = PlayerHandler(collection)
    ph.handle()
    
    