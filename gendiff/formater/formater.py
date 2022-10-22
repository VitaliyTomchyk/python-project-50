from gendiff.additionals.additional_tools import transforms_option_to_string, \
    dict_to_complex_value, inner_parent_generator, stylish_result_wrapper
from gendiff.additionals.checkers import is_deep
from gendiff.additionals.result_generators import plain_result_generator, \
    stylish_result_generator, json_result_appender
from gendiff.additionals.replacers import str_bool_to_lower


def stylish(dictionary):
    def inner(dictionary, result, level=1):
        for key in sorted(list(dictionary)):
            dict_value = dictionary[key]

            if isinstance(dict_value, dict) and is_deep(dict_value):
                value = inner(dict_value, "", level + 1)
                result = result + transforms_option_to_string(key, level,
                                                              value,
                                                              'common')

            elif isinstance(dict_value, list):
                result = stylish_result_generator(dict_value, key,
                                                  level, result)

            else:
                result = result + transforms_option_to_string(key, level,
                                                              dict_value,
                                                              'common')

        result = stylish_result_wrapper(result, level)
        return result
    return inner(dictionary, '')


def added_line_generator(value, function, inner_parent):
    if isinstance(value, list):
        return plain_result_generator(inner_parent, value)
    if isinstance(value, dict):
        return function(value, '', inner_parent)
    return ''


def plain(dictionary):
    def inner(dictionary, result, parent):
        for key in sorted(list(dictionary)):
            inner_parent = inner_parent_generator(parent, key)
            added_line = added_line_generator(dictionary[key], inner,
                                              inner_parent)
            result = result + added_line
        return result
    return inner(dictionary, '', '')[1::]


def json_decoder(dictionary):
    result = {"added": {},
              "removed": {},
              "updated": {}}

    def inner(dictionary, result, parent):
        for key in dictionary:

            inner_parent = inner_parent_generator(parent, key)

            if isinstance(dictionary[key], dict):
                inner(dictionary[key], result, inner_parent)

            if isinstance(dictionary[key], list):
                pair = list(map(dict_to_complex_value, dictionary[key]))
                result = json_result_appender(result, pair, key, inner_parent)

        result = str_bool_to_lower(result)
        return result

    return inner(dictionary, result, '')
