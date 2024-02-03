import random


def game():
    num = random.randint(0, 1)
    if num == 1:
        print("--- ОРЕЛ ---")
    elif num == 0:
        print("--- РЕШКА ---")
    else:
        print("--- СТАЛАСЬ ПОМИЛКА ---")


if __name__ == "__main__":
    game()
    while True:
        print("Бажаєте продовжити?\n"
              "1 - Так\n"
              "2 - Ні\n\n")
        ch = int(input("Зробіть свій вибір: "))

        if ch == 1:
            game()
            continue
        elif ch == 2:
            print('---- GAME OVER ----')
            break
        else:
            print("Ви зробили не вірний вибір!")
            continue
