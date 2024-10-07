
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# OCP = open for extension, closed for modification

'''
    BAD : making changes on the fly is not recommended 
          and should not be practiced
'''

class ProductFilter:
    def filter_by_color(self, products, color) -> None:
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size) -> None:
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color) -> None:
        for p in products:
            if p.color == color and p.size == size: yield p 

'''
    GOOD : Solution [ Specification ]
'''

# base class
class Specification:
    def is_satisfied(self, item) -> None:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

# base class
class Filter:
    def filter(self, items, specs) -> None:
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item) -> object:
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item) -> object:
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item) -> bool:
        return all( map( lambda spec: spec.is_satisfied(item), self.args ) )

class BetterFilter(Filter):
    def filter(self, items, spec) -> None:
        for item in items:
            if spec.is_satisfied(item): yield item

if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL) 
    tree = Product('tree', Color.GREEN, Size.LARGE) 
    house = Product('house', Color.BLUE, Size.LARGE) 


    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green prodcuts (OLD)")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    bf = BetterFilter()
    print("Green prodcuts (NEW)")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large Products")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")
    
    print("Large blue items")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")

    print("Small green items")
    small = SizeSpecification(Size.SMALL)
    small_green = small & ColorSpecification(Color.GREEN)
    for p in bf.filter(products, small_green):
        print(f" - {p.name} is small and green")


