students=["harsh","king","siva","maliik","nani"]
attendence=[["absent","present","absent","present","absent","absent"],["present","present","absent","absent","absent","present"],["absent", "absent", "present", "absent", "present", "absent"],
    ["present", "present", "present", "present", "present", "present"],
    ["present", "absent", "present", "present", "absent", "present"]]
count_absent=[0,0,0,0,0]
status=[]
for index,value in enumerate(students):
    c1=0
    for index1,value1 in enumerate(attendence[index]):
        if value1 != "present" and value1!= "absent":
            continue
        
        if value1=="absent":
            c1+=1
        count_absent[index]=c1
       

    if count_absent[index]>=3: 
        status.append("NEEDS INTREVENTION")
    else:
        status.append("ok")
for index,value in enumerate(students):
    print("")
    print("")
    print(f"student name is {value} ") 
    print("")
    print(f"the absent days are {count_absent[ index]}")
    print("")
    print(f"and the status is {status[index]}")
sum=0

for value in count_absent:
    sum=sum+value
average=sum/len(count_absent)

print("average is :" , average)

print("the students who needs intrevention")

for k1 in status:
    if k1 == "NEEDS INTREVENTION":
        break ## due to break no else case execution  
else:
    print("No students need intervention.")

for index,k in enumerate(status):
    if k=="NEEDS INTREVENTION":
        print(students[index])
    
