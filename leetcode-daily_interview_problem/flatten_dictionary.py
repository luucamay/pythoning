'''
Flatten Dictionary - Daily Interview Problem
Given a nexted dictionary, flatten the dictionary, where nested dictionar keys can be represented through dot notation
'''

def flatten_dictionary(d):
    values = d.values()
    keys = d.keys()
    output = {}
    while keys:
        current_key = keys.pop()
        current_value = values.pop()
        if isinstance(current_value, (str, int)):
            output[current_key] = current_value
        else:
            for e in current_value:
                dot = ""
                if current_key != "" and e != "":
                    dot = "."
                keys.append(current_key + dot + e)
                values.append(current_value[e])
    return output
# Test
d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': {
                "" : 1
            }
        }
    }
}
print(flatten_dictionary(d))
d = {'a':
     {
         '':
         {
             'c':
             {
                 '': 1
             }
         }
     }
}
print(flatten_dictionary(d))

