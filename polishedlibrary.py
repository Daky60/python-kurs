import pandas as pd

library_file = 'out.csv'


class library:
    def __init__(self, file):
        self.file = file
        self.df = pd.read_csv(file, sep=';', encoding='UTF-8', names=['title', 'players', 'timelapse', 'age'])
    ## Adds game to df
    def add_game(self):
        title = input('Title: ').lower()
        if title not in self.df.title.values:
            try:
                players, timelapse, age = int(input('Players: ')), int(input('Timelapse: ')), int(input('Age: '))     
                self.df = self.df.append([{'title': title, 'players': players, 'timelapse': timelapse, 'age': age}], ignore_index=True)
                print(title.title(), 'added to library')
            except:
                print('Something went wrong')
        else:
            print(title.title(), 'already exists')
    ## changes title of game in df
    def change_title(self):
        old_title = input("Title: ").lower()
        if old_title in self.df.title.values:
            new_title = input("New title: ").lower()
            if new_title not in self.df.title.values:
                self.df.title = self.df.title.replace(old_title, new_title)
                print(f'Title changed from {old_title} to {new_title}')
            else:
                print(new_title, 'is taken')
        else:
            print(old_title.title(), 'doesnt exist')
    ## changes value of header by searched title
    def set_value(self, header):
        keyword = input('Title: ').lower()
        if keyword in self.df.title.values:
            value = input(f'New {header}: ')
            self.df.loc[self.df.title == keyword, header] = value
            print(f'{header.title()} changed to {value}')
        else:
            print(old_title.title(), 'doesnt exist')
    ## exports df to file
    def export_df(self):
        self.df.to_csv(self.file, sep=';', encoding='UTF-8', index=False, header=None)


def menu_options():
    print("""Choose alternative by number
1. Add game
2. Change game title
3. Change player amount
4. Change timelapse
5. Change age
0. Exit
""", end="Input: ")
    pick = int(input())
    return pick

def menu_handler(library):
    pick = None
    while pick != 0:
        pick = menu_options()
        if pick == 1:
            library.add_game()
        if pick == 2:
            library.change_title()
        if pick == 3:
            library.set_value('players')
        if pick == 4:
            library.set_value('timelapse')
        if pick == 5:
            library.set_value('age')
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()



menu_handler(library(library_file))
