import string
import os
import json


class Story:
    def __init__(self, name):
        self.name = name
        self.keywords = {}
        self.story = ""
        self.data = {}

    def savestory(self, location):
        os.mkdir(f"{self.name}")
        with open(location, "r") as f:
            self.story = f.read()
        self.data = {'keywords': self.keywords, 'story': self.story}
        with open(self.name+"\\"+self.name+".txt", "w") as savefile:
            json.dump(self.data, savefile)

    def namecheck(self, stopthatshit=0):
        recursion = stopthatshit
        if recursion >= 100:
            print("FIND A VALID NAME!")
            exit()
        elif os.path.exists(self.name + ".txt") is False:
            pass
        else:
            newordelete = str(input("That story already exists! Do you want to create a new one, delete the old one, or load the old one?"))
            while True:
                if newordelete == "delete":
                    os.remove(self.name + ".txt")
                    break
                elif newordelete == "new":
                    self.name = str(input("enter a valid name!"))
                    self.namecheck(recursion+1)
                    break
                elif newordelete == "load":
                    self.loadstory()
                    self.runstory()
                    return 0
                else:

    def loadstory(self):
        with open(os.path.realpath(self.name)+"\\"+self.name+".txt", "r") as savefile:
            tempdict = json.load(savefile)
        self.keywords = tempdict['keywords']
        self.story = tempdict['story']

    def runstory(self):
        for count, key in enumerate(self.keywords):
            if f"{count}" in key:
                printkey = key.replace(f"{count}", "")
                self.keywords[key] = input(f'Enter another {printkey}')
            else:
                self.keywords[key] = input(f'Enter a {key}')
        print(self.slicer())

    def finder(self):
        for count, character in enumerate(self.story):
            if self.story[count + 1] != "_" and self.story[count+1] != "\\":
                if character == "_" and self.story[count + 1] in string.punctuation:
                    return count + 1
            if character == "_" and self.story[count + 1] == " ":
                return count + 1
            if character == "_" and self.story[count + 1] in string.ascii_letters:
                return count + 1

    def slicer(self, vers=1):
        if vers == 1:
            keywordvalues = list(self.keywords.values())
            arrayindex = 0
            while self.story.find("_") != -1 and arrayindex < len(self.keywords):
                resetpoint = self.story.find("_")
                placeholderstring = self.story[:resetpoint] + keywordvalues[arrayindex] + self.story[self.finder():]
                self.story = placeholderstring
                arrayindex += 1
            return self.story
        else:
            for count, lettercombo in self.story:
                if lettercombo == "_" and self.story[count-1] in string.ascii_letters:
                    resetpoint = count - 1
                    placeholderstring = self.story[:resetpoint] + " " + self.story[lettercombo:]
                    self.story = placeholderstring
                if lettercombo == "_" and self.story[count+1] in string.ascii_letters:
                    resetpoint = count+1
                    placeholderstring = self.story[:lettercombo] + " " + self.story[resetpoint:]
                    self.story = placeholderstring

    def dictmaker(self, amount):
        for i in range(amount):
            wordplaceholder = str(input("What type of word will be input?"))
            if wordplaceholder in self.keywords.keys():
                self.keywords[f"{wordplaceholder}{i}"] = ""
            else:
                self.keywords[wordplaceholder] = ""


def runprogram():
    choice = str(input("What do you want to do? Import Story? Random Story? Specific Story?"))
    while True:
        if choice == "import":
            newstory = Story(input("Enter the name of the story!"))
            if newstory.namecheck() == 0:
                break
            iterations = int(input("How many Keywords are there?"))
            newstory.dictmaker(iterations)
            print(newstory.keywords.keys())
            newstory.slicer(vers=2)
            newstory.savestory(input("Enter the file path of the story to import!"))
            loadornah = input("do you want to run the story? Yes or no?")
            if loadornah == "yes":
                newstory.runstory()
            if loadornah == "no":
                break
            break
        elif choice == "random":
            break
        elif choice == "specific":
            newstory = Story(input("What is the name of the story?"))
            newstory.loadstory()
            newstory.runstory()
            break
        else:
            choice = str(input("There was a typo. Enter import, random, or specific."))


runprogram()
