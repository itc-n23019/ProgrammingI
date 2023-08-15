country_code = {
    'Iceland': {'code': '354', 'capital': 'Reykjavik'},
    'Ireland': {'code': '353', 'capital': 'Dublin'},
    'Azerbaijan': {'code': '994', 'capital': 'Baku'}
}

def getstr_keyval(x):
    if not isinstance(x, dict):
        return x

    my_str = ''
    for key, val in x.items():
        my_str += ('  ' + str(key) + ': ' + getstr_keyval(val) + '\n')
    return my_str

for key1, val1 in country_code.items():
    print(key1 + '\n' + getstr_keyval(val1))

