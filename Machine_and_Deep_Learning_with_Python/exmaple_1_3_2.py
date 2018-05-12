
def foo():
    pass

print(foo)

bar = foo
print(bar)

foo = 5
print(foo)
print(bar)
print(bar.__name__)

bar.plugin_name = 'demo'
print("bar.plugin_name : " + bar.plugin_name)

import atexit
atexit.register(bar)

import collections
d = collections.defaultdict(list)
print(d)


class Example:
    class_trait = 5

    def __init__(self):
        self.instance_trait = 7

print(Example)

def new_function(self):
    print(self.instance_trait, self.class_trait)

print("#########################")

Example.added = new_function
x = Example()
x.added()

Example.class_trait = 9
x.added()

