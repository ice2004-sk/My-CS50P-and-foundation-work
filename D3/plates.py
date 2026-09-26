def main():

    s = input("Plate: ").upper().strip()

    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    c = 0

    if 2 <= len(s) <= 6:
        
        if not (65 <= ord(s[0]) <= 90) or not (65 <= ord(s[1]) <= 90):
            return False        

        for i in s:
            if 65 <= ord(i) <= 90:
                c += 1
            elif 48 <= ord(i) <= 57:
                break
            else:
                return False  # Reject punctuation, spaces, or symbols

        if c < 2:
            return False

        # First number cannot be '0'
        if c < len(s) and s[c] == '0':
            return False

        while c < len(s):
            if 48 > ord(s[c]) or ord(s[c]) > 57:
                return False
            c += 1

        return True

    return False
main()