# 这是一个二分查找的算法
# 每次都将问题一分为二 ，每次的范围都缩小一半，这样的就能快速解决问题
# 注意的是二分查找是针对于升序的列表或者数组 



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
