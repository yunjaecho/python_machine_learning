# dictionary is key, value pair
example_dic = {'a':1 , 'b':2, 'c':3}
# create empty dictionary
another_dict = {}
print(example_dic['b'])
print(example_dic.get('c'))

example_list = ['a', 'b', 'c', 'd', 'e', 'f']

# tuple type
another_list = ()
# list type
another_list = list()

print("[0] :" + example_list[0])
print("[1] : " + example_list[1])
print("[-2] : " + example_list[-2])
example_list.append('happy')

example_tuple = ('Hello', 12, None)
another_tuple = tuple([1,2,3,'jump'])
print("example_tuple[1] : " + str(example_tuple[1]))

example_set = {'a', 'b', 'c', 'd', 'e', 'f'}
another_set = set()
bool_test1 = 'b' in example_set
print('bool_test1 : ' + str(bool_test1))

bool_test2 = 'b' in another_set
print('bool_test2 : ' + str(bool_test2))
example_set.add('b')
print(example_set)

example_set.discard('b')
bool_test3 = 'b' in example_set
print('bool_test3 : ' + str(bool_test3))

capitals = [x.upper() for x in example_list]
print(capitals)

sqares = {k: v ** 2 for k, v in example_dic.items()}
print(sqares)

codes = {ord(x) for x in example_set}
print(codes)

capital_keys = {x.upper for x in example_dic.keys()}

stringified = tuple(str(x) for x in example_tuple)
print(stringified)