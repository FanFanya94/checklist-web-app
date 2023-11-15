DEFAULT_FILEPATH = "todos.txt"


def save_list_to_file(list_to_save, filename=DEFAULT_FILEPATH):
    """
    The function saves list's elements to the text file.
    Every element is placed in one line.
    """
    with open(filename, 'w') as file_:
        file_.writelines([item_ + "\n" for item_ in list_to_save])


def get_list_from_textfile(filename=DEFAULT_FILEPATH):
    """
    The function gets lines from the text file and save
    them as a list. Every line is striped from special str symbols.
    """
    with open(filename, 'r') as file_:
        loaded_list = file_.readlines()
    loaded_list = [item_.strip() for item_ in loaded_list]

    return loaded_list


def indexate_list(list_to_indexate):
    """
    Gets a list and returns the new list of tuples with indexes beginning from 1
    and values of original list. Ex: [(1, value1), (2, value2), ... (N, valueN)]
    """
    indexed_list = []

    for index, value in enumerate(list_to_indexate):
        indexed_list.append((str(index + 1) + '.', value))

    return indexed_list
