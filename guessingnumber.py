import random
def play_game():
    lucky_num=random.randint(1,50)
    attempts=5
    while attempts>0:
        user_num=int(input("Guess the number: "))
        attempts -=1
        if user_num==lucky_num:
            print("You win, Game is over !!..")
            break

        elif user_num<lucky_num:
            print("Too low,")
        else:
            print("Too high.")


play_game()
print("Thank you for playing.")
