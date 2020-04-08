import pandas as pd


library_file = 'out.csv'

searchbase = pd.read_csv(library_file, sep=';', encoding='UTF-8', names=['Title', 'Players', 'Timelapse', 'Age'])

def menu_options():
    print("""Välj mellan alternativen
1. Lägg till spel
2. Ändra titel
3. Ändra spelare
4. Ändra Tid
5. Ändra Ålder
6. Spel från x ålder
0. Avsluta
""", end="Svar: ")
    pick = int(input())
    return pick


def menu_handler(searchbase):
    pick = None
    while pick != 0:
        pick = menu_options()
        ## Add game
        if pick == 1:
            title = input("Title: ")
            if title in searchbase.Title.values:
                print('Title exists')
                break
            try:
                players = int(input("Players: "))
                timelapse = int(input("Timelapse: "))
                age = int(input("Age: "))
                searchbase = searchbase.append([{'Title': title, 'Players': players, 'Timelapse': timelapse, 'Age': age}], ignore_index=True)
            except:
                print('Something went wrong')
                continue
        if pick == 2:
            title = input("Title: ")
            if title in searchbase.Title.values:
                new_title = input("New title: ")
                if new_title in searchbase.Title.values:
                    print('Title exists')
                    break
                searchbase.Title = searchbase.Title.replace(title, new_title)
                print(searchbase)
        if pick == 3:
            title = input("Title: ")
            if title in searchbase.Title.values:
                new_players = int(input("New players: "))
                searchbase.loc[searchbase.Title == title, 'Players'] = new_players
        if pick == 4:
            title = input("Title: ")
            if title in searchbase.Title.values:
                new_timelapse = int(input("New timelapse: "))
                searchbase.loc[searchbase.Title == title, 'Timelapse'] = new_timelapse
        if pick == 5:
            title = input("Title: ")
            if title in searchbase.Title.values:
                new_age = int(input("New age: "))
                searchbase.loc[searchbase.Title == title, 'Age'] = new_age
        if pick == 6:
            entry = int(input("Från ålder: "))
            print(searchbase[searchbase.Age > entry])
    print(searchbase)
    searchbase.to_csv(library_file, sep=';', encoding='UTF-8', index=False, header=None)


menu_handler(searchbase)
