def print_params(a=1, b='Hi', c=True):
    print(a, b, c)


print_params(1)
print_params(1, 2)
print_params(1, 2, 3)
print_params(b=25)
print_params(c=[1, 2, 3])
valies_list = [4, "Yes", 3.14]
values_dict = {'a': 4,'b': 5, 'c': 9}
print_params(*valies_list)
print_params(**values_dict)
valies_list_2 = [1,'one']
print_params(*valies_list_2,42)
