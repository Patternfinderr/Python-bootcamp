# LSP 

class Rectangle:
    def __init__(self, width:int, height:int) -> None:
        self._width = width
        self._height = height

    @property
    def area(self):
        """The area property."""
        return self._width * self._height

    def __str__(self) -> None:
        return f"width: {self.width}\nheight: {self.height}"

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value:int) -> None:
        self._width = value

    @property
    def height(self) -> int:
        """The height property."""
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    """
        These setter is what violates the 
        liskov substitution principle 
        : better to avoid this overall
    """
    @Rectangle.width.setter
    def width(self, value) -> None:
        self._width = self._width = value
    
    @Rectangle.height.setter
    def height(self, value) -> None:
        self._height = self._height = value

"""
    use_it functions run only for Rectangle class
    and does not work on any derived classes

    rc.height = 10 also not a good practice but because 
    the function itself is if only used for rectangle then 
    only then for this case this function is good Rectangle class
    but for any derieved class this function is garbage
"""
def use_it(rc) -> None:
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


