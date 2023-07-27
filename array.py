# Function that accepts an array and returns the count of
# every element in the array. [S:1, a:1, c:1, e:2, 4:2, 2:2, 1:2]

def count_elements(arr):
    element_count = {}
    for item in arr:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    return element_count

array = ['S', 'a', 'c', 'e', 4, 2, 1, 'e', 4, 2, 1]
result = count_elements(array)
print(result)       

