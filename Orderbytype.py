stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F", ("abc") ]

if type(stuff[0]) is str:   #type(stuff[0]) geeft het datatype van het eerste item in de list 
    print("string found")

if type(stuff[1]) is int:   #type(stuff[0]) geeft het datatype van het eerste item in de list 
    print("interger found")

if type(stuff[2]) is float:   #type(stuff[0]) geeft het datatype van het eerste item in de list 
    print("float found")

    if type(stuff[3]) is bool:   #type(stuff[0]) geeft het datatype van het eerste item in de list 
        print("booleans found")
    else:
        print("booleans not found...")