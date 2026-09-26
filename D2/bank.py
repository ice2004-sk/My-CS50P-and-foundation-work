greeting = input("Greeting: ").strip()
greeting = greeting.upper()

if greeting[:5] == "HELLO":
    print ("$0")
elif greeting[:1] == "H" and greeting[:5] != "HELLO":
    print("$20")
else:
    print("$100")
