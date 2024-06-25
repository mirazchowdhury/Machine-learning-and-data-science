#dictionary is an ordered collection of items.It stores item in the keyvalue pairs. Ex: dict = {'Name':'Miraj','ID':'C201074'}

"""dict_1 = {'Name':'Miraj'}
print(type(dict_1))

student = {"Name":"Miraj","Age":23,"Courses":["ML","IP","NN"],"CreditHours":(3,4,3),"Grade":{"A+","A","A-"},"CGPA":3.101,"C":4+5j}
print(student)

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

dict_2=dict(name = "jon",age = 36)
print(dict_2)
print(type(dict_2))"""

"""employee = dict(name = "miraj",skills = ["Python","FLask","Go"],years_of_experience = 4)
print(employee["years_of_experience"])
print(employee)"""

"""print(employee["salary"])""" #will give key error

"""
#get()
print(employee.get("name"))
print(employee.get("salary"))
print(employee.get("CGPA",3.69))
"""
#change_items
"""employee["name"] = "Siraj"
print(employee)"""
#another_method_by_using_update()

"""employee.update(
    {
        "name" : "Jalal",
        "years_of_experience": 10
    }
)
print(employee)"""