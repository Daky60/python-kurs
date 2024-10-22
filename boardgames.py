

##############################################################################

lib_file = 'out.csv'                                                        ## File to run script against, file is created if it doesn't exist
columns = ['Title', 'Players', 'Duration', 'Age']                           ## Add or remove any column seamlessly, first is assumed to be unique id
testing = True                                                              ## Adds random games for testing purposes

##############################################################################



import pandas as pd
class library:
    def __init__(self, file, columns):
        self.file = file
        self.columns = columns
        self.id = columns[0]
        self.df = pd.read_csv(self.file, sep=';', names=self.columns) #--kommentar om vad df står för vore bra
    ## Adds game  #--överflödig kommentar, då metoden heter add_game
    def add_game(self):
        result = list()
        result.append(input(f'Enter {self.id}: ').title()) 
        ## Check so title doesn't already exist
        if result[0] not in self.df[self.id].values:
            ## Loop through self.columns, ask for input value, creates a seperate df(temp) and merges it to self.df
            try:
                for i in self.columns[1:]:
                    result.append(int(input(f'Enter {i}: '))) #--smidigt!
                temp = pd.DataFrame([result], columns=self.columns)
                self.df = self.df.append(temp, ignore_index=True)
                print(result[0], 'added to library')
            except:
                print('Something went wrong')
        else:
            print(result[0], 'already exists')
    ## Adds a bunch of random games for testing purposes #- här har vi en bättre kommentar. VARFÖR man har något i koden. 
    def add_random_games(self):
        import random #- lägg importer i början av filen. 
        for i in range(100):
            result = list()
            identifier = random.choice('aeiouy').join(random.choice('bcdfghjklmnpqrstvwxz') for i in range(random.randrange(3, 5))).title() #--här vore det bra med en kommentar
            if identifier not in self.df[self.id].values:
                result.append(identifier)
                for i in self.columns[1:]: #-här hade det varit bra med en kommentar
                    result.append(random.randrange(1, 1000)) 
                temp = pd.DataFrame([result], columns=self.columns)
                self.df = self.df.append(temp, ignore_index=True)
    ## Search for a game
    def search_game(self, pool=None):
        ## Needed for filtering search #--what is needed?
        if pool is None:
            pool = self.df
        header = input(f'Do you want to search by {", ".join(self.columns[:-1]).lower()} or {self.columns[-1].lower()}?: ').title() #- här hade det varit bra med en kommentar om VARFÖR det står columns[-1]
        if header in self.columns:
            ## Search by title (unique) #-gör detta till en funktion
            if header == self.id:
                keyword = input(f'Search for partial or full {self.id.lower()}: ').title()
                results = pool[pool[header].str.startswith(keyword, na=False)]
            ## Searches for value from keyword #-gör detta till en funktion
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
    ## changes property of selected game #-edit game properties kanske hade varit ett bättre namn. 
    def change_property(self, edit=None):
        if edit is None:
            identifier = input(f'Enter {self.id}: ').title()
        else:
            identifier = edit
        ## Search for title
        if identifier in self.df[self.id].values: #-den här biten hade jag delat upp och omstrukturerat. 
            header = input(f'Do you want to change {", ".join(self.columns).lower()} or delete game?: ').title()
            ## Check if input matches an existing column
            if header in self.columns:
                value = input(f'New {header}: ')
                ## Change title (unique) #-gör det här till en funktion
                if header == self.id:
                    if value not in self.df[self.id].values:
                        self.df[self.id] = self.df[self.id].replace(identifier, value.title())
                        print(header, 'changed to', value.title())
                    else:
                        print(value, 'is taken')
                ## Change other values
                else:
                    try:
                        self.df.loc[self.df[self.id] == identifier, header] = int(value)
                        print(header, 'changed to', value)
                    except:
                        print('Invalid input')
            ## If input is delete
            elif header == 'Delete':
                self.df = self.df[self.df[self.id] != identifier]
                print(identifier, 'deleted')
            else:
                print('Invalid input')
        else:
            print(identifier, 'doesn\'t exist')
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
            ## Saves search results to results var so you can continue filtering #- förslag om att lägga detta i en separat funktion 
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
            print(library.df.to_string())
        if pick != 0:
            input("Press any key to continue...")
    library.export_df()


## create lib_file if it doesn't exist
with open(lib_file, 'a') as f:
    pass



## Calls menu_handler which in return calls everything else
menu_handler(library(lib_file, columns))

#-Allmänt bra namngivning på funktioner, även om jag gärna hade sett fler funktioner. Strukturen är inte klockren (lite väl många indenteringar vid try/except och if-satser) men god.