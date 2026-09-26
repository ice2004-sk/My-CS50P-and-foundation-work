fruits = {"Apple" : 130, "Avocado" : 50,
            "Banana" : 110, "Cantaloupe" : 50,
            "Grapefrduit" : 60, "Grapes" : 90,
            "Honeydew Melon" : 50, "Kiwifruit" : 90,
            "Lemon" : 15, "Lime" : 20, "Nectarine" : 60,
            "Orange" : 80, "Peach" : 100, "Pineapple" : 50,
            "Plums" : 70, "Strawberries" : 50, "Sweet Cherries" : 100,
            "Tangerine" : 50, "Watermelon" : 80}
    
user = input("").lower()
user = user.title()

if user in fruits:
    print (fruits[user])