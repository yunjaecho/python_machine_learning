
class A:
    def __init__(self):
        print(str(self))

from Machine_and_Deep_Learning_with_Python.module import b

class C(b.B):
    def __str__(self):
        return 'C'