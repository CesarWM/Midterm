def find_pattern(text):
    """
    Finds all occurrences of a pattern that starts with 'C', and ends with 'jeb'.

    Parameters:
    text (str): The text to search within.

    Returns:
    int: The number of matches found.
    """
    count = 0
    i = 0
    while i < len(text):
        start_index = text.find('C', i)
        if start_index == -1:
            break
        end_index = text.find('jeb', start_index)
        if end_index != -1:
            count += 1
            i = end_index + len('jeb')
        else:
            i = start_index + 1
    return count
