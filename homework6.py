my_dict = {'Vova': 1999,'Vera': 1996,'Ira':2000,'Egor':2024}
print(my_dict)
a=my_dict['Vova']
print(a)
b=my_dict.get('Lesha')
print(b)
my_dict.update({'Saha': 2003,
                'Vika':2001})
c=my_dict.pop('Vera')
print(c)
print(my_dict)
my_set = {1,4,'Vova',1,4,'Vova'}
print(my_set)
my_set.update(["Saha",8])
my_set.discard(1)
print(my_set)