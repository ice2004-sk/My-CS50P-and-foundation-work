ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip()
ans = ans.upper()


match ans:
    case "42" | "FORTY-TWO" | "FORTY TWO":
        print ("Yes")

    case _:
        print ("No")
