from knapsack import knapsack
def main():
    kn = knapsack()
    while (True):
        print("Witamy w menu!!")
        print(" 0 - Wyjscie\n 1 - plecakowy\n 2 - MST\n 3 - CPM\n 4 - Przepływ w sieciach\n 5 - poroblem szeregowania\n 6 - kolorowanie (algorytm Browna)")
        print("Wybierz program: ", sep="", end="")
        program = int(input())
        if program == 0:
            print("Pa, pa!!")
            break
        if program == 1:
            kn.back()
        if program == 2:
            print("Program w budowie...")
        if program == 3:
            print("Program w budowie...")
        if program == 4:
            print("Program w budowie...")
        if program == 5:
            print("Program w budowie...")
        if program == 6:
            print("Program w budowie...")
        print()


main()
