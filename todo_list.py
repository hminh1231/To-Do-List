class TodoList:
    def menu(self):
        '''This function will display the menu'''
        print("Welcome to your first step of making your life much more better by making a to do list ^^.")
        print('So what do you want to do today?')
        print('1. Create a to do list')
        print('2. Browse all your lists name')
        print('3. Add more things to do in your list')
        print('4. Browse your to do list')
        print('5. Delete your to do list')
        print('6. Exit')
        
    def menu2(self):
        '''This function will display the menu again''' #Sorry, because I want it to looks cute so I have to create another menu with funny respond when user keep using
        print('Alright, here are your options')
        print('1. Create a to do list')
        print('2. Browse all your lists name')
        print('3. Add more things to do in your list')
        print('4. Browse your to do list')
        print('5. Delete your to do list')
        print('6. Exit')
        
    def lst_name(self):
        '''This function will create a file name to do list with the name given by user'''
        name = input(f"Let's choose a cute name for your list: ")
        self.name = name 
        file_names = []
        file_names.append(name)
        with open('files_name.txt','a') as file_name:
            for i in file_names:
                file_name.write(i + '\n')
        print(f'Alrighty, so your list name will be "{name}.txt"')
        create = open(f'{name}.txt','w')
        create.close()
        
    def browse_file(self):
        '''this function will let user browse all the files he/she created so far'''
        with open('files_name.txt','r') as browse_files:
            browse = browse_files.readlines()
            if len(browse) == 0:
                print("You don't have any files yet")
            else:
                for i, fname in enumerate(browse, start=1):
                    print(f"{i}. {fname.strip()}")
        
    def add(self):
        '''This function will add things to the list in the file'''
        search = input('so what file do you want to add? ')
        print('Uki dooki, what do you want to add? Press stop to stop')
        details = []
        while True:
            thing = input()
            if thing.lower() == 'stop':
                break
            else:
                details.append(thing)
        with open(f'{search}.txt','r') as lines:
            count = lines.readlines()
            last_num = len(count)
        with open(f'{search}.txt','a') as file:
            for i, detail in enumerate(details,start=last_num):
                file.write(f'{i+1}. {detail}\n')
                    
    def browse(self):
        '''This function allows the user to see their to do list'''
        search = input('What file do you want to check? ')
        print('Alright, here is your to do list, remember to do all of them okay.')
        with open(f'{search}.txt','r') as things:
            print(things.read())
    
    def destroy(self):
        '''This function will erase the to do list'''
        search = input('What file do you want to erase? ')
        print('Are you sure you want to erase your list? have you done everything in your list yet?')
        while True:
            ask = input('Press Y to continue and N to go back: ')
            if ask.lower() == 'n':
                break
            elif ask.lower() == 'y':
                with open(f'{search}.txt','w') as delete:
                    delete.write('')
                    break
            else:
                print('Ohhhhhh, so sorry but your input is invalid')
                
    def options(self):
        '''This function will get user choice input and process it'''
        while True:
            try:
                user = int(input('What is your choice numer: '))
                if user in range(1,7):
                    break
                else:
                    print('You must choose option from 1-6')
            except ValueError:
                print("It's okay, I know that sometime human can misread too, it's a normal thing that you can't read the part 'What is your choice NUMBER'. Now, let's try again okay. ")
        return user
        
    def keep_going(self):
        '''This function will decide if the user want to continue or not'''
        choice = True
        while choice:
            working = input('Do you want to continue?(Y/N): ')
            if working.lower() == 'y':
                choice = False
                return True
            elif working.lower() == 'n':
                print('Thank you for using me')
                choice = False
                return False
            else:
                print('Your choice is invalid, please try again')
    
    def display(self):
        '''This function will display everything'''
        self.menu()
        while True:
            option = self.options()
            if option == 1:
                self.lst_name()
                if not self.keep_going():
                    break
                else:
                    self.menu2()
            elif option == 2:
                self.browse_file()
                if not self.keep_going():
                    break
                else:
                    self.menu2()
            elif option == 3:
                self.add()
                if not self.keep_going():
                    break
                else:
                    self.menu2()
            elif option == 4:
                self.browse()
                if not self.keep_going():
                    break
                else:
                    self.menu2()
            elif option == 5:
                self.destroy()
                if not self.keep_going():
                    break
                else:
                    self.menu2()
            else:
                print('Thank you for using my service')
                break

        
            
todolst = TodoList()
todolst.display()
