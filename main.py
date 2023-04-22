import string


class Stories:
  def __init__(self, location):
    self.keywords = []
    with open(location,"r") as f:
        self.story = f.read()

  def finder(self):
    for count, character in enumerate(self.story):
      if self.story[count+1] != "_":
        if character == "_" and self.story[count+1] in string.punctuation:
          return count+1
        if character == "_" and self.story[count+1] == " ":
          print(count)
          return count+1
  def slicer(self):
    arrayindex = 0
    placeholderString = ""
    while self.story.find("_") != -1 and arrayindex<len(self.keywords):
      resetPoint=self.story.find("_")
      print(resetPoint, "reset")
      placeholderString = self.story[:resetPoint] + self.keywords[arrayindex] + self.story[self.finder():]
      self.story = placeholderString
      arrayindex += 1