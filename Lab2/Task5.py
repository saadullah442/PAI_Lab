students = {
    "S1": {"name": "Alice", "marks": 85},
    "S2": {"name": "Bob", "marks": 72},
    "S3": {"name": "Charlie", "marks": 91},
    "S4": {"name": "Diana", "marks": 88},
    "S5": {"name": "Ethan", "marks": 76},
    "S6": {"name": "Fiona", "marks": 95},
    "S7": {"name": "George", "marks": 67},
    "S8": {"name": "Hannah", "marks": 82},
    "S9": {"name": "Ian", "marks": 79},
    "S10": {"name": "Julia", "marks": 90}
}

def addStudent(newName , newMarks, studentNumber):
    students[f"S{studentNumber}"] = { "name": newName , "marks": newMarks}

def updateMarks(findName , newMarks):
    for x in students.values():
        if(x['name'] == findName):
            x['marks'] = newMarks
            break

def deleteStudent(studName):
    for id , x in students.items():
        
        if(studName == x["name"]):
            del students[id]
            break
        

def findTopper():
    highestMarks = -9999
    for x in students.values():
        if(x["marks"] > highestMarks):
            highestMarks = x["marks"]
    print(f"{highestMarks =:>5}")

print("Before deleting student")
for id , x in students.items():
    print(f"{id=:<10} {x}")

addStudent("idk" , 100 , 11)
updateMarks("Fiona" , 0)
deleteStudent("George")
findTopper()
print("\n\n")
for id , x in students.items():
    print(f"{id=:<10} {x}")
