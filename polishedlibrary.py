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
    ## changes a games' property of choice
    def change_property(self):
        keyword = input('Title: ').lower()
        if keyword in self.df.title.values:
            header = input('Do you want to change players, timelapse or age? ')
            if header in ('players', 'timelapse', 'age'):
                value = input(f'New {header.title()}: ')
                self.df.loc[self.df.title == keyword, header] = value
                print(f'{header.title()} changed to {value}')
            else:
                print('invalid input')
        else:
            print(old_title.title(), 'doesnt exist')
    ## exports df to file
    def export_df(self):
        self.df.to_csv(self.file, sep=';', encoding='UTF-8', index=False, header=None)


def menu_options():
    print("""Choose alternative by number
1. Add game
2. Change game title
3. Change game properties
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
        elif pick == 2:
            library.change_title()
        elif pick == 3:
            library.change_property()
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()



menu_handler(library(library_file))
