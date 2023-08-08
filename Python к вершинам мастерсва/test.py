# import random

# def bubble_sort(nums):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):

#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True


# random_list_of_nums = [random.randint(0,100) for _ in range(100)]
# print(random_list_of_nums)
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        print(i)
        # Находим индекс минимального элемента в неотсортированной части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем минимальный элемент с первым элементом в неотсортированной части
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Отсортированный массив:", arr)