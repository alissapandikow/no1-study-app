# ===========================================================
#                    Uppgiftsroulette                   
# ===========================================================   
# Skapat av: Alissa Pandikow - Den kreativa hjärnan bakom detta fantastiska verk (Tidigare student på teknisk matematik - numera uppgiftsrouletteingenjör)
# Datum: 2024-04-10
# Credits:
#   - Random's Choice Awards: För att ha utsett "Uppgiftsroulette" till toppbetyg i kategorin
#     bästa uppgiftshanteringssystem. Tack för beröm och stödet!
# ===========================================================


import random
import sys

def randomiser(lst):
    random_element = random.choice(lst)
    lst.remove(random_element)
    return random_element

def main():
    lst = [1.5, 1.7, 2.11, 3.7, 3.5, 1.1, 1.2, 2.4, 2.10, 3.2, 3.6, 3.8,
           7.2, 7.5, 7.11, 7.15, 7.16, 7.1, 7.3, 7.7, 7.9, 7.13, 7.17,
           8.3, 8.5, 8.6, 8.10, 8.17, 8.33, 8.2, 8.4, 8.8, 8.9, 8.13,
           8.15, 8.35, 8.17, 8.42, 8.46, 8.48, 8.61, 8.64, 8.68, 8.36,
           8.38, 8.43, 8.49, 8.51, 9.18, 9.19, 9.22, 9.24, 9.33, 9.41,
           9.6, 9.8, 9.9, 9.10, 9.12, 9.15, 9.29, 9.30
           ]
    tuple_list = []

    while True:
        inp = input("1. Randomisera 2. Välj svårighetsgrad på uppgift 3. Avsluta\n")
        if inp == '1':
            random_element = randomiser(lst)
            print(random_element)

            difficulty = input("Ange svårighetsgrad: l. Lätt m. Medel s. Svår ")

            tuple_list.append((random_element, difficulty))
        elif inp == '2':
            choice = input("Välj svårighetsgrad: l. Lätt m. Medel s. Svår")
            diff_list = []
            for item in tuple_list:
                if item[1] == choice:
                    diff_list.append(item[0])
            if diff_list:
                elem_diff = randomiser(diff_list)
                print(elem_diff)
            else:
                print("Inga uppgifter med den valda svårighetsgraden.")
        elif inp == '3':
            sys.exit()
        else:
            print("Ange giltig input")

main()
