import time


while True:
    stuff = ["hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F", ("abc") ]
    break
if type(stuff[0]) is str:
    print("string found")
else:
    print("string not found...")

if type(stuff[4]) is int:   
    print("interger found")
else:
    print("interger not found...")

if type(stuff[6]) is float:
    print("float found")
else:
    print("float not found...")

if type(stuff[1]) is bool:
    print("booleans found")
else:
    print("booleans not found...")