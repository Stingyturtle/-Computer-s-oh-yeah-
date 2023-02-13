########
#import modules
#######

########
#define functions
#######
def entrance():
    print("Welcome it's your first day of school, 1st period History and you need to make it on time to class, make a good first impression!")
    school=input("Where would you like to go? The options are townhall or cafeteria?")
    if school == "townhall":
        townhall()
    elif school == "cafeteria":
        cafeteria()

def townhall():
    print("You are in townhall")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tcafeteria\n\tstay in town hall\n")
    if move.lower() == "cafeteria":
        cafeteria()
    elif move.lower() == "stay in town hall":
        townhall()
    else:
        #TODO: what should happen if they type something else?
        pass

def cafeteria():
    print("You are in the cafeteria")
    choice = input("what do you want for breakfast? say one of these choices:\n\tpancakes\n\twaffles")
    if choice== "pancakes":
        global nautious
        nautious=True
        print("You get a stomacache, You should use the bathroom")
    if choice=="waffles":
        print("The waffles had bacteria, you get a virus, school gets closed down, GAME OVER")
        exit()
    move = input("Say one of these choices:\nbathroom\nhclass")
    if move == "bathroom":
        bathroom()
    elif move == "hclass":
        hclass()


def bathroom():
    global nautious
    nautious= False 
    print("you're in the bathroom and no longer feel nautious ")
    input("press enter to leave and go to history class")
    hclass()

def hclass(): 
    if nautious==True:
        print("congratulations you made it to class in time!, Unfortunately you never went to the bathroom the pancakes got to you and the history teachers face is covered in your vomit!") 
    
    else:
        print("congratulations you made it to class in time!")
      

def room3():
    print("You are in town hall")
    move = input("\nWhere would you like to go? Say one of these choices:\n\troom1\n\troom2\n")
    if move.lower() == "room2":
        room2()
    elif move.lower() == "room1":
        room1()
    else:
        #TODO: what should happen if they type something else?
        pass


########
#main
#######
#TODO: 
nautious=False
breakfast="none"
entrance()