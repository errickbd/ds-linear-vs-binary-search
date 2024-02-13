#linear search
def linear_search_unsorted(arr, target):
    steps = 0
    for i, num in enumerate(arr):
        steps += 1
        if num == target:
            return i, steps
    return -1


#binary search
def binary_search_unsorted(arr, target):
    steps = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if arr[middle]  == target:
            return middle, steps
        elif arr[middle] < target:
            left = middle + 1  
        else:
            right = middle - 1
          
    return -1, steps

#scenario 1 test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")


def linear_search_sorted_words(word_list, target_word):
    steps = 0
    for i, num in enumerate(word_list):
        steps += 1
        if num == target_word:
            return i, steps
    return -1

def binary_search_sorted_words(word_list, target_word):
    steps = 0
    left = 0
    right = len(word_list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if word_list[middle] == target_word:
            return middle, steps
        elif word_list[middle] < target_word:
            left = middle + 1
        else:
            right = middle - 1
    return -1, steps
#scenario 2 test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")


# Linear Search
def linear_search_last_occurrence(arr, target):
    steps = 0
    for i, num in enumerate(arr):
        steps += 1
        if num == target:
            return i, steps
    return -1
    

# Binary Search
def binary_search_last_occurrence(arr, target):
    steps = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle, steps
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, steps


# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
