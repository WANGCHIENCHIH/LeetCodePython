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
