
class Jolyne():
    def __init__(self,Sigma, WfNforWhile,ReverseSigma, InputWord_T):
        self.Sigma = Sigma
        self.WfNforWhile = WfNforWhile
        self.ReverseSigma = ReverseSigma
        self.InputWord_T = InputWord_T
        self.AlphabetStrength = len(self.Sigma)

    def FromNtoW(self):
        r = 1000
        print(" ")
        print("The number of the word: ",self.WfNforWhile )
        self.CNTOENG = []
        while (self.WfNforWhile > 0):
            r = self.WfNforWhile % self.AlphabetStrength
            print('Остаток от деления ', self.WfNforWhile, ' на ', self.AlphabetStrength, ' = ', r)
            if (r != 0):
                self.WfNforWhile = self.WfNforWhile // self.AlphabetStrength
                print(self.WfNforWhile, '/', self.AlphabetStrength)
            else:
                WfNforWhile_last = self.WfNforWhile
                self.WfNforWhile = (self.WfNforWhile // self.AlphabetStrength) - 1
                r = WfNforWhile_last - (self.WfNforWhile * self.AlphabetStrength)
                print("Вычисление остатка: ",WfNforWhile_last,'- ((',WfNforWhile_last,'/',self.AlphabetStrength,' - 1) * ',self.AlphabetStrength,') = ', r)
            self.CNTOENG.append(r)

        self.CNTOENG.reverse()
        WhatWord = []
        for i in self.CNTOENG:
            WhatWord.append(self.Sigma[i])
        print('КОДИРОВКА СЛОВА: ',self.CNTOENG)
        print('ПОЛУЧЕННОЕ СЛОВО: ', ''.join(WhatWord))
        print(' ')

    def FromWtoN(self):
        print(" ")
        print("ВВЕДЕННОЕ СЛОВО: ", self.InputWord_T)
        self.InputWord_Code = []
        for i in self.InputWord_T:
            self.InputWord_Code.append(self.ReverseSigma[i])
        print('КОД НАПИСАННОГО СЛОВА: ',self.InputWord_Code)

        k = len(self.InputWord_Code) - 1
        self.Number = 0
        for i in range(len(self.InputWord_Code)):
            self.Number += ((self.AlphabetStrength)**k) * self.InputWord_Code[i]
            print(self.AlphabetStrength,'^',k,' * ', self.InputWord_Code[i],' + ')
            k -= 1
        print(" = ")
        print("НОМЕР НАПИСАННОГО СЛОВА: ",self.Number)


if __name__ == '__main__':
    # Entering  an input alphabet and the number of a word
    Input_Alphabet = list((input("Enter an alphabet as a string: ")))
    WfNforWhile_0 = int(input("Enter the number of a word: "))

    # Creating dictionaries for the input alphabet
    Sigmus = dict(zip([i for i in range(1,len(Input_Alphabet)+1)], Input_Alphabet))
    SigmusReverse = dict(zip(Sigmus.values(),Sigmus.keys()))

    # Creating English and Russian dictionaries
    SigmaEng = {1: "a", 2: "b", 3: "c", 4:"d"}
    SigmaRus = {1: "а", 2: "б", 3: "в", 4: "г"}
    SigmaEngReverse = dict(zip(SigmaEng.values(),SigmaEng.keys()))
    SigmaRusReverse = dict(zip(SigmaRus.values(),SigmaRus.keys()))

    InputWord = list(input("Enter a word: "))
    variants = int(input("Choose an alphabet:\n 1 - Input alphabet\n 2 - Rus\n 3 - Eng\n"))

    # Creating sets to check the input
    set_input_word = set(InputWord)
    set_input_alphabet = set(Input_Alphabet)
    set_eng_symbols = set(SigmaEng.values())
    set_rus_symbols = set(SigmaRus.values())

    if(variants == 1):
        if set_input_word.issubset(set_input_alphabet):
            Eng = Jolyne(Sigmus, WfNforWhile_0, SigmusReverse, InputWord)
            Eng.FromNtoW()
            Eng.FromWtoN()
        else:
            print("There are no such symbols in the alphabet")
    elif (variants == 2):
        if set_input_word.issubset(set_rus_symbols):
            Eng = Jolyne(SigmaRus, WfNforWhile_0, SigmaRusReverse, InputWord)
            Eng.FromNtoW()
            Eng.FromWtoN()
        else:
            print("There are no such symbols in the alphabet")
    elif (variants == 3):
        if set_input_word.issubset(set_eng_symbols):
            Eng = Jolyne(SigmaEng, WfNforWhile_0,SigmaEngReverse, InputWord)
            Eng.FromNtoW()
            Eng.FromWtoN()
        else:
            print("There are no such symbols in the alphabet")