class StringToDictionary:
    def __init__(self, name, string):
        self.name = name
        self.str1 = string



    def dictionary(self):
        string1 =self.str1 
        my_dict = {}
        for letter in self.str1:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        return  F"{self.name} of string is {my_dict}"

dictionary = StringToDictionary("Dictionary",input("Wright your text here\n"))
print(dictionary.dictionary())