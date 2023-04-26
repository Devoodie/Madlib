import string
import os
import json


class Story:
    def __init__(self, name, location):
        self.name = name
        self.keywords = {}
        with open(location, "r") as f:
            self.story = f.read()

    def savestory(self):
        ogpath = "C:\\Users\\devan\\PycharmProjects\\pythonProject\\"
        os.mkdir(f"{self.name}")
        newpath = os.path.join(ogpath, f"{self.name}")
        with open(newpath + "\\story.txt", "w") as savefile:
            json.dump(self.story, savefile)
        with open(newpath + "\\keywords.txt", "w") as savefile:
            json.dump(self.keywords, savefile)

    def finder(self):
        for count, character in enumerate(self.story):
            if self.story[count + 1] != "_":
                if character == "_" and self.story[count + 1] in string.punctuation:
                    return count + 1
            if character == "_" and self.story[count + 1] == " ":
                return count + 1

    def slicer(self):
        keywordvalues = list(self.keywords.values())
        arrayindex = 0
        while self.story.find("_") != -1 and arrayindex < len(self.keywords):
            resetpoint = self.story.find("_")
            print(resetpoint, "reset")
            placeholderstring = self.story[:resetpoint] + keywordvalues[arrayindex] + self.story[self.finder():]
            self.story = placeholderstring
            arrayindex += 1

    def dictmaker(self, amount):
        for i in range(amount):
            wordplaceholder = str(input("What type of word will be input?"))
            if wordplaceholder in self.keywords.keys():
                self.keywords[f"{wordplaceholder}{i}"] = ""
            else:
                self.keywords[wordplaceholder] = ""


def makenewstory():
    choice = str(input("What do you want to do? Import Story? Random Story? Specific Story?"))
    while True:
        if choice == "import":
            newstory = Story(input("Enter the name of the story!"), input("Enter the file path!"))
            iterations = int(input("How many Keywords are there?"))
            newstory.dictmaker(iterations)
            print(newstory.keywords.keys())
            newstory.savestory()
            break
        elif choice == "random":
            break
        elif choice == "specific":
            break
        else:
            choice = str(input("There was a typo. Enter import, random, or specific."))


makenewstory()
