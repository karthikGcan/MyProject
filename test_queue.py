import queue

def test_put():

    L = queue.Queue(maxsize=2) 
    L.put(1)
    L.put(1)
    L.put(1)
    L.get()
    L.get()
    L.get()
