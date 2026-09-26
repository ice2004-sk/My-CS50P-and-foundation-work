#while True:
def main():
    time = input("What time is it? ").strip()
    h, m = time.split(":")

    t = convert(h,m)

    if 7 <= t <= 8:
        print ("breakfast time")
    elif 12 <= t <= 13:
        print ("It's lunch time")
    elif 18 <= t <= 19:
        print ("it's dinner time")
    else:
        print("")

def convert(h,m):
    newM = (float(m)/60) * 100
    newH = float(h) + (newM/100)
    return newH

main()