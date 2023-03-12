"""
Write a Python program to find intersection of two given lists using lambda function. Example: for two given lists: list_nums1 = [1, 2, 3, 5, 7, 8, 9, 10] list_nums2 = [1, 2, 4, 8, 9] the program should return the list [1, 2, 8, 9] Tip: pass the lambda function as argument to the filter() function

"""
list1 = [1, 2, 4, 8, 9]
list2 = [1, 2, 3, 5, 7, 8, 9, 10]
find_intersection = list(filter(lambda x: x in list1, list2))

print(find_intersection)