
'''Prompts user to specify whether to use an existing CSV
   or create a new CSV for the specified symbol(s)
   & returns answer to Controller'''

from tkinter import *

class ExistOrNew:

    def __init__(self, master,symbolList): #,sentence):
        self.master = master
        self.Frame = Frame(master, width=500, height=200)
        self.symbolList = symbolList
        # self.sentence= sentence
        self.choice = 'x'
        self.Frame.pack()

    def requestFileOrigin(self):
        self.sentenceLabel = Label(self.Frame, text="Symbols requested: {0}".format(self.symbolList))
        self.chooseFileType = Label(self.Frame, text="Use Existing File or Create New File?")

        self.existingButton = Button(self.Frame, text='Existing', command = lambda: fileChoice(0))

        self.newButton = Button(self.Frame, text='New', command = lambda: fileChoice(1))

        self.quitButton = Button(self.Frame, text='Quit', command = self.Frame.quit)

        self.sentenceLabel.grid(columnspan=3)
        self.chooseFileType.grid(columnspan=3)
        self.existingButton.grid(row=3)
        self.newButton.grid(row=3,column=1,sticky=W)
        self.quitButton.grid(row=3,column=2,sticky=W)

        '''Closure'''
        def fileChoice(choice):
            self.choice = choice
            self.Frame.quit()

    def returnChoice(self):
        self.Frame.quit()
        return self.choice

def start(symbolList):
    root = Tk()
    root.wm_attributes('-topmost',1)
    a1 = ExistOrNew(root,symbolList) #,sentence)
    root.geometry("400x150+10+10")
    root.title('STEP 2')
    b1 = a1.requestFileOrigin()
    root.mainloop()

    c1 = a1.returnChoice()
    if c1 == 0:
        print ('Existing', c1)
    elif c1 == 1:
        print('New', c1)
    else:
        print('You quit')

    return c1

# Following line is for isolated testing only. Comment out otherwise
start(['T'])

## if __name__ == '__main__': main()