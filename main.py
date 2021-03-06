import json
from difflib import get_close_matches  # this is for getting the closer match of the word

data = json.load(open('data.json'))

# new line added
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]


    elif w.title() in data:
        return data[w.title()]


    elif w.upper() in data:  # in case user enters uppercase words like USA or NATO
        return data[w.upper()]


    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead ? Enter Y is yes or N if no : ")
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exits !!!  Please enter the valid word... "
        else:
            return "We didn't understand your query !!! "


    else:
        return "The word doesn't exits !!!  Please enter the valid word... "


word = input('Please Enter the word : ')

output = translate(word)

# However we get the output in list format. To get it in str format we have to iterate through it.
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)


# this is the branch 2