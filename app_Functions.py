import json
import JSONManipulator
import tkinter_Objects
import datetime

def main():

    while True:

        tkinter_Objects.window.mainloop()

        break

    JSONVar = JSONManipulator.JSONManipulator("data/data.json", "r")
    JSONVar.dumpJSON(eosIterator(tkinter_Objects.nameList,
                                 tkinter_Objects.statList,
                                 tkinter_Objects.summaryList,
                                 tkinter_Objects.bugDict))

    autoMessage()

def autoMessage():
    loadJSON = json.load(open("data/data.json"))

    keyList = []
    for i in loadJSON.keys():
        keyList.append(i)
    iterations = len(keyList)
    counter = 0

    if iterations == 0:
        print("\n\nHi all, \n\nToday we ", end='')
        print("assisted RTB with tasks.")

    for it in range(0, iterations):

        for i in loadJSON.keys():
            keyList.append(i)

        valueList = loadJSON.get(keyList[counter])

        if it == 0:
            print("\n\nHi all, \n\n\nToday we ", end='')
            print("{0} *{1}* - {2} - http://developer.origin.com/browse/{3} \n".format(valueList[0][0][0],
                                            keyList[counter], valueList[0][0][1], keyList[counter]))
        else:
            print("We also {0} *{1}* - {2} - http://developer.origin.com/browse/{3} \n".format(valueList[0][0][0],
                                                                                keyList[counter], valueList[0][0][1],
                                                                                keyList[counter]))
        bugDict = loadJSON.get(keyList[counter])[0][1]
        if len(bugDict.get("Bugs")) > 0:

            print("\nThe following issues were observed: \n\n")

            for b in bugDict.get("Bugs"):

                print("*{0}* - {1} - http://developer.origin.com/browse/{2}".format(b[0], b[1], b[0]))

            it +=1
            counter += 1
            print("\n")
        else:

            print("\nNo issues were observed \n\n")
            it +=1
            counter += 1

    date = datetime.date (datetime.datetime.now ().year, datetime.datetime.now ().month, datetime.datetime.now ().day)
    if date.weekday() == 4:
        print("\n- Have a great evening and weekend!\n\n")
    else:
        print("\n- Have a great evening!\n\n")

def eosIterator(ticket, progress, summary, bugs):
    newD = {}
    newKeys = bugs.keys()

    for n in newKeys:
        print(bugs.get(n))

    for i in range(0, len(ticket)):

        newD[ticket[i]] = [[
                    [
                        progress[i],
                        summary[i]
                    ],
                    bugs.pop(ticket[i])
                ]]

        i += 1

    # old bug iterator
    '''
        for k in newKeys:
        newD1 = newD.get(k)
        if bugs.get(k) not in newD1[0][1]["Bugs"]:
            newD1[0][1]["Bugs"] = bugs.get(k)
    '''
    return newD

def saveToDict(ticketName, bugNWidgets, bugSWidgets):
    bugNames = []
    bugSums = []
    newL = []
    newD = {}
    if len(bugNWidgets) == 0:
        newD["Bugs"] = []
        tkinter_Objects.bugDict[ticketName] = newD
    else:
        for bN in bugNWidgets:
            print(bN.get())
            bugNames.append(bN.get())
        for bS in bugSWidgets:
            bugSums.append(bS.get())
        for i in range(len(bugNames)):
            newL.append([bugNames[i],bugSums[i]])
        newD["Bugs"] = newL
        tkinter_Objects.bugDict[ticketName] = newD
    print(tkinter_Objects.bugDict)

def goBug(name, bugs):
    tkinter_Objects.bugNameWidgets.clear()
    tkinter_Objects.bugSumWidgets.clear()
    bugWindow = tkinter_Objects.Tk()
    l = tkinter_Objects.Label(bugWindow, text=name)
    l.grid(row=0)
    r=1
    a=0

    if bugs > 0:
        for i in range(0, bugs):
            bugEntries = []
            bugSummaries = []

            bugEntries.append(("bugEntryWidget_" + str(i)))
            bugSummaries.append(("bugSummaryWidget_" + str(i)))
            for b in bugEntries:
                bE = tkinter_Objects.Entry(bugWindow)
                bE.insert(tkinter_Objects.END, "Enter bug title here")
                bE.grid(row=r)
                tkinter_Objects.bugNameWidgets.append(bE)
            for p in bugSummaries:
                pE = tkinter_Objects.Entry(bugWindow)
                pE.insert(tkinter_Objects.END, "Enter bug summary here")
                pE.grid(row=r, column=1)
                tkinter_Objects.bugSumWidgets.append(pE)
            r+=1

    buttonSave = tkinter_Objects.Button(bugWindow, text="Save", command= lambda : saveToDict(name, tkinter_Objects.bugNameWidgets, tkinter_Objects.bugSumWidgets))
    buttonSave.grid(row=r, column=1, sticky="w")
    bugWindow.mainloop()

def exFunc(var):
    c = 3
    r = 3
    f = 0
    z = 0
    for i in range(0, tkinter_Objects.amount.get()):
        nameList = []
        sumList = []
        progList = []
        bugLabelList = []
        bugList = []
        buttonList = []
        tkinter_Objects.bugAmountList.append(("bugAmountVariable_" + str(i)))
        tkinter_Objects.statusList.append("statusVariable" + str(i))
        buttonList.append(("buttonWidget_" + str(i)))
        bugList.append(("bugListWidget_" + str(i)))
        bugLabelList.append(("bugLabelWidget_" + str(i)))
        progList.append(("progressWidget_" + str(i)))
        nameList.append("entryWidget_" + str(i))
        sumList.append("summaryWidget_" + str(i))
        for n in nameList:
            n = tkinter_Objects.Entry(tkinter_Objects.window)
            n.insert(tkinter_Objects.END, "Enter ticket here")
            n.grid(row=r)
            tkinter_Objects.nameWidgets.append(n)
        for s in sumList:
            s = tkinter_Objects.Entry(tkinter_Objects.window)
            s.insert(tkinter_Objects.END, "Enter summary here")
            s.grid(row=r, column=1)
            tkinter_Objects.sumWidgets.append(s)
        for p in progList:
            tkinter_Objects.statusList[z] = tkinter_Objects.StringVar()
            opts = ["completed", "began", "continued"]
            p = tkinter_Objects.OptionMenu(tkinter_Objects.window, tkinter_Objects.statusList[z], *opts)
            p.grid(row=r, column=2)
            z +=1
            tkinter_Objects.statWidgets.append(p)
        for bLL in bugLabelList:
            bLL = tkinter_Objects.Label(tkinter_Objects.window, text="Bugs")
            bLL.grid(row=r, column=3)
        for bl in bugList:
            tkinter_Objects.bugAmountList[r-3] = tkinter_Objects.IntVar()
            opts = [0,1,2,3,4,5,6,7,8,9,10]
            bl = tkinter_Objects.OptionMenu(tkinter_Objects.window, tkinter_Objects.bugAmountList[r-3], *opts, command= lambda bugs=tkinter_Objects.bugAmountList[r-3], issueName=n : goBug(issueName.get(), bugs))
            bl.grid(row=r, column=4)
            f +=1

        r += 1

def func():
    for i in range(0, tkinter_Objects.amount.get()):
        tkinter_Objects.summaryList.append(tkinter_Objects.sumWidgets[i].get())
        tkinter_Objects.nameList.append(tkinter_Objects.nameWidgets[i].get())
        tkinter_Objects.statList.append((tkinter_Objects.statusList[i].get()))
        tkinter_Objects.bugAmounts.append((tkinter_Objects.bugAmountList[i].get()))

    print(tkinter_Objects.summaryList)
    print(tkinter_Objects.nameList)
    print(tkinter_Objects.statList)
    print(tkinter_Objects.bugAmounts)
