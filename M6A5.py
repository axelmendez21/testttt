# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 5

def comp_avg(*nums):
    avg = 0
    for num in nums:
        avg = avg + num
    return avg/len(nums)
def comp_max(*nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max
def comp_min(*nums):
    max = nums[0]
    for num in nums:
        if max > num:
            max = num
    return max

