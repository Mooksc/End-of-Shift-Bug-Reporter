from tkinter import *
import app_Functions

window = Tk()
bugDict = {}
bugNameWidgets = []
bugSumWidgets = []
nameWidgets = []
sumWidgets = []
statWidgets = []
statusList = []
statList = []
bugAmountList = []
bugNameGet = StringVar()
bugSumGet = StringVar()
bugAmounts = []
nameList = []
summaryList = []
opts = [1,2,3,4,5]
amount = IntVar()

textLabel = Label(window, text="How many issues?")

issueAmount = OptionMenu(window, amount, *opts, command=app_Functions.exFunc)

button1 = Button(window, text="Go", command=app_Functions.func)

textLabel.grid(row=0, column=0, sticky="n", pady=1)
issueAmount.grid(row=1, column=0, sticky="n", pady=1)
button1.grid(row=2, column=0, sticky="n", pady=1)
