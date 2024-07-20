def swap_first_last(lst):
    if len (lst) < 2:
        return last
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst
my_list = [1, 2, 3, 4, 5]
print("original list:",my_list)
swapped_list = swap_first_last(my_list)
print("list after swapping first and last elements:",swapped_list)