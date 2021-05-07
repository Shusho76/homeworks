class StringToDictionary:
    def __init__(self, name, string):
        self.name = name
        self.str1 = string
        self.dict = {}
        for key in self.str1:
        	self.dict[key] = 1
        print(F"{self.name} of string is {self.dict}") 

dictionary = StringToDictionary("Dictionary",input("Wright your text here\n"))
