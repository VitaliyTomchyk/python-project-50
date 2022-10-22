def replaces_of_special_values(val):
    bool_elements = {'True': 'true',
                     'False': 'false',
                     'null': 'null',
                     'None': 'None',
                     '[complex value]': '[complex value]',
                     '0': '0'}

    if str(val) in bool_elements:
        return bool_elements.get(str(val))
    else:
        return str("'{}'".format(val))


def none_to_null(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            none_to_null(dictionary[key])
        elif dictionary[key] is None:
            dictionary[key] = 'null'
    return dictionary


def bool_to_lower_case_str(dictionary):

    for key in dictionary:
        if dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is True:
            dictionary[key] = 'true'
    return dictionary


def str_bool_to_lower(result):
    result = str(result).replace("'", "\"")
    result = result.replace("True", "true").replace("False", "false")
    return result
