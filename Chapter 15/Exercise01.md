# Chapter 15 - Exercise 01

## What is the difference between an instance method and a static method?

An instance method works with a particular object. Its first parameter is normally `self`, which refers to the object the method is invoked on.

A static method belongs with a class but does not need a particular object. It does not receive `self` automatically.

## Why are static methods called static?

They can be used without an instance of the class. They are associated with the class rather than one specific object.

## Rewrite subtract_time as a method of the Time class

```python
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def subtract_time(self, other):
        return self.time_to_int() - other.time_to_int()
```
