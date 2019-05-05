#class Stack:

    #def __init__(self):
        #self.items = []
    
    #def is_empty(self):
        #return self.items == []
    
    #def push(self,item,max=5):
         #self.items.append(item)

    #def  pop(self):
        #return self.items.pop()

    #def peek(self):
        #return self.items[len(self.items)-1]


    #def size(self):
        #return len(self.items)

class Stack:
  def __init__(self):
    self.stack = list()
	
  def push(self, value):
    if value == None:
      return False
    else:
      self.stack.insert(0, value)
    return True
	
  def peek(self):
    return self.stack[0]
	
  def pop(self):
    if self.stack:
      self.stack.pop(0)
      return True
    else:
      return False
	
  def size(self):
    return len(self.stack)
	
  def has(self, value):
    if value in self.stack:
      return True
    else:
      return False
	
  def clear(self):
    self.stack = list()
        

   