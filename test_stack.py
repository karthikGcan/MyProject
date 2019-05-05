import stack
import pytest


def test_push():
    s = stack.Stack()
    s.push(5)
    s.push(5)
    s.push(5)
    s.push(5)
    s.push(5)
    s.push(5)
    s.push(5)
   
    #s.pop()
    #with pytest.raises(IndexError):
        #s = stack.Stack(maxsize=5)
        #assert s.pop == 0
    
    


    