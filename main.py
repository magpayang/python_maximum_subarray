
import MaximumSubArray

my_array = [-9,8,-7,6,-5,4,-3,2,-1,0]
my_array = [0,-9,8,-7,6,-5,4,-3,2,-1]
my_array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
my_array = [-1,-2,-3,-4,-5]
my_array = [-2, -5, 6, -2, -3, 1, 5, -6]
my_array = [0,-1,1,1,1]
my_array = [-1,1,2]
my_array = [0,-1,1,1]
my_array = [-2,1]


print(MaximumSubArray.MaximumSubarrayBrute(my_array))
start_idx, end_idx, sum = MaximumSubArray.MaximumSubarrayDivideandConquer(my_array, 0, len(my_array)-1)
print(my_array[start_idx:end_idx+1])
