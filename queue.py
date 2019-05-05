
class Queue:
    def __init__(self,maxsize=2):
        self.items = []
    def is_empty(self):
        return self.items == []
    
    def put(self,item):
         self.items.append(item)

    def  get(self):
        return self.items.pop()

  
