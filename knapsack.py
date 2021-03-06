import random

class knapsack:

    def back(self):
        waga = [5,3,2,4,3]
        wartosc = [3,4,2,6,1]
        pojemnosc = 12
        # print("Podaj dane do plecakow (po spacjach): ")
        # waga = list(map(int, input("Wagi     : ").split()))
        # wartosc = list(map(int, input("Wartosci : ").split()))
        # pojemnosc = int(input("Pojemnosc: "))
        l_kontenerow = len(waga)
        print("Algorytm zachlanny: ")
        self.greedy([waga, wartosc], pojemnosc)
        print("Algorytm dynamiczny 1.: ")
        self.dynamic(pojemnosc, waga, wartosc)
        print("Algorytm dynamiczny 2.: ")
        self.dynamic2(pojemnosc, waga, wartosc)

    def printNice(self, digit, space):
      if digit < 10: print(f"  {digit}{space}", end = "", sep = "")
      elif digit < 100: print(f" {digit}{space}", end = "", sep = "")
      elif digit < 1000: print(f"{digit}{space}", end = "", sep = "")

    def greedy(self, data, backpackmax):
        result = 0
        items = list()

        for i in range(len(data[0])):
            items.append((i, data[0][i], data[1][i], data[1][i]/data[0][i]))

        items = sorted(items, key=lambda a: a[3], reverse = True)
        #for i in dane: print(f"{i}")

        print(f"Element Number Size Value\n")
        for i in range(len(data[0])):
            if items[i][1] <= backpackmax:
                print(f"{i}       {items[i][0]}      {items[i][1]}    {items[i][2]}\n")
                result += items[i][2]
                backpackmax -= items[i][1]
        print("Result: ", result)

    def dynamic(self, W, wt, val):
        n = len(val)
        K = [[0 for w in range(W + 1)]
                for i in range(n + 1)]

        # Build table K[][] in bottom
        # up manner
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1]
                      + K[i - 1][w - wt[i - 1]],
                                   K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        print("    ", end="", sep="")
        for i in range(W + 1): self.printNice(i, " ")
        print()
        for i in range(n + 1):
           for j in range(W + 1):
               if j == 0:
                   self.printNice(i, " ")
               self.printNice(K[i][j], " ")
           print()
        print()
        # stores the result of Knapsack
        res = K[n][W]
        print("Result", res)
        print()
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:

                # This item is included.
                print(f"{wt[i - 1]}[{val[i - 1]}] ", sep="", end="")
                res = res - val[i - 1]
                w = w - wt[i - 1]
        print()

    def dynamic2(self, W, wt, val):
        maxvalue = sum(val)
        n = len(val)
        K = [[0 for w in range(maxvalue + 1)]
                for i in range(n + 1)]

        for i in range(n + 1):
            for w in range(maxvalue + 1):
                if w == 0:
                    K[i][w] = 0
                elif i == 0 and w != 0:# or w == 0:
                    K[i][w] = 100
                elif val[i - 1] <= w:
                    K[i][w] = min(wt[i - 1] + K[i - 1][w - val[i - 1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        print("    ", end="", sep="")
        for i in range(maxvalue + 1): self.printNice(i, " ")
        print()
        for i in range(n + 1):
           for j in range(maxvalue + 1):
               if j == 0:
                   self.printNice(i, " ")
               self.printNice(K[i][j]," ")
           print()
        print()

        res = K[n][W]
        print("Result", res)
        print()
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:
                print(f"{wt[i - 1]}[{val[i - 1]}] ", sep="", end="")
                res = res - val[i - 1]
                w = w - wt[i - 1]
        print()
