immutable_var_tuple = (1,True,'привет')
print(immutable_var_tuple)
#immutable_var_tuple[2]= [100] значение является неизменяемым
mutable_list_tuple = [1,2,3],[True,'привет']
print(mutable_list_tuple)
mutable_list_tuple[1][1]='poka'
mutable_list_tuple[1].append('new word')
mutable_list_tuple[0].remove(2)
mutable_list_tuple[0].extend('привет')
print(mutable_list_tuple)