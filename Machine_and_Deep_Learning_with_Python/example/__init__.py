from pkgutil import get_data

data = get_data('example', 'data/datafile.txt')
print(data)