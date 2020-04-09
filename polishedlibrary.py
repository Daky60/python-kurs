import pandas as pd


## file which to write data to, file is created if it doesn't exist
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
            header = input('Do you want to change players, timelapse or age? ').lower()
            if header in ('players', 'timelapse', 'age'):
                value = input(f'New {header}: ')
                self.df.loc[self.df.title == keyword, header] = value
                print(f'{header.title()} changed to {value}')
            else:
                print('invalid input')
        else:
            print(old_title.title(), 'doesnt exist')
    ## searches for a game title
    def search_partial_title(self):
        keyword = input('search for partial or full title: ').lower()
        results = self.df[self.df.title.str.startswith(keyword, na=False)]
        if len(results) > 0:
            print('Following results found:')
            print(results)
        else:
            print('No results found')
    def search_property_from(self):
        header = input('Do you want to search by players, timelapse or age? ').lower()
        if header in ('players', 'timelapse', 'age'):
            try:
                keyword = int(input(f'Game with {header} from: '))
                print(self.df[self.df[header] >= keyword])
            except:
                print('invalid input')
        else:
            print('invalid input')
    ## exports df to file
    def export_df(self):
        self.df.to_csv(self.file, sep=';', encoding='UTF-8', index=False, header=None)


def menu_options():
    print("""Choose alternative by number
1. Add game
2. Change game title
3. Change game properties
4. Search game title
0. Exit
""", end="Input: ")
    try:
        pick = int(input())
        return pick
    except:
        print('Invalid input')




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
        elif pick == 4:
            library.search_partial_title()
        elif pick == 5:
            library.search_property_from()
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()

## create library_file if it doesn't exist
with open(library_file, 'a') as f:
    f.close()

menu_handler(library(library_file))
