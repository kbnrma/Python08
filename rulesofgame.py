
import random
from decouple import config

def play_game():
    my_money = int(config("MY_MONEY"))
    nums = list(range(1, 31))

    while True:
        print(f"Ваши деньги: {my_money}")
        bet = int(input("Поставьте деньги: "))
        if bet > my_money:
            print(f"Извините у вас не хватает средств на ставку. Попробуйте еще раз\n")
            continue

        win_number = random.choice(nums)
        select_number = int(input("Выбирайте номера с 1 по 30: "))

        if select_number > 30:
            print(f"Других цифр не надо. Заново давай\n")
            continue

        elif bet > my_money:
            print("Извините у вас не хватает средств. Попробуйте еще раз")
            continue

        elif select_number == win_number:
            my_money += bet * 2
            print(f"Вы выиграли!")
        else:
            my_money -= bet
            print(f"Вы проиграли. У вас осталось {my_money}")

        


        def play_again(self):
            while True:
                choice = input("Хотите сыграть еще? (Да/Нет): ").lower()
                if choice == "да":
                    return True
                elif choice == "нет":
                    return False
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")

play_game()