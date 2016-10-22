"""
This module takes pattern and path data from stdin and
prints best matching pattern or NO MATCH to stdout for each path.
"""

def get_sort_value(pattern):
    '''
    Takes a pattern string with fields delimited by the ',' symbol.
    Returns a wildcard sort value used to sort against other strings
    with the same field count and the same count of '*' symbol.
    Strings whose leftmost '*' appears in a field further to the right
    are preferred. If patterns have '*' symbols in the same leftmost position,
    we can look right until we find a '*' whose position is different.
    To achieve this, we can represent the position of wildcards in the fields
    as bits turned on in a binary number and return it's value.
    Least preferred configurations are given higher numbers,
    >>> get_sort_value('c,c,c')
    0
    >>> get_sort_value('*,c')
    2
    >>> get_sort_value('c,*')
    1
    '''
    result = 0
    pattern = pattern.split(',')
    pattern_length = len(pattern)
    for field_index, field in enumerate(pattern):
        if field == '*':
            result += 2**(pattern_length - field_index - 1)
    return result

def get_sorted_patterns(patterns):
    """
    Takes a list of patterns and returns a list sorted first by descending
    wildcard count and last by descending wildcard sort value.
    >>> get_sorted_patterns(['*,c', 'c,c', 'c,*'])
    ['c,c', 'c,*', '*,c']
    """
    return sorted(patterns, key=lambda x: (x.count('*'), get_sort_value(x)))

def path_matches_pattern(path, pattern):
    """
    Checks whether a path matches a pattern, both in array form. A pattern
    field with a wildcard can match anything in a corresponding path field.
    >>> path_matches_pattern(['c', 'hey'], ['c', '*'])
    True
    >>> path_matches_pattern(['c'], [])
    False
    """
    if len(path) != len(pattern):
        return False
    for field_index, pattern_field in enumerate(pattern):
        if pattern_field == '*':
            continue
        if path[field_index] != pattern_field:
            return False
    return True

def get_path_and_patterns():
    """
    Gets path and pattern lists from stdin.
    """
    import sys
    input_str = sys.stdin.readlines()
    patterns = []
    pattern_count = int(input_str[0])
    offset = 1
    for i in range(offset, pattern_count + offset):
        patterns.append(input_str[i].rstrip())
    paths = []
    path_count = int(input_str[pattern_count + 1])
    offset = pattern_count + 2
    for i in range(offset, path_count + offset):
        paths.append(input_str[i].rstrip())
    return paths, patterns

def get_and_print_results():
    """
    Gets data from stdin and prints pattern matching results to stdout.
    """
    paths, patterns = get_path_and_patterns()
    patterns = get_sorted_patterns(patterns)
    patterns = [x.split(',') for x in patterns]
    for path in paths:
        # Leading and trailing slashes in paths should be ignored.
        path = path.strip('/').split('/')
        found_match = False
        for pattern in patterns:
            if path_matches_pattern(path, pattern):
                found_match = True
                print ','.join(pattern)
                break
        if not found_match:
            print 'NO MATCH'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    get_and_print_results()
