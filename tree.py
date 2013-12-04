#Tree is used to represent our decision tree

class Tree:
  
  def __init__(self, name, depth, yes, no, label):
    self.name= name
    self.depth= depth
    self.yes= yes
    self.no= no
    self.label= label
    
  #type: 0->no, 1->yes
  def setBranch(self, type, tr):
    if type:
      self.yes= tr
    else:
      self.no= tr

  #type: 0->no, 1->yes
  def getBranch(self, type):
    if type:
      return self.yes
    else:
      return self.no

  def getDepth(self):
    return self.depth

  def setLabel(self, label):
    self.label= label

  def getLabel(self):
    return self.label

  def setName(self, name):
    self.name=name
    
  def getName(self):
    return self.name
