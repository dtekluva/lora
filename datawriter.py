import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'questions': [] ,
        'answers': [],
        }

# Write JSON file
def from_jason():

    # Read JSON file
    with open('mldata.json') as data_file:
        data_loaded = json.load(data_file)

    data = data_loaded

    return data

def to_jason(new_data):
    
    with io.open('mldata.json', 'w', encoding='utf8') as outfile:

        str_ = json.dumps(new_data,
                        indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)

        outfile.write(to_unicode(str_))

