"""

"""

class Shape(object) :
    """

    """
    def __init__(self, number_of_side ) :
        self.number_of_side = number_of_side


class Triangle(Shape) :
    """

    """
    def __init__(self, side1, side2, side3) :
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


my_triangle = Triangle(3, 4, 5)

print(my_triangle.side1)
print(my_triangle.side2)

