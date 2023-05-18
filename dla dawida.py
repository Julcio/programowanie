name = input('Witaj drogi użytkowniku!')
name = input('Teraz zaprezentuje ci możliwości programu Python!')

   #KALKULATOR
print('KALKULATOR')

def dodawanie(x, y):
    return x + y

def roznica(x, y):
    return x - y

def iloczyn(x, y):
    return x * y

def iloraz(x, y):
    return x / y 

def potegowanie(x, y):
    return x ** y

wyjscie = False
while wyjscie == False:
    
    print('Menu')
    print('1 - Dodawanie')
    print('2 - Roznica')
    print('3 - Iloczyn')
    print('4 - Iloraz')
    print('5 - Potęgowanie')
    print('6 - Wyjście')

    choice = input('Wybier (1/2/3/4/5/6):')

    if choice == '6':
        pytanie = input('Czy napewno chesz wyjść z programu? (Tak/Nie): ')
        if pytanie == 'Tak' :
            wyjscie = True
            print('Do Widzenia drogi użytkowniku!')
            break
        elif pytania == 'Nie':
            wyjscie = False
            print('Powrót do programu!')
            choise = input('Wybierz (1/2/3/4/5/6):')

    x = float(input('Podaj pierwszą liczbę od 1 - 10: '))
    y = float(input('Podaj drugą liczbę od 1 - 10: '))

    if choice == '1':
        print(x, '+' ,y, '=', dodawanie(x,y))

    elif choice == '2':
        print(x, '-' ,y, '=', roznica(x,y))

    elif choice == '3':
        print(x, '*' ,y, '=', iloczyn(x,y))

    elif choice == '4':
        print(x, '/' ,y, '=', iloraz(x,y))

    elif choice == '5':
        print(x, '**' ,y, '=', potegowanie(x,y))

    else:
        print('Wybrałeś opcje która nie istnieje, spróbuj ponownie wybrać opcję! ')