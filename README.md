# LeetCodePython
DoLeet Code With Python

Do on Python 3.8

[1. Two Sum](src/TwoSum.py)

* 建立hashmap,num為key,index為value
* iter i for every element,and add nums[i] to hash map
* if target-nums[i]>0,find target-nums[i] in hashmap and return index

[9. Palindrome Number](src/PalindromeNumber.py)
* do not use string reverse
* if input number<0 return false
* else set a new num=0
* mod 10 get remainder
* let num*10+remainder
* if new num = num return true


[13. Roman to Integer](src/RomantoInteger.py)

* create roman_table
* convert roman to int array
* if left one smaller than right one which meaning subtraction
* if left one larger than right one meaning addition

[14. Longest Common Prefix](src/LongestCommonPrefix.py)

* due to prefix 
* sorted string list first
* get the first element do enumerate
* iter check value and add prefix

[20. Valid Parentheses](src/ValidParentheses.py)

* create bracket table
* iter every bracket
* add bracket '(' ,'[','{' to stack
* if get right bracket,pop
* if stack is empty Valid

[21. Merge Two Sorted Lists](src/MergeTwoSortedLists.py)

* add a new pointer to get head node
* compare l1,l2 two linkedlist
* if l1.val> l2.val,add l2 as next,else add l1 as next
* we can't know about length of two linkedlist,
* if l1 is none ,link l2 as next

[26. Remove Duplicates from Sorted Array](src/RemoveDuplicatesfromSortedArray.py)

* notice that nums has be sorted,just a non-decrease array
* set two pointer one for current,one for next
* iter array 
* if value of nums[currentIndex] not equal nums[nextIndex] find next element
* if different update next element with different value you found,and update currentIndex

[27. Remove Element](src/RemoveElement.py)

* judge will sort nums by k
* set two pointer,one for current begin from 0,one for tail Index
* if nums[current]==val ,replace value with tail element
* at the end of this,lastindex represent sorted Index

[28. Implement strStr](src/ImplementstrStr.py)

* slide windows?

[35. Search Insert Position](src/SearchInsertPosition.py)

* if target is the smallest in nums ,it will insert to begin,
* if target is the biggest in nums,it will insert at the tail
* use binary search to find insert position

[53. Maximum Subarray](src/MaximumSubarray.py)

[58. Length of Last Word](src/LengthofLastWord.py)

[66. Plus One](src/PlusOne.py)

[67. Add Binary](src/AddBinary.py)

[69. Sqrt(x)](src/Sqrt.py)