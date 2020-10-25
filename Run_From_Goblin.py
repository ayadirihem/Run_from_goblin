def principal():
    print(
        "One day, you open your eyes in a ruined palace srounded with gold.\n so you start hide some of it in your clothes.\n Suddenly you heard a voice behind you !!\n"
        "it was the goblin. \n You will ")
    print(" A- Run \n B-throw some gold on him ")
    choice = input(">>")
    if choice == 'A' or choice == 'a':
        Run()
    else:
        fight()


def Run():
    print('Run as quickly as possible, but the goblin\'s speed is too great.\n you will:')
    print('A- hide inside an empty room \nB-you trapped, so you fight \nC-you jump from the window')
    choice = input(">>")
    if choice == 'A' or choice == 'a':
        print("it was the grim reaper's room ."
              "\n he hate visitors"
              '\n you died')
    elif choice == 'B' or choice == 'b':
        print("\nYou're no match for a goblin. "
              "\n\nYou died!")
    elif choice == 'C' or choice == 'c':
        print(" You quickly jumped from the window to fall in the river, somehow "
              "hoping it will stop the goblin. It does! The goblin was afraid "
              "for water. "
              "\n\nThis got weird, but you survived! ")


def fight():
    print("\nThe goblin is stunned, but regains control. He begins "
          "\nrunning towards you again. You were hesitant"
          " \nBefore you fully enter, you notice a shiny sword on "
          "the ground. \nDo you pick up a sword. Y/N?")
    answer = input('>> ')
    yes = ['Y', 'y', 'Yes', 'yes']
    if answer in yes:
        sword = 1
    else:
        sword = 0
    print(" \n A- run to the door of the palace and try to open it"
          "\n B- try to kill the goblin with the sword"
          "\n C- hide in silent ")
    choice = input('>> ')
    if choice == 'A' or choice == 'a':
        print("the door was closed from the outside. You are trapped. \n\nYou died!")
    elif choice == 'B' or choice == 'b':
        if sword > 0:
            print("\nYou laid in wait. The shimmering sword attracted "
                  "\nthe goblin, which thought you were no match. As he walked "
                  "\ncloser and closer, your heart beat rapidly. As the goblin "
                  "\nreached out to grab the sword, you pierced the blade into "
                  "\nits chest. \n\nYou survived!")
        else:
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice == 'C' or choice == 'c':
        print("\nYou decided to throw another rock, as if the first "
              "\nrock thrown did much damage. The rock flew well over the "
              "\ngoblin head. You missed. \n\nYou died!")


principal()
