import json

req_file = "myjson.json"


# read json file
file = open(req_file, "r")

# convert string file to json obj
json_obj = json.load(file)
print(json_obj)

file.close()

# write dict to file
my_dict1 = {"Name": "Martin", "skills": ["Python", "Bash", "AWS"]}

req_file1 = "mydict1.json"

file1 = open(req_file1, "w")

# convert json obj to dict file
json.dump(my_dict1, file1, indent=4)
