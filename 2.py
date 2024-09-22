first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_res = [len(i) for i in first_strings if len(i)>5 ]
second_res = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_res = {x:len(x) for x in first_strings + second_strings if not len(x) % 2}


print(first_res)
print(second_res)
print(third_res)