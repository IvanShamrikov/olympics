import random
WORDLIST = 'лелека акула бабуїн баран'.split(" ")
ALPHABET = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя"

def get_pics():
    a = r'''
    +---+
    |   
    |   
    |   
    ===
    '''

    b = r'''
    +---+
    |   0
    |   
    |   
    ===
    '''

    c = r'''
    +---+
    |   0
    |   |
    |   
    ===
    '''

    d = r'''
    +---+
    |   0
    |  /|
    |   
    ===
    '''

    e = r'''
    +---+
    |   0
    |  /|\
    |   
    ===
    '''

    f = r'''
    +---+
    |   0
    |  /|\
    |  / 
    ===
    '''

    g = r'''
    +---+
    |   0
    |  /|\
    |  / \
    ===
    '''

    lst = [a, b, c, d, e, f, g]
    return lst

def tablo(pic, mis, cor, word):
    print(mis)
    print(cor)

    print( pic[len(mis)] )
    print("Помилкові літери - ", mis)
    print("Правильні літери - ", end=" ")

    for letter in word:
        if letter in cor:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def user_input(mis, cor, alf):
    while True:
        u_inp = input("Введи букву укр. абетки - ")
        if len(u_inp) == 0:
            print("Ви нічого не ввели")
            continue
        elif len(u_inp) > 1:
            print("Введіть ОДНУ букву")
            continue
        elif u_inp not in alf:
            print("Введіть літеру!!!!")
            continue
        elif u_inp in cor or u_inp in mis:
            print("Ви таку літеру вже називали!!!!")
            continue
        else:
            return u_inp

# def analis(guess, word, correct_letters, missed_letters, pictires):
#     if guess in word:  # Якщо вгадав
#         correct_letters += guess
#         # Чи вгадав всі букви?
#         for letter in word:
#             if not letter in correct_letters:
#                 return None, correct_letters, missed_letters
#         return f"ВИ ВГАДАЛИ СЛОВО {word}!", correct_letters, missed_letters
#
#     else:  # Якщо не вгадав
#         missed_letters += guess
#         # Чи закінчились спроби?
#         if len(missed_letters) != len(pictires):
#             return None, correct_letters, missed_letters
#         return f"ЗАКІНЧИЛИСЬ СПРОБИ! ВИ НЕ ВГАДАЛИ СЛОВО {word}!", correct_letters, missed_letters

def endGameCheck():
    while True:
        u_inp = input("Чи хочете Ви зіграти ще раз? (Так/Ні) - ").lower()
        if u_inp not in ["т", "так", "н", "ні"]:
            print("Будьте уважні з відповідями.")
            continue
        elif u_inp in ["т", "так"]:
            return True
        elif u_inp in ["н", "ні"]:
            return False

def analisys(guess, word, cor_l, mis_l, pic):
    game_continue = True
    winner = None

    # Якшо гравець вгадав
    if guess in word:
        cor_l += guess
        # Гравець вгадав всі літери?
        for letter in word:
            if letter not in cor_l:
                game_continue = True
                winner = None
                return cor_l, mis_l, game_continue, winner

        game_continue = False
        winner = "player"
        return cor_l, mis_l, game_continue, winner

    # Якшо гравець не вгадав
    else:
        mis_l += guess
        # Чи закінчились спроби?
        if len(mis_l) != len(pic):
            game_continue = True
            winner = None
            return cor_l, mis_l, game_continue, winner
        else:
            game_continue = False
            winner = "computer"
            return cor_l, mis_l, game_continue, winner


def checkAnotherGame():
    while True:
        print("Чи хочете Ви зіграти ще раз? (Так/Ні)")
        u_inp = input().lower()
        if u_inp.startswith("т"):
            return True
        elif u_inp.startswith("н"):
            return False
        else:
            print("Ви ввели якусь фігню")


def game(wlist, albt):

    # задаємо змінні
    correct_letters = ''
    missed_letters = ''
    pictires = get_pics()
    game_continue = True
    winner = None

    word = random.choice(wlist)

    while True:
        # Виводимо табло шибениці
        tablo(pictires, missed_letters, correct_letters, word)

        # Гравець вказує літеру
        guess = user_input(missed_letters, correct_letters, albt)

        #Аналітика здогадки
        correct_letters, missed_letters, game_continue, winner = analisys(guess, word, correct_letters, missed_letters, pictires)

        if game_continue == True:
            continue
        else:
            if winner == "player":
                print(f"ВИ ВГАДАЛИ СЛОВО {word}!")
            else:
                print(f"ЗАКІНЧИЛИСЬ СПРОБИ! ВИ НЕ ВГАДАЛИ СЛОВО {word}!")

        if checkAnotherGame():
            game(wlist, albt)
        else:
            break


print("ШИБЕНИЦЯ")
game(WORDLIST, ALPHABET)
print("ДЯКУЄМО ЗА ГРУ")