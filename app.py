from abc import ABC, abstractmethod


class InvalidOperationException(Exception):
    pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#        if self.opened:
#            raise InvalidOperationException("Stream already opened")
#        self.opened = True
#
#     def close(self):
#        if not self.opened:
#            raise InvalidOperationException("Stream already opened")
#        self.opened = False
#     @abstractmethod
#     def read(self):
#         pass
#
# class FileStream(Stream):
#     def read(self):
#         print("read from file")
#
# class NetworkStream(Stream):
#     def read(self):
#         print("read from network")
#
# class MemoryStream(Stream):
#     def read(self):
#         print("read from Memory")
#
#
# stream = FileStream()
# stream.read()
# stream.open()
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point1 = Point(1, 2)
point2 = Point(3, 4)
print(f"{id(point1)}, {id(point2)}")
