import json

class Staff(object):

    def __init__(self, name, surname, age, profession, married):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession
        self.married = married

    def __repr__(self):
        return F"{self.name}-{self.surname}"

    def to_json(self):
        data_ = {
            'name':self.name,
            'surname': self.surname,
            'age': self.age,
            'profession': self.profession,
            'married': self.married
        }
        return data_
    def present(self):
        return "{}\n{}\n{}\n{}\n{}\n".format(self.name, self.surname, self.age, self.profession, self.married)



with open("example_json.json", "r") as j_file:
    print(j_file)
    data = json.load(j_file)
    print(F"data is \n{data}")


staffs = []
for staf in data["staff"]:
    print("staf = {}".format(staf))
    staffs.append(
    Staff(

        name=staf["name"],
        surname=staf["surname"],
        age=staf["age"],
        profession=staf["profession"],
        married=staf["married"]

            )

        )
print(staffs)
filtered_staf=[]
for staf in staffs:
    if staf.profession == "programmer":
        print(staf.present())
        filtered_staf.append(staf.to_json())
json_data = {"staff":filtered_staf}
print(filtered_staf)
with open("filtered_json.json", "w") as json_file:
    json.dump(json_data,json_file,indent=4)
