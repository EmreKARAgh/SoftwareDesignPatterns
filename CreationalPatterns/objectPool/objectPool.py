from __future__ import annotations
from threading import RLock, Thread, Condition
from typing import Optional
import time
import random
import queue

class Obstacle:
    def __init__(self,name):
        self.name = name
class ObstaclePoolMeta(type):
    _instance: Optional[ObstaclePool] = None
    _lock: RLock = RLock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class ObstaclePool(metaclass=ObstaclePoolMeta):
    def __init__(self) -> None:
        self._pool = queue.Queue(maxsize=5)
        self._queue = queue.Queue(maxsize=3)
        self._fillPool(self._pool)
    def getObject(self,thr):
        with threadLock:
            if not self._pool.empty():
                thr.myObs = self._pool.get()
                print(thr.name + ' get obs from pool ' + thr.myObs.name)
            else:
                if self._queue.qsize() < 3:
                    self._queue.put(thr)
                    thr.queue = self._queue.qsize() -1
    def releaseObject(self,obs):
        with threadLock:
            self._pool.put(obs)
            obs = None
            del(obs)
            if self._queue.qsize() > 0:
                nextThread = self._queue.get()
                nextThread.queue= None
                nextThread.myObs = self._pool.get()
                print(nextThread.name + 'get obs from queue ' + nextThread.myObs.name)
                nextThread.pause() #if the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.
                nextThread.resume()
    def _fillPool(self,_pool):
        with threadLock:
            for i in range(5):
                _pool.put(Obstacle('Obstacle'+str(i)+''))
            print('Pool filled', self._pool.qsize())
                
class ObstacleThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        self.myPool = ObstaclePool()
        self.paused = False
        self.pause_cond = Condition(RLock())
        self.status = 'Not Handled Yet.'
        self.queue = None
        self.myObs = None
    def run(self):
        for i in range(25):
            self.myPool.getObject(self)
            if self.myObs is not None:
                with threadLock:
                    self._updateStatus((self.name + ' using ' + self.myObs.name +' ...'))
                self._process()
            elif self.queue is not None:
                with threadLock:
                    self._updateStatus((self.name + ' is in the queue. Waiting in line ' + str(self.queue)))
                self.pause()
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()
            else:
                with threadLock:
                    self._updateStatus((self.name + ' waiting outside the queue.'))
                    
                time.sleep(2+random.random())
                
    def _process(self):
        time.sleep(random.random())
        with threadLock:
            print(self.name + ' done with ' + self.myObs.name)
        self.myPool.releaseObject(self.myObs)
        self.myObs = None
        time.sleep(2+random.random())
    def pause(self):
        self.paused = True
        self.pause_cond.acquire()
    def resume(self):
        self.paused = False
#        self.pause_cond.notify()
        self.pause_cond.release()
    def _updateStatus(self,status):
        self.status = status
        print(self.status)
        
threadLock = RLock()
for i in range(10):
    ObstacleThread('Thread'+str(i)+'').start()