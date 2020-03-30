#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear as execution increases with output


b) O(n^2) due to the nesting of the loops


c) Recursive function has time complexity O(n) n standing for number of elements "bunnies"

## Exercise II

We could use a binary search since the floors are in order.
```
#Pass in an array of floors and the Floor the egg will break past
def egg_break(arr,floor):
    #Set last floor
    low = 0
    #Set High Floor
    high = len(arr) - 1
    #While loop as long as the lowest floor is less than the highest Floor
    while low <= high:
    #Find the middle of the high and low floor
        middle = (low + high)/2
    #Check if breaking floor is higher or lower than mid floor
        if floor < arr[middle]:
            high = middle - 1
        elif floor > arr[middle]:
            low = middle + 1
    #Return highest floor you can drop without breaking
        else:
            return middle

```