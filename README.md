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

[70. Climbing Stairs](src/ClimbingStairs.py)

* think stage 1 =1 situation ([1]),stage 2 =2 situations ([1,1] or [2])
* find and check if stage 3 equal stage 1 add stage 2
* [1,1,1],[2,1],[1,2]
* check stage 4 equal stage 3 add stage2
* [1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2]
* induction
* ->stage(n)=stage(n-1)+stage(n-2)


[83. Remove Duplicates from Sorted List](src/RemoveDuplicatesfromSortedList.py)

[88. Merge Sorted Array](src/MergeSortedArray.py)

* use three pointer nums1_p,,nums2_p,current,
* current is the tail index of nums1
* compare value of nums1,nums2 by pointer nums1_p,nums2_p
* choose the bigger one insert to current
* update current,and bigger one 's index

[94. Binary Tree Inorder Traversal](src/BinaryTreeInorderTraversal.py)

* left leaf->root ->right leaf

[100. Same Tree](src/SameTree.py)

[101. Symmetric Tree](src/SymmetricTree.py)

[104. Maximum Depth of Binary Tree](src/MaximumDepthofBinaryTree.py)

[108. Convert Sorted Array to Binary Search Tree](src/ConvertSortedArraytoBinarySearchTree.py)

[110. Balanced Binary Tree](src/BalancedBinaryTree.py)

[111. Minimum Depth of Binary Tree](src/MinimumDepthofBinaryTree.py)

[112. Path Sum](src/PathSum.py)

* if not left ,root,right ,target sum - root node value

[118. Pascal's Triangle](src/PascalsTriangle.py)

[119. Pascal's Triangle II](src/PascalsTriangleII.py)

[121. Best Time to Buy and Sell Stock](src/BestTimetoBuyandSellStock.py)

[125. Valid Palindrome](src/ValidPalindrome.py)

[136. Single Number](src/SingleNumber.py)

[141. Linked List Cycle](src/LinkedListCycle.py)

[144. Binary Tree Preorder Traversal](src/BinaryTreePreorderTraversal.py)

* root-> left leaf ->right leaf

[145. Binary Tree Postorder Traversal](src/BinaryTreePostorderTraversal.py)

* left leaf ->right leaf->root

[155. Min Stack](src/MinStack.py)

[160. Intersection of Two Linked Lists](src/IntersectionofTwoLinkedLists.py)

[169. Majority Element](src/MajorityElement.py)

[171. Excel Sheet Column Number](src/ExcelSheetColumnNumber.py)

[190. Reverse Bits](src/ReverseBits.py)

[191. Number of 1 Bits](src/Numberof1Bits.py)

[202. Happy Number](src/HappyNumber.py)

[203. Remove Linked List Elements](src/RemoveLinkedListElements.py)

[205. Isomorphic Strings](src/IsomorphicStrings.py)

[206. Reverse Linked List](src/ReverseLinkedList.py)

[217. Contains Duplicate](src/ContainsDuplicate.py)

[219. Contains Duplicate II](src/ContainsDuplicateII.py)

[225. Implement Stack using Queues]()

[226. Invert Binary Tree]()

[228. Summary Ranges]()

[231. Power of Two]()

[232. Implement Queue using Stacks]()

[234. Palindrome Linked List]()

[235. Lowest Common Ancestor of a Binary Search Tree]()

[237. Delete Node in a Linked List]()

[242. Valid Anagram]()

[257. Binary Tree Paths]()

[258. Add Digits]()

[263. Ugly Number]()

[268. Missing Number]()

[278. First Bad Version]()

---------

A lonely programer, 
Could you buy me a cup of coffee, if you don't mind.

```
ETH:0x7743c5f84926ee8ec469562c8e2c64436c8b9ebe
``` 

```
USDT:0x7743c5f84926ee8ec469562c8e2
```