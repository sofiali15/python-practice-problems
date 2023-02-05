def negate_list(lst):
    """
    Produce a *new* list with its values negated

    Inputs:
        lst [list[int]]: a list of positive and negative integers

    Returns [list[int]]: a new list of integers where values from the old list
    have been negated
    """
    new = []
    for val in lst:
        val = val * -1
        new.append(val)

    new_lst = new

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return new_lst


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_negate_list(lst, expected):
    recreate_msg = utils.gen_recreate_msg("negate_list", *(lst,))
    lst_copy = lst[:]

    actual = negate_list(lst)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)
    utils.check_list_unmodified("lst", before=lst_copy, after=lst)



def test_negate_list_1():
    do_test_negate_list(lst=[1, 2, 3, 4], expected=[-1, -2, -3, -4])


def test_negate_list_2():
    do_test_negate_list(lst=[-1, -2, -3, -4], expected=[1, 2, 3, 4])


def test_negate_list_3():
    do_test_negate_list(lst=[-1, 2, -3, 4], expected=[1, -2, 3, -4])


def test_negate_list_4():
    do_test_negate_list(lst=[], expected=[])