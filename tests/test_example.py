#!/usr/bin/python3

import example

def test_examplemethod_returns1():
    exampleClass = example.ExampleClass
    assert exampleClass.exampleMethod() == 1, "exampleMethod() did not return 1"
