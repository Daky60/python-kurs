

##############################################################################

lib_file = 'out.csv'                                            ## File to run script against, file is created if it doesn't exist
columns = ['Title', 'Players', 'Duration', 'Age']               ## Add or remove any column seamlessly, first is assumed to be unique id
testing = True                                                  ## Adds random games for testing purposes

##############################################################################



import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
class library:
    def __init__(self, file, columns):
        self.file = file
        self.columns = columns
        self.df = pd.read_csv(self.file, sep=';', names=self.columns)
    ## Adds game
    def add_game(self):
        result = list()
        result.append(input(f'Enter {self.columns[0]}: ').title())
        ## Check so title doesn't already exist
        if result[0] not in self.df[self.columns[0]].values:
            ## Loop through self.columns, ask for input value, creates a seperate df(temp) and merges it to self.df
            try:
                for i in self.columns[1:]:
                    result.append(int(input(f'Enter {i}: ')))
                temp = pd.DataFrame([result], columns=self.columns)
                self.df = self.df.append(temp, ignore_index=True)
                print(result[0].title(), 'added to library')
            except:
                print('Something went wrong')
        else:
            print(result[0].title(), 'already exists')
    ## Adds a bunch of random games for testing purposes
    def add_random_games(self):
        import random
        alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'
        for i in range(100):
            result = list()
            identifier = ''.join(random.choice(alphabet) for i in range(random.randrange(5, 15))).title()
            if identifier not in self.df[self.columns[0]].values:
                result.append(identifier)
                for i in self.columns[1:]:
                    result.append(random.randrange(1, 1000))
                temp = pd.DataFrame([result], columns=self.columns)
                self.df = self.df.append(temp, ignore_index=True)
    ## Search for a game
    def search_game(self, pool=None):
        ## Needed for filtering search
        if pool is None:
            pool = self.df
        header = input(f'Do you want to search by {", ".join(self.columns[:-1]).lower()} or {self.columns[-1].lower()}?: ').title()
        if header in self.columns:
            ## Search for title (unique)
            if header == self.columns[0]:
                keyword = input(f'Search for partial or full {self.columns[0].lower()}: ').title()
                results = pool[pool[header].str.startswith(keyword, na=False)]
            ## Searches for value from keyword
            else:
                try:
                    keyword = int(input(f'Game with {header} from: '))
                    results = pool[pool[header] >= keyword]
                except:
                    print('Invalid input')
            ## Return search results if 1 or more
            if len(results) > 0:
                results = results.sort_values(by=header)
                print(results)
                return results
            else:
                print('No results found')
        else:
            print('Invalid input')
    ## changes property of selected game
    def change_property(self, edit=None):
        if edit is None:
            identifier = input(f'Enter {self.columns[0].title()}: ').title()
        else:
            identifier = edit
        ## Search for title
        if identifier in self.df[self.columns[0]].values:
            header = input(f'Do you want to change {", ".join(self.columns).lower()} or delete game?: ').title()
            ## Check if input matches an existing column
            if header in self.columns:
                value = input(f'New {header}: ')
                ## Change title (unique)
                if header == self.columns[0]:
                    if value not in self.df[self.columns[0]].values:
                        self.df[self.columns[0]] = self.df[self.columns[0]].replace(identifier, value.title())
                        print(f'{header.title()} changed to {value.title()}')
                    else:
                        print(value, 'is taken')
                ## Change other values
                else:
                    try:
                        self.df.loc[self.df[self.columns[0]] == identifier, header] = int(value)
                        print(f'{header.title()} changed to {value}')
                    except:
                        print('invalid input')
            ## If input is delete
            elif header == 'Delete':
                self.df = self.df[self.df[self.columns[0]] != identifier]
                print(identifier, 'deleted')
            else:
                print('invalid input')
        else:
            print(identifier.title(), 'doesnt exist')
    ## exports df to file
    def export_df(self):
        self.df.to_csv(self.file, sep=';', index=False, header=None)


## The options for the menu
def menu_options():
    print(
        'Choose alternative by number\n'
        '1. Add game\n'
        '2. Edit game\n'
        '3. Find game\n'
        '4. Display all games\n'
        '0. Exit'
    )
    ## Returns input for method calls
    try:
        pick = int(input('Enter: '))
        return pick
    except:
        print('Invalid input')



## Function that puts it all together
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
            ## Saves search results to results var so you can continue filtering
            try:
                results = library.search_game()
                while (len(results) > 1 and input('Press 1 to continue search or 0 to exit: ') != str(0)):
                    results = library.search_game(results)
                    ## If only 1 result, give choice to edit game
                if len(results) == 1 and input('Press 1 to edit game or 0 to exit: ') != str(0):
                    selected = results.iloc[0][library.columns[0]]
                    library.change_property(selected)
            except:
                pass
        elif pick == 4:
            print(library.df)
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()

## create lib_file if it doesn't exist
with open(lib_file, 'a') as f:
    pass



## Calls menu_handler which in return calls everything else
menu_handler(library(lib_file, columns))
