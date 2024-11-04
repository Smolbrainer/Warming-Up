#Welcome to my collection of madlibs! What are madlibs? They are short, silly stories based on your words. Just pick ten words and read your own short story!
#Stolen from https://www.glowwordbooks.com/blog/category/kids-online-mad-libs/

def start():
    story = int(input("What do you want the story to be about? 1: Tacos, 2: Jobs, and 3: Photo Shoot. "))
    if story == 1:
        tacos()
    elif story == 2:
        jobs()
    elif story == 3:
        photoShoot()    
    else:
        print("Make sure to select one of the options")
        start()

def gameOver():
    input("Press enter to start again")
    start()

def tacos():
    adjective = str(input("Give me an Adjective of your choice: "))
    foods1 = str(input("Give me a food in plural of your choice: "))
    verb = str(input("Give me a Verb of your choice: "))
    saying = str(input("Give me a Saying of your choice: "))
    noun = str(input("Give me a Noun of your choice: "))
    foods2 = str(input("Give me a second food in plural of your choice: "))
    color = str(input("Give me a Color of your choice: "))
    ride = str(input("Give me a something you could ride in: "))
    animal = str(input("Give me an Animal your choice: "))
    person = str(input("Give me a person of your choice: "))

    print(f"Today I went to my favorite Taco Stand called the {adjective} {animal}. Unlike most food stands, they cook and prepare the food in a {ride} while you {verb}. The best thing on the menu is the {color} {noun}. Instead of ground beef they fill the taco with {foods2}, cheese, and top it off with a salsa made from {foods1}. If that doesn't make your mouth water, then it's just like {person} always says: {saying}! ")
    gameOver()

def jobs():
    occupation = str(input("Give me an Occupation of your choice: "))
    noun1 = str(input("Give me a Noun of your choice: "))
    adjective1 = str(input("Give me an Adjective of your choice: "))
    noun2 = str(input("Give me a Noun of your choice: "))
    verb = str(input("Give me a Verb of your choice: "))
    adjective2 = str(input("Give me an Adjective of your choice: "))
    noun3 = str(input("Give me a Noun of your choice: "))
    verb2 = str(input("Give me a Verb of your choice: "))
    noun4 = str(input("Give me a Noun of your choice: "))
    verb3 = str(input("Give me a Verb of your choice: "))

    print(f"Today a {occupation} named {noun4} came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to {verb2} around (a) {adjective1} {noun3}. She said it was easy for her to learn her job because she loved to {verb} when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a) {adjective2} {noun1}. That's very important! If you get too distracted in that situation you won't be able to {verb3} next to (a) {noun2}!")
    gameOver()

def photoShoot():
    animal = str(input("Give me an Animal your choice: "))
    feeling = str(input("Give me a feeling your choice: "))
    things1 = str(input("Give me a thing in plural of your choice: "))
    professional = str(input("Give me a professional like a Baker: "))
    clothing = str(input("Give me a piece of clothing of your choice: "))
    things2 = str(input("Give me a thing in plural of your choice: "))
    person = str(input("Give me a person of your choice: "))
    place = str(input("Give me a place of your choice: "))
    verb = str(input("Give me a Verb ending in ing of your choice: "))
    food = str(input("Give me a food of your choice: "))

    print(f" Say '{food},' the photographer said as the camera flashed! {person} and I had gone to {place} to get our photos taken today. The first photo we really wanted was a picture of us dressed as {animal} pretending to be a {professional}. When we saw the proofs of it, I was a bit {feeling} because it looked different than in my head. (I hadn't imagined so many {things1} behind us.) However, the second photo was exactly what I wanted. We both looked like {things2} wearing {clothing} and {verb}--exactly what I had in mind!")
    gameOver()

start()


















start()