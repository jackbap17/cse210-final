class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def add(self, other):
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x,y)

    def equals(self, other):
        return self._x == other.get_x() and self._y  == other.get_y()

    def hits(self, other):
        return (self._x == other.get_x() or self._x + 1 == other.get_x() or self._x -1 == other.get_x()) and (self._y == other.get_y() or self._y - 1 == other.get_y())
    


    def get_x(self):
        return int(self._x)

    def get_y(self): 
        return int(self._y)

    def is_zero(self):
       return self._x == 0 and self._y == 0