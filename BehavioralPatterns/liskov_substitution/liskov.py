# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:58:32 2020

@author: EmreKARA
"""

import abc
class DownloadingSource(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    def download(self):
        pass
class PausableDownloadingSource(DownloadingSource):
    def __init__(self):
        DownloadingSource.__init__(self)
    def pause(self):
        pass
    def resume(self):
        pass
class Source1(PausableDownloadingSource):
    def __init__(self):
        PausableDownloadingSource.__init__(self)
    def download(self):
        print('downloading from Source1 ...')
    def pause(self):
        print('Source 1 paused.')
    def resume(self):
        print('Source 1 resuming...')
class Source2(PausableDownloadingSource):
    def __init__(self):
        PausableDownloadingSource.__init__(self)
    def download(self):
        print('downloading from Source2 ...')
    def pause(self):
        print('Source 2 paused.')
    def resume(self):
        print('Source 2 resuming...')
class Source3(DownloadingSource):
    def __init__(self):
        DownloadingSource.__init__(self)
    def download(self):
        print('downloading from Source3 ...')
        
src1 = Source1()
src2 = Source2()
src3 = Source3()

src1.download()
src2.download()
src3.download()

print()
src1.pause()
src2.pause()

print()
src1.resume()
src2.resume()

#src3.pause()


