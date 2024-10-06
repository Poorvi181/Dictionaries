Dic={
    "name":"Poorvi",
    "age":11,
    "country":"UK"
}
print(Dic)
print(Dic["country"])
print(Dic.keys())
print(Dic.values())

for i in Dic.keys():
    print(i,Dic[i])

if "country" in Dic:
    print(Dic["country"])
else:
    print("Key does not exist.")    
#dictionaries are mutable(changeable)
Dic["age"]=12
print(Dic)

del(Dic["age"])
print(Dic)

Dic["marks"]=[100,95,97,100]
print(Dic)
#nested dictionary
Classroom={
    "Poorvi":{
        "age":11,
        "height":180
    },
    "Pari":{
        "age":5,
        "height":150
    }
}

print(Classroom.keys())
print(Classroom.values())
for i in Classroom.keys():
    print(i,Classroom[i])
print(Classroom["Pari"]["age"])










