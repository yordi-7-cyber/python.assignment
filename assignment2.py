students = {"yordanos": 21, "tinsae": 20, "feven": 22,"Lulit":20}
def HUCISA_Students(action, name=None, age=None):
    if action == "display":
        print("\n".join(f"{n}: {a}" for n, a in students.items()))
    elif action == "add" and name and age:
        students[name] = age
        print(f"{name} added.")
    elif action == "update" and name and age:
        if name in students: 
            students[name] = age
            print(f"{name}'s age updated.")
        else:
            print(f"{name} not found.")
    elif action == "remove" and name:
        if name in students:
            del students[name]
            print(f"{name} removed.")
        else:
            print(f"{name} not found.")
HUCISA_Students("display")
HUCISA_Students("add", "miko", 21)
HUCISA_Students("update", "surafel", 23)
HUCISA_Students("remove", "hananita")
HUCISA_Students("display")
