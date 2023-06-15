# Merge Sort
## Steps

- Divide the unsorted array into twp sublists of about half the size.
- Continuously divide each sublist into two sublists until you reach the base case of 1 element.
![sort](./img/000005.png)
- Repeatedly merge partitioned left units to produce new sublists until there is only 1 right sublist remaining. This will be the sorted list at the end.
![sort](./img/000006.png)
![sort](./img/000007.png)
![sort](./img/000008.png)
![sort](./img/000009.png)
- Do the same for the right half.
![sort](./img/000010.png)
- Merge the two sorted sublists back into one sorted list, compare each element of the two sublists and place the smaller element in the new list. This will be done until all elements are in the new sorted list.
![sort](./img/000011.png)
![sort](./img/000012.png)
- Repeat the process until the whole list is sorted.
![sort](./img/000013.png)



## Complexity
- Time Complexity: O(nlog(n))
- Space Complexity: O(n)
