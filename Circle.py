class Circle:

    def __init__ (self, name, radius):
        self.name = name
        self.R = radius

    def perimetr (self):
        circle_perimetr = 2 * 3.14 *(self.R)
        return  F"{self.name} of circle is {circle_perimetr}" 
    def area (self):
        circle_area = 3.14 * (self.R^2)
        return F'{self.name} of circle is {circle_area}'

perimetr = Circle("Perimetr", 15)
area = Circle("Area", 15)
print(perimetr.perimetr())
print(area.area())

