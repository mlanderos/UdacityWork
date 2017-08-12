# def product_list(list_of_numbers):
#    total = 1
#    for i in list_of_numbers:
#        total = total * i
#        print total
#    return total
#product_list([1,2,3])

def greatest(list_of_nums):
    if len(list_of_nums) < 1:
        return 0
    list = list_of_nums
    return max(list_of_nums)

print greatest([])