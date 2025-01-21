#Adventure game
import random
print("******************** ADVENTURE GAME *********************")
name = input ("What is your name?\n")
print(f"Hi {name} Welcome to Let's Play a Game adventure!")
def play_game():
    print("You have just arrived in Nairobi, you're in Machakos country bus!")
    print("1. Extremly tired, locate the nearest Restaurant and have a lunch? ")
    print("2. Proceed directly to Bus station and take your Mathree to Embakasi? ")

    options = input("Pick one option?\n" )

    if options == '1':
        find_restaurant()
    elif options == '2':
        proceed_to_Bus_station()
    else:
        print("Invalid option")
      
        
def find_restaurant():
    print("You find the restaurant, and since you have not eaten since morning, what do you choose?")
    print("1. Buy some yummy chicken drum sticks? ")
    print("2. Buy ugali nyama? ")

    find_options = input("Pick one option?\n")

    if find_options == '1':
        print("That was quite delicious!, time to go home!!")
        proceed_to_Bus_station()
    elif find_options == '2':
        print("I'm quite full, home here I come!!")
        proceed_to_Bus_station()
    else:
        print("Invalid option")

def proceed_to_Bus_station():
    print("You arrive at the Bus station, You board a bus and arrive safely in your humble cottages in Embakasi! \n")
    print("Since your very tired, you take a nap at your sofa and your sucked in the time Portal!\n")
    print("As the light from the portal fades, you find yourself standing in the heart of a bustling village marketplace. Vibrant textiles hang from wooden stalls, baskets of fruits and grains line the paths, and the air is rich with the smell of cooking and spices. Children stop mid-play to stare at you, and adults begin murmuring in a language you don’t yet understand. Your modern clothes and disoriented demeanor make you stand out like a sore thumb. A silence falls as an elder, dressed in elaborate traditional garments, approaches you. His gaze is sharp and cautious. Behind him, villagers gather, their expressions a mix of curiosity and suspicion.")
    print("1. Speak the truth? ")
    print("2. Conceal your purpose? ")
    
    back_in_past_options = input("Pick one option?\n")
    if back_in_past_options == '1':
        truth()
    elif back_in_past_options == '2':
        conceal()
    else:
        print("Invalid option")

def truth():
    print("Its a noble choice even though it has its consequences")
    truth_events = ["1. Prove Yourself Through Action", "2. Share Knowledge of Future Events", "3. Expose Early Collaborators", "4. Rally Support for Resistance"]
    for events in truth_events:
        print(events)

    truth_options = input("Pick an option?\n")
    if truth_options == '1':
        print("Prove Yourself Through Action:\n")
        print("I am from the future, the British will come and pretend they want to preach about their god.")
        print("They will use this opportunity to colonize us using guns. They have already set sail and are coming here—that's why we have so many missionaries among us!")
        print("You must warn the neighboring village and stop them from signing treaties!")
    
    elif truth_options == '2':
        print("Share Knowledge of Future Events:\n")
        print("I have seen what happens when the British gain control. They will build railways and extract our resources, leaving our land barren.")
        print("If we unite now, we can prevent them from dividing us and taking our land!")
    
    elif truth_options == '3':
        print("Expose Early Collaborators:\n")
        print("Some among us have already started cooperating with the British, thinking they will gain wealth and power.")
        print("If we uncover their plans and reveal their betrayal, we can strengthen the village's resistance!")
    
    elif truth_options == '4':
        print("Rally Support for Resistance:\n")
        print("We must bring together all the tribes to stand as one. The British will exploit our divisions.")
        print("If we unite now, we can stop them before their influence grows too strong.")
    
    else:
        print("Invalid choice. Please pick a number between 1 and 4.")




def conceal():
    print("Its not in their best interest for the people to know the truth, and its allows you to work from the shadows")
    conceal_events = ["1. Blend In as a Helper.", "2. Spy on Colonial Movements.", "3. Mediate Local Conflicts", "4. Influence Through Subtle Warnings"]
    for con_events in conceal_events:
        print(con_events)

    conceal_options = input("Pick an option?\n")
    if conceal_options == '1':
        print("\nBlend In as a Helper:")
        print("You offer to help the villagers with their daily tasks—tending crops, fixing tools, or assisting in trade.")
        print("As you earn their trust, you gather insights into their concerns and slowly learn about their awareness of colonial activities.")
    
    elif conceal_options == '2':
        print("\nSpy on Colonial Movements:")
        print("You venture near a British camp under the guise of curiosity, listening to their plans and observing their interactions with local leaders.")
        print("You gather critical information, like maps or schedules, while keeping a low profile.")
    
    elif conceal_options == '3':
        print("\nMediate Local Conflicts:")
        print("You position yourself as a neutral outsider who can help resolve disputes between tribes or families.")
        print("By reducing internal divisions, you create a stronger foundation for future resistance without revealing your true intentions.")
    
    elif conceal_options == '4':
        print("\nInfluence Through Subtle Warnings:")
        print("You share hypothetical stories about the dangers of foreign invaders, carefully planting seeds of caution among the villagers.")
        print("They begin to discuss the Europeans with greater suspicion, unknowingly preparing themselves for resistance.")
    
    else:
        print("Invalid choice. Please pick a number between 1 and 4.")

play_game()
