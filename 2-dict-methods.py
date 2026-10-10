marks = { "devasish":45,
        "sonu": 56,
           " ramesh": 100
}
print(marks,type(marks))
print(marks,["harry"])

print(marks.items())

print(marks.keys())

print(marks.values())
marks.update({"sonu":55})   
print(marks.get("sonu"))