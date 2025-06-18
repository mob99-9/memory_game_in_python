import random

#create randomizer
def randomizer():
    global shuffled_code
    code = ""
    alphabets = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g",
                 "H","h","I","i","J","j","K","k","L","l","M","m","N","n",
                 "O","o","P","p","Q","q","R","r","S","s","T","t","U","u",
                 "V","v","W","w","X","x","Y","y","Z","z"]
    numbers = ["1", "2", "3", "4", "5","6","7","8","9","0"]

    for counter in range(0,6):
        random_letter = alphabets[random.randint(1,52)]
        code += random_letter
    
    for counter_number in range(0,2):
        random_number = numbers[random.randint(1,9)]
        code += random_number

    shuffled_code = "".join(random.sample(code, len(code)))    

    print(shuffled_code)
#create timer and blocker
randomizer()
#create score shower