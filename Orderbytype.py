import time


while True:
    stuff = [56,5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F", ("abc") ]
    break
if type(stuff[0]) is str:
    print("string found")
else:
    print("string not found...")

if type(stuff[1]) is int:   
    print("interger found")
else:
    print("interger not found...")

if type(stuff[2]) is float:
    print("float found")
else:
    print("float not found...")

if type(stuff[4]) is bool:
    print("booleans found")
else:
    print("booleans not found...")
