#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            index1 = my_list_1[i]
            index2 = my_list_2[i]
            if index2 == 0:
                raise ZeroDivisionError()
            if not isinstance(index1,
                              (int, float)) and isinstance(index2,
                                                           (int, float)):
                raise TypeError
            new_list.append(index1/index2)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
