

def getStudentById(student_data : list,id :int):
    for i in student_data:
        if(i["ID"]==id):
            return i
def getStudents(student_data:list):
    for i in student_data:
        print(i)   

def getStudentByMajor(data,major):
    students=[]
    for i in data:
        if(i["Major"]==major):
            students.append(i)
    return students

def addStudent(id,name,age,major,gpa,data:list):
    new_student={"ID":id,"Name":name,"Age":age,"GPA":gpa}
    data.append(new_student)

def commonMajor(data1,data2):
    
    majors_data1=set()
    majors_data2=set()
    for x in data1:
        majors_data1.add(x["Major"])
    for x in data2:
        majors_data2.add(x["Major"])
    common= majors_data1.intersection(majors_data2)
    return common

def removeById(data:list,id):
    for i in range(data):
        student=data[i]
        if(student["ID"]==id):
            data.remove(data[i])
            break

def getAverage(data:list):
    sum=0
    for i in data:
        sum+=i["GPA"]
    avg=sum/len(data)
    return avg

def terminate():
    exit()