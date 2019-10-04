
"""
Write a function that receives an array of integers and returns an array of the products.

For example, given 
```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```
"""


def product_of_others(arr):
    result = [1]*len(arr)
    for index, val in enumerate(arr):
        for sub_i, sub_v in enumerate(arr):
            if sub_i != index:
                result[index] *= sub_v
    return result


print(product_of_others([1, 7, 3, 4]))
