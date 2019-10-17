'''
In simple terms, a dictionary is a collection of unique keys and their values.
The values can typically be of any primitive type (i.e an integer, boolean, double,
string etc) or other dictionaries (dictionaries can be nested).
However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.

If you're using a compiled language such Java, C++, C#, Swift and Go, you may want to use a
Map/Dictionary/Hash Table that maps strings (keys) to a generic type
(e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).
'''
def flatten_dictionary(dictionary):
  keys = dictionary.keys()
  values = dictionary.values()
  new_dict = {}
  while keys:
    key = keys.pop(0)
    value = values.pop(0)
    if isinstance(value, (str, int)):
      new_dict[key] = value
    else:
      for child_key in value:
        if child_key == "":
          keys.append(key)
        elif key == "":
          keys.append(child_key)
        else:
          keys.append(key + "." + child_key)
        values.append(value[child_key])
  return new_dict

# Test
dict = {
  "Key1" : "1",
  "Key2" : {
    "a" : "2",
    "b" : "3",
    "c" : {
      "d" : "3",
      "e" : {
        "" : "1"
      }
    }
  }
}

print flatten_dictionary(dict)
