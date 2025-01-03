#!/usr/bin/python3
from models.base_model import BaseModel

# Create a new BaseModel instance
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print attributes of the initial instance
print(my_model.id)
print(my_model)
print(type(my_model.created_at))

# Convert to dictionary
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

# Create a new instance using the dictionary
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

# Check if they are the same instance
print("--")
print(my_model is my_new_model)
