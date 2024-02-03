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
    # game()
    num = 0
    while True:
        num += 1
        print(f"SPAM -- {num}")
