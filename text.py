def binary_search(search_list, target):
    left = 0
    right = len(search_list) - 1

    while left < right:
        mid = (right - left) // 2
        if search_list[mid] == target:
            return mid
        if search_list[mid] < target:
            left = mid + 1
        if search_list[mid] > target:
            right = mid - 1
    return -1

target_list = [1, 5, 6, 7 , 8 ,9]
print(binary_search(target_list,9))












#     while left <= rig:
#         mid = int((low + high) / 2)
#         guess = list[mid]
#         if guess == item:
#             return guess
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# my_list = [1, 3, 5, 7, 9]
#
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))
#
