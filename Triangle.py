class Shape:
	def __init__(self, name):
		self.name = name

	def present_shape(self):
		return F"This is geometric figure and it's name is{self.name}"

class Triangle(Shape):
	def__init__(self, name, side1, side2, base, height):
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height
        super__init__(name):


    def present_triangle(self):
        return F" This geometric figure has three sides and we coled it {self.name}"

    def triangle_area:    
    	return F"The area of {self.name} equally {(self.base * self.height)/2}"
    def triangle_perimetr(self):
    	return F"The perimetr of {self.name} equally {self.side1 + self.side2 + self.base}"

triangle = Triangle("Triangle")
print(triangle.present_triangle())