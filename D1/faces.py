def convert(x):
    return x.replace(":(" , "🙁").replace(":)" , "🙂")

def main():
    emoji = input(":( or :)")
    print(convert(emoji))

main()
