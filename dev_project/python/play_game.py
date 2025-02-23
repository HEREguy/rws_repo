
def ask_age():
    age = input("What's your age? ")
    if int(age) <= 18:
        print("You are still wet behind the ears!")
    else:
        print("You are a grown up!")

ask_age()
