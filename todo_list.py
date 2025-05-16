class TodoList:
    def menu(self):
        print("Welcome to your first step of making your life much more better by making a to do list ^^.")
        print('So what do you want to do today?')
        print('1. Create a to do list')
        print('2. Add more things to do in your list')
        print('3. Browse your to do list')
        print('4. Delete your to do list')
        print('5. Exit')
        
    def menu2(self):
        print('Alright, here are your options')
        print('1. Create a to do list')
        print('2. Add more things to do in your list')
        print('3. Browse your to do list')
        print('4. Delete your to do list')
        print('5. Exit')
        
    def lst_name(self):
        name = input(f"Let's choose a cute name for your list: ")
        self.name = name 
        print(f'Alrighty, so your list name will be "{name}.txt"')
        create = open(f'{name}.txt','w')
        create.close()
        
    def add(self):
        search = input('so what file do you want to add? ')
        print('Uki dooki, what do you want to add? Press stop to stop')
        details = []
        while True:
            thing = input()
            if thing.lower() == 'stop':
                break
            else:
                details.append(thing)
        with open(f'{search}.txt','a') as file:
            for i, detail in enumerate(details):
                file.write(f'{i+1}. {detail}\n')
                    
    def browse(self):
        search = input('What file do you want to check? ')
        print('Alright, here is your to do list, remember to do all of them okay.')
        with open(f'{search}.txt','r') as things:
            print(things.read())
    
    def destroy(self):
        search = input('What file do you want to erase? ')
        print('Are you sure you want to erase your list? have you done everything in your list yet?')
        while True:
            ask = input('Press Y to continue and N to go back: ')
            if ask.lower() == 'n':
                break
            elif ask.lower() == 'y':
                with open(f'{search}.txt','w') as delete:
                    delete.write()
                    break
            else:
                print('Ohhhhhh, so sorry but your input is invalid')
                
    def option(self):
        while True:
            try:
                user = int(input('So your choice is: '))
                if user in range(1,6):
                    break
                else:
                    print("Well... Let's try again because you can only choose from 1-5")
            except ValueError:
                print("Okay, don't make this difficult for both of us, your choice is only a number okay, not any strange words or symbols")
        if user == 1:
            self.lst_name()
        elif user == 2:
            self.add()
        elif user == 3:
            self.browse()
        elif user == 4:
            self.destroy()
        else:
            print("Ukiiii, see you next time my friend and thank you for using me")
            return False
    
    def display(self):
        self.menu()
        self.option()
        while True:
            print("Alright, let's go back, shall we?")
            using = input('(Y/N): ')
            if using.lower() == 'y':
                self.menu2()
                self.option()
            elif using.lower() == 'n':
                print('Alright, thank you for using me, have a good day my friend.')
                break
            else:
                print("*sigh* the instruction is clear, only Y or N, what are you doing? Let's try it again.")
        
            
todolst = TodoList()
todolst.display()