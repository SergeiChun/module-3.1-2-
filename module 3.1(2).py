calls = 0

def count_calls(func):

    def schot(*ar, **kwar):
        global calls
        calls += 1
        return func(*ar, **kwar)
    return schot

@count_calls
def string_info(string):

    return (len(string), string.upper(), string.lower())

@count_calls
def is_contains(string, list_to_search):

    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)