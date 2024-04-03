import re 
regrex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
new_password = "HeLloWo5@"
validation = re.match(regrex,new_password)
if validation:
    print(validation)
    print("Valid Password")
else:
    print("not valid")