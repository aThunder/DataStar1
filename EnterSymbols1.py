
'''Prompts user to input stock symbol(s),
   creates a List of the symbol(s),
   then prints the listing of symbol(s)'''

from tkinter import *
from datetime import datetime

class StkCollectInfo:

    def __init__(self, master):
        self.topFrame = Frame(master) #, width=500, height=200)
        self.topFrame.pack()

        self.enterSymbols = Label(self.topFrame, text='   Enter Stock Symbol(s) (separated by spaces)   ')
        self.entry1 = Entry(self.topFrame)
        self.submitButton = Button(self.topFrame, text ="Submit", command = self.submitSymbols)
        self.quitButton = Button(self.topFrame, text='Quit', command = self.topFrame.quit)

        self.enterSymbols.grid(columnspan=2)
        self.entry1.grid(columnspan=2)
        self.submitButton.grid()
        self.quitButton.grid(row=2,column=1,sticky=W)

    def submitSymbols(self):
        self.symbols = self.entry1.get()
        self.topFrame.quit()
        print('Symbol(s) entered: ', self.symbols)


    def parseList(self):
        self.x = []
        counter = 0
        indivSymbol = ''
        for i in self.symbols:
            counter += 1
            if i != ' ':
                indivSymbol += i
                if counter == len(self.symbols):
                    self.x.append(indivSymbol)
            else:
                self.x.append(indivSymbol)
                indivSymbol = ''

        self.symbolList = [i.upper() for i in self.x]
        print(self.symbolList)
        return self.symbolList

    def printSentence(self):
        if len(self.symbolList) < 1:
            print("You didn't enter any symbol(s))")

        if len(self.symbolList) == 1:
            self.sentence = ''
            print("The symbol you requested: ",self.symbolList[0])
            for i in self.symbolList:
                self.sentence += i
            return self.sentence

        self.sentence = ''
        counter = 1
        for i in self.symbolList:
            if len(self.symbolList) == counter:
                self.sentence += i
            else:
                self.sentence += i
                self.sentence += ', '
                counter += 1
        print('The symbols you requested: ', self.sentence)
        return self.sentence

    print ("Data as of: ",(str(datetime.now())))

def main():
    root = Tk()
    root.wm_attributes('-topmost',1)
    root.geometry("400x150+10+10")
    root.title('STEP 1')

    a = StkCollectInfo(root)
    root.mainloop()
    b = a.parseList()
    c = a.printSentence()
    return b

#Following for isolated testing only. Comment out otherwise
if __name__ == '__main__': main()
