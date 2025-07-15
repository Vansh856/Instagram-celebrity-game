import os
import random
famous_people = [
    {"name": "Cristiano Ronaldo", "birth_place": "Madeira, Portugal", "profession": "Footballer", "instagram_followers_millions": 653},
    {"name": "Lionel Messi", "birth_place": "Rosario, Argentina", "profession": "Footballer", "instagram_followers_millions": 504},
    {"name": "Selena Gomez", "birth_place": "Texas, USA", "profession": "Musician and Actress", "instagram_followers_millions": 420},
    {"name": "Dwayne Johnson", "birth_place": "California, USA", "profession": "Actor and Wrestler", "instagram_followers_millions": 394},
    {"name": "Kylie Jenner", "birth_place": "California, USA", "profession": "Entrepreneur and Media Personality", "instagram_followers_millions": 394},
    {"name": "Ariana Grande", "birth_place": "Florida, USA", "profession": "Musician and Actress", "instagram_followers_millions": 376},
    {"name": "Kim Kardashian", "birth_place": "California, USA", "profession": "Entrepreneur and Media Personality", "instagram_followers_millions": 357},
    {"name": "Beyoncé", "birth_place": "Texas, USA", "profession": "Musician and Actress", "instagram_followers_millions": 312},
    {"name": "Khloé Kardashian", "birth_place": "California, USA", "profession": "Media Personality", "instagram_followers_millions": 303},
    {"name": "Justin Bieber", "birth_place": "Ontario, Canada", "profession": "Musician", "instagram_followers_millions": 294},
    {"name": "Kendall Jenner", "birth_place": "California, USA", "profession": "Model and Media Personality", "instagram_followers_millions": 288},
    {"name": "Taylor Swift", "birth_place": "Pennsylvania, USA", "profession": "Musician", "instagram_followers_millions": 282},
    {"name": "Virat Kohli", "birth_place": "Delhi, India", "profession": "Cricketer", "instagram_followers_millions": 271},
    {"name": "Jennifer Lopez", "birth_place": "New York, USA", "profession": "Musician and Actress", "instagram_followers_millions": 249},
    {"name": "Neymar Jr.", "birth_place": "São Paulo, Brazil", "profession": "Footballer", "instagram_followers_millions": 229},
    {"name": "Nicki Minaj", "birth_place": "Trinidad and Tobago", "profession": "Musician", "instagram_followers_millions": 226},
    {"name": "Kourtney Kardashian", "birth_place": "California, USA", "profession": "Media Personality", "instagram_followers_millions": 219},
    {"name": "Miley Cyrus", "birth_place": "Tennessee, USA", "profession": "Musician and Actress", "instagram_followers_millions": 213},
    {"name": "Katy Perry", "birth_place": "California, USA", "profession": "Musician", "instagram_followers_millions": 204},
    {"name": "Zendaya", "birth_place": "California, USA", "profession": "Actress and Singer", "instagram_followers_millions": 179}
]
score = 0
rounds = 0
while True:
    
        comptation=random.sample(famous_people,k=2)
        print(f"Compare A: {comptation[0]['name']}, a {comptation[0]['profession']} from {comptation[0]['birth_place']} .")
        print("VS")
        print(f"Compare B: {comptation[1]['name']}, a {comptation[1]['profession']} from {comptation[1]['birth_place']} .")
        choice= input("Who has more Instagram followers? Type 'A' or 'B': ").strip().upper()
       
        if choice == 'A':
            if comptation[0]['instagram_followers_millions'] > comptation[1]['instagram_followers_millions']:
                print(f"You are right! {comptation[0]['name']} has more followers.")
                score += 5
                rounds += 1
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                print(f"You have finished{ rounds} rounds.")
                print(f"Your current score is: {score}")

            else:
                print(f"Sorry, {comptation[1]['name']} has more followers.")
                print(f"Your final score is: {score}")
                break
        elif choice == 'B':
            if comptation[1]['instagram_followers_millions'] > comptation[0]['instagram_followers_millions']:
                print(f"You are right! {comptation[1]['name']} has more followers.")
                score += 5
                rounds += 1
                os.system('cls' if os.name == 'nt' else 'clear')  #
                print(f"You have finished {rounds} rounds.")
                print(f"Your current score is: {score}")

            else:
                print(f"Sorry, {comptation[0]['name']} has more followers.")
                print(f"Your final score is: {score}")
                break  
        else:
            print("Invalid input. Please type 'A' or 'B'.")
                 
