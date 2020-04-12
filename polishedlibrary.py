import pandas as pd

## file which to write data to, file is created if it doesn't exist
library_file = 'out.csv'
testing = True


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class library:
    def __init__(self, file):
        self.file = file
        self.columns = ['name', 'players', 'duration', 'age']
        self.df = pd.read_csv(self.file, sep=';', encoding='UTF-8', names=self.columns)
    ## Adds game to df
    def add_game(self):
        identifier = input(f'Enter {self.columns[0].title()}: ').lower()
        print(identifier)
        if identifier not in self.df[self.columns[0]].values:
            try:
                one = int(input(f'Enter {self.columns[1].title()}: '))
                two = int(input(f'Enter {self.columns[2].title()}: '))
                three = int(input(f'Enter {self.columns[3].title()}: '))
                self.df = self.df.append([{self.columns[0]: identifier, self.columns[1]: one, self.columns[2]: two, self.columns[3]: three}], ignore_index=True)
                print(identifier.title(), 'added to library')
            except:
                print('Something went wrong')
        else:
            print(identifier.title(), 'already exists')
    ## Search for a game
    def search_game(self, pool=None):
        if pool is None:
            pool = self.df
        header = input(f'Do you want to search by {", ".join(self.columns[:-1])} or {self.columns[-1]}?: ').lower()
        if header in self.columns:
            if header == self.columns[0]:
                keyword = input(f'search for partial or full {self.columns[0]}: ').lower()
                results = pool[pool[header].str.startswith(keyword, na=False)]
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
        else:
            print('Invalid input')
    ## changes property of selected game
    def change_property(self):
        identifier = input(f'Enter {self.columns[0].title()}: ').lower()
        if identifier in self.df[self.columns[0]].values:
            header = input(f'Do you want to change {", ".join(self.columns[:-1])} or {self.columns[-1]}?: ').lower()
            if header in self.columns:
                value = input(f'New {header}: ').lower()
                if header == self.columns[0]:
                    if value not in self.df[self.columns[0]].values:
                        self.df[self.columns[0]] = self.df[self.columns[0]].replace(identifier, value)
                        print(f'{header.title()} changed to {value}')
                    else:
                        print(value, 'is taken')
                else:
                    try:
                        self.df.loc[self.df[self.columns[0]] == identifier, header] = int(value)
                        print(f'{header.title()} changed to {value}')
                    except:
                        print('invalid input')
            else:
                print('invalid input')
        else:
            print(identifier.title(), 'doesnt exist')
    def add_random_games(self):
        import random
        alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
        for i in range(random.randrange(30, 100)):
            identifier = ''.join(random.choice(alphabet) for i in range(random.randrange(5, 12)))
            one, two, three = random.randrange(1, 12), random.randrange(20, 1440), random.randrange(18)
            if identifier not in self.df[self.columns[0]].values:
                self.df = self.df.append([{self.columns[0]: identifier, self.columns[1]: one, self.columns[2]: two, self.columns[3]: three}], ignore_index=True)
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
    pick_sub = None
    while pick != 0:
        pick = menu_options()
        if pick == 1:
            library.add_game()
        elif pick == 2:
            library.change_property()
        elif pick == 3:
            try:
                pick_sub = True
                results = library.search_game()
                while (len(results) > 1 and input('Press 0 to exit or 1 to continue searching: ') != str(0)):
                    results = library.search_game(results)
            except:
                pass
            pick_sub = None
        elif pick == 9:
            print(library.df)
        if pick != 0 and not pick_sub:
            input("Press any key to continue...")
        pick_sub = None
    library.export_df()

## create library_file if it doesn't exist
with open(library_file, 'a') as f:
    pass

menu_handler(library(library_file))