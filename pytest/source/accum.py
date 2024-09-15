class Accumulator:

    def __init__(self) -> None:
        self.__count = 0
        self.__brand = "Accumulator"
    
    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, count):
        self.__count = count

    def add_count(self, count=1):
        self.__count += count
