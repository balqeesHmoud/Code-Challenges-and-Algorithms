# test_challenge04.py

from challenge04 import *

def test_reverse_queue():
    q = Queue()
    for i in [5, 4, 3, 2, 1]:
        q.put(i)

    reversed_q = reverse_queue(q)
    
    result = []
    while not reversed_q.empty():
        result.append(reversed_q.get())
    
    assert result == [1, 2, 3, 4, 5]

def test_reverse_empty_queue():
    q = Queue()
    reversed_q = reverse_queue(q)
    
    result = []
    while not reversed_q.empty():
        result.append(reversed_q.get())
    
    assert result == []
