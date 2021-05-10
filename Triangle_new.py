class Shape:
    def __init__(self, name):
        self.name = name
        
    def present_shape(self):
        return F"This is a geometric figure and it's name is {self.name} "

class Triangle(Shape):

    def __init__(self, name, side1, side2, base, height):
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height
        super().__init__(name)

    def present_triangle(self):
        return F" This geometric figure has three sidеs equal {self.side1}, {self.side2} , {self.base} and with height equal {self.height} and we called it {self.name}"

    def triangle_area(self):    
        return F"The area of {self.name} equally {(self.base * self.height)/2}"
    def triangle_perimetr(self):
        return F"The perimetr of {self.name} equally {self.side1 + self.side2 + self.base}"

class Square(Shape):

    def __init__(self, name, side_1, side_2):
        self.sidе_1 = side_1
        self.side_2 = side_2
        super().__init__(name)

    def present_square(self):
        return F"This geometric figure is {self.name} has four sidеs equal {self.side_1}, {self.side_2}  "

    def square_area(self):
        return F"The are of {self.name} equal {self.side_1 * self.side_2}"
    def square_perimetr(self):
        return F"The perimetr of {self.name} equal {2 * side_1 + 2 * side_2}"
    def square_diagonal(self):
        return F"We will use the Pythagorean theorem and calculate the diogonal of the {self.name} which equal {(self.side_1*2+self.side_2**2)**1/2}"
                  

shape = Shape("Triangle")
print(shape.present_shape())
print("\n\n")
triangle =Triangle("Triangle" , 10, 15, 20, 10)
print(triangle.present_triangle())
print(triangle.triangle_area())
print(triangle.triangle_perimetr())
shape1 = Shape("Square")
print(shape1.present_shape())
print("\n\n")

square1 = Square("Square", 6, 8)

print(square1.present_square())

print(square1.square_area())
print(square1.square_perimetr())
print(square1.square_diagonal())