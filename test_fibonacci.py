import fibonacci
import pytest
import unittest

def test_recur_fibo():
    assert fibonacci.recur_fibo(2) == 1
    assert fibonacci.recur_fibo(10) == 55
    #assert fibonacci.recur_fibo("10") == 55
    assert fibonacci.recur_fibo(-2) == -2
    #assert fibonacci.recur_fibo("10") == 55
    #self.assertEqual(fibonacci.recur_fibo(10),55)

    with  pytest.raises(TypeError):
        fibonacci.recur_fibo("karth")

    with  pytest.raises(TypeError):
        fibonacci.recur_fibo("@")

    #with  pytest.raises(AssertionError):
        #fibonacci.recur_fibo(-10)