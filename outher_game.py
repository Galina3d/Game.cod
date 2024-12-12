import random

def game():
    # Виведення привітання
    print("Вітаємо в грі 'Врятувати Різдво'!")
    print("Ви — маленький, але спритний різдвяний Ельф, який має врятувати Різдво.")
    # Викликаємо функцію для визначення кількості подарунків
    gifts = get_initial_gifts()
    # Викликаємо функцію для визначення, хто починає гру
    first_player = who_goes_first()
    # Початкова черговість
    current_player = first_player
    is_game_over = False
    # Головний цикл гри
    while gifts > 0 and not is_game_over:
        print(f"Залишилось подарунків: {gifts}")        
        if current_player == 'Ельф':
            gifts_taken = elf_move(gifts)
        else:
            gifts_taken = winter_spirit_move(gifts)
        # Віднімаємо кількість взятих подарунків
        gifts -= gifts_taken
        # Перевірка на магічний подарунок (модель випадкового знаходження магічного подарунка)
        #if random.random() < 0.05:  # 5% шанс знайти магічний подарунок
            #print("Ви знайшли магічний подарунок! Ви забираєте всі залишки подарунків!")
            #gifts = 0  # Всі подарунки переходять до Ельфа, гра закінчується
        # Перевірка на завершення гри
        if gifts == 0:
            if current_player == "Ельф":
                print('Шановний Ельф, у вас є ще один шанс врятувати Різдво, розгадайте головоломку!')
                selection = random.randint(1, 11)
                is_game_over = puzzle(selection)
                P = False
                while not P:
                    n = random.randint(1, 11)
                    P = puzzle(n)
            else:
                print("Злий Дух Зими забрав останній подарунок. Різдво врятовано!")
                is_game_over = True
        # Зміна черговості ходу
        current_player = "Дух Зими" if current_player == "Ельф" else "Ельф"


def get_initial_gifts():
    # Функція для визначення кількості подарунків
    while True:
        try:
            gifts = int(input("Введіть кількість подарунків (від 11 до 30): "))
            if 11 <= gifts <= 30:
                return gifts
            else:
                print("Невірне значення! Введіть число від 11 до 30.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def who_goes_first():
    # Функція для визначення, хто ходитиме першим
    while True:
        first_player = input("Хто почне першим? (Ельф / Дух Зими): ").strip()
        if first_player == "Ельф" or first_player == "Дух Зими":
            return first_player
        else:
            print("Невірне введення. Будь ласка, виберіть 'Ельф' або 'Дух Зими'.")


def elf_move(gifts_left):
    # Хід Ельфа
    while True:
        try:
            move = int(input(f"Скільки подарунків хочеш забрати? (1, 2 або 3): "))
            if 1 <= move <= 3 and move <= gifts_left:
                return move
            else:
                print("Невірне число або занадто багато подарунків.")
        except ValueError:
            print("Будь ласка, введіть число 1, 2 або 3.")


def winter_spirit_move(gifts_left):
    for number in range(1, 4):
        if (gifts_left - number) % 4 == 0 and gifts_left - number >= 0:
            return number
    number = random.randint(1, min(3, gifts_left))
    return number


def puzzle(selection):
    """A function that sets a puzzle for an elf."""
    match selection:
        case 1:
            with open("puzzle1.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 2:
            with open("puzzle2.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 3:
            with open("puzzle3.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 4:
            with open("puzzle4.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 5:
            with open("puzzle5.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 6:
            with open("puzzle6.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 7:
            with open("puzzle7.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 8:
            with open("puzzle8.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 9:
            with open("puzzle9.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 10:
            with open("puzzle10.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()
        case 11:
            with open("puzzle11.txt", "r", encoding="utf-8") as file:
                contents = file.read().splitlines()

    for i in range(len(contents) - 1):
        print(contents[i])
    answer = input("Ваша відповідь:")
    if answer == contents[-1]:
        print("Чудово!!! Правильна відповідь! РІЗДВО ВРЯТОВАНО!!!")
        return True

    print("Нажаль ви не впорались! РІЗДВО ПІД ЗАГРОЗОЮ! Спробуйте наступну головоломку")
    print("****************")
    return False



game()
