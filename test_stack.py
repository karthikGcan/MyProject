#import stack
#import pytest


#def test_push():
    #s = stack.Stack()
    #s.push(5)
    #s.push(5)
    #s.push(5)
    #s.push(5)
    #s.push(5)
    #s.push(5)
    #s.push(5)
   
    #s.pop()
    #with pytest.raises(IndexError):
        #s = stack.Stack(maxsize=5)
        #assert s.pop == 0
    
import stack
import unittest

class TestStack(unittest.TestCase):
  def testPush(self):
    s = stack.Stack()
    for value in range(1,101):
      self.assertEqual(True, s.push(value))
		
  def testPop(self):
    s = stack.Stack()
    for value in range(1, 11):
      self.assertEqual(True, s.push(value))
      self.assertEqual(True, s.pop())
		
    self.assertEqual(False, s.pop())
	
  def testPeek(self):
    s = stack.Stack()
    for value in range(1, 11):
      self.assertEqual(True, s.push(value))
      self.assertEqual(value, s.peek())
	
  def testHas(self):
    s = stack.Stack()
    for value in range(1, 11):
      self.assertEqual(True, s.push(value))
      self.assertEqual(True, s.has(value))
      self.assertEqual(False, s.has(value+1))
	
  def testSize(self):
    s = stack.Stack()
    for value in range(1, 11):
      self.assertEqual(True, s.push(value))
      self.assertEqual(value, s.size())
      self.assertEqual(False, s.has(value+1))
	
  def testClear(self):
    s = stack.Stack()
    for value in range(1, 11):
      self.assertEqual(True, s.push(value))
	
    self.assertEqual(10, s.size())
    s.clear()
    self.assertEqual(0, s.size())

if __name__ == '__main__':
    unittest.main()


    