import string

def makenewstory(name,filelocation):
   name= Stories(filelocation)
class Stories:
   def __init__(self, location):
      self.keywords = []
      with open(location,"r") as f:
         self.story = f.read()

   def finder(self):
      for character in enumerate(self.story):
         if character == "_" and self.story[self.story.find(character)+1] in string.punctuation:
            return self.story.find(character+"")
            break
         elif character == "_" and self.story[self.story.find(character)+1] == " ":
            return self.story.find(character+" ")
            break

   def slicer(self):
      arrayindex = 0
      placeholderString = ""
      i=0
      while self.story.find("_") != -1 and arrayindex<len(self.keywords):
         resetPoint=self.story.find("_")
         end_=self.story.find("_")
         print(resetPoint, "reset")
         placeholderString = self.story[:resetPoint] + self.keywords[arrayindex] + self.story[self.finder():]
         self.story = placeholderString
         arrayindex += 1

Penis = Stories("D:\D\madlib.txt")
Penis.finder()
