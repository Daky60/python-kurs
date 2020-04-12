import pandas as pd

## file which to write data to, file is created if it doesn't exist
library_file = 'out.csv'
testing = True


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class library:
    def __init__(self, file):
        self.file = file
        self.columns = ['title', 'players', 'duration', 'age']
        self.df = pd.read_csv(self.file, sep=';', encoding='UTF-8', names=self.columns)
    ## Adds game to df
    def add_game(self):
        title = input('Title: ').lower()
        if title not in self.df.title.values:
            try:
                players, duration, age = int(input('Players: ')), int(input('Duration: ')), int(input('Age: '))
                self.df = self.df.append([{'title': title, 'players': players, 'duration': duration, 'age': age}], ignore_index=True)
                print(title.title(), 'added to library')
            except:
                print('Something went wrong')
        else:
            print(title.title(), 'already exists')
    ## Search for a game
    def search_game(self, pool=None):
        if pool is None:
            pool = self.df
        header = input(f'Do you want to search by {", ".join(self.columns)}?: ').lower()
        if header in self.columns:
            if header == 'title':
                keyword = input('search for partial or full title: ').lower()
                results = pool[pool.title.str.startswith(keyword, na=False)]
            else:
                try:
                    keyword = int(input(f'Game with {header} from: '))
                    results = pool[pool[header] >= keyword]
                except:
                    print('Invalid input')
            if len(results) > 0:
                print(results)
                return results
            else:
                print('No results found')
    ## changes property of selected game
    def change_property(self):
        keyword = input('Title: ').lower()
        if keyword in self.df.title.values:
            header = input(f'Do you want to change {", ".join(self.columns)}?: ').lower()
            if header in self.columns:
                value = input(f'New {header}: ')
                if header == 'title':
                    if value not in self.df.title.values:
                        self.df.title = self.df.title.replace(keyword, value)
                    else:
                        print(value, 'is taken')
                else:
                    try:
                        self.df.loc[self.df.title == keyword, header] = int(value)
                        print(f'{header.title()} changed to {value}')
                    except:
                        print('invalid input')
            else:
                print('invalid input')
        else:
            print(keyword.title(), 'doesnt exist')
    def add_random_games(self):
        import random
        import string
        alphabet = string.ascii_lowercase
        for i in range(random.randrange(30, 100)):
            title = ''.join(random.choice(alphabet) for i in range(random.randrange(5, 12)))
            players, duration, age = random.randrange(1, 12), random.randrange(20, 1440), random.randrange(18)
            if title not in self.df.title.values:
                self.df = self.df.append([{'title': title, 'players': players, 'duration': duration, 'age': age}], ignore_index=True)
    ## exports df to file
    def export_df(self):
        self.df.to_csv(self.file, sep=';', encoding='UTF-8', index=False, header=None)


def menu_options():
    print("""Choose alternative by number
1. Add game
2. Edit game
3. Find game
9. Display all games
0. Exit
""", end="Input: ")
    try:
        pick = int(input())
        return pick
    except:
        print('Invalid input')



def menu_handler(library):
    if testing:
        library.add_random_games()
    pick = None
    while pick != 0:
        pick = menu_options()
        if pick == 1:
            library.add_game()
        elif pick == 2:
            library.change_property()
        elif pick == 3:
            results = library.search_game()
            while (len(results) > 1 and input('Press 0 to exit or 1 to continue searching: ') != str(0)):
                results = library.search_game(results)
        elif pick == 9:
            print(library.df)
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()

## create library_file if it doesn't exist
with open(library_file, 'a') as f:
    pass

menu_handler(library(library_file))