from typing import List, Any

calls = 0
def count_cals(f):
    global calls
    calls += 1
    return calls
def string_info(string):
    count_cals(calls)
    return [len(string), string.upper(), string.lower()]


# noinspection PyUnreachableCode
def is_contains(string, list_to_search):
    count_cals(calls)
    lower_string = string.lower()
    lower_list: list[Any] = [string.lower() for string in list_to_search ]
    return lower_string in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
