######################################################################
# HEAP USAGE
######################################################################

# In Python, we will use the heapq module
# Note: heapq only implements min heaps
import heapq 

# Declaration: heapq does not give you a heap data structure.
# You just use a normal list, and heapq provides you with
# methods that can be used on this list to perform heap operations
heap = []

# OR you can use the heapify method to convert a list to a heap
nums = [43, 2, 13, 634, 120]
heapq.heapify(nums)
heapq._heapify_max(nums)

# Add to heap
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

# Check minimum element
heap[0] # 1

# Pop minimum element
heapq.heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert a list to a heap in linear time
nums = [43, 2, 13, 634, 120]
heapq.heapify(nums)

# Now, you can use heappush and heappop on nums
# and nums[0] will always be the minimum element

# Note: Python's heapq implements a min heap

heap = [67, 341, 234, -67, 12, -976]
heapq.heapify(heap)

heapq.heappush(heap, 7451)
heapq.heappush(heap, -5352)

# The numbers will be printed in sorted order
while heap:
    print(heapq.heappop(heap))

######################################################################
# HEAP QUESTIONS
######################################################################

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

