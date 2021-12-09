#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Function that divides element by element 2 lists.

    Args:
        my_list_1: numerators containing list
        my_list_2: denominators containing list
        list_length: length of the result containing list

    Returns:
        Returns a new list with all divisions
    """
    result_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            result_list.append(0)
            continue
        except IndexError:
            print("out of range")
            result_list.append(0)
            continue
        finally:
            result_list.append(result)
    return result_list
