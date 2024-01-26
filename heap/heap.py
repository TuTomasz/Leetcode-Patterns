
# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Pseudocode:

# 1. Initialize a max heap
# 2. Iterate through the array
# 3. Push the current element to the heap
# 4. If the size of the heap is greater than k, then pop from the heap
# 5. Return the top element of the heap

def findKthLargest(nums, k):
    
    import heapq

    heapq._heapify_max(nums)

    for i in range(k-1):
        
        heapq._heappop_max(nums)

    return heapq._heappop_max(nums)

