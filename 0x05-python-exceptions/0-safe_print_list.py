#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0

    try:
        for i in my_list:
            if ret < x:
                print('{}'.format(my_list[ret]), end='')
                ret += 1

        print()
    except TypeError:
        pass
    finally:
        return ret
