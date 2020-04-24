import math
def spilter (nums, mid) :
    big = [];
    small = [];
    for i in nums :
        if (i > mid) :
            big.append(i);
        else :
            small.append(i);
    return [big, small];

def quickSork (nums) : 
    if(len(nums) <= 1) :
        return nums;
    mid = nums.pop(math.floor(len(nums)/2));
    temp = spilter(nums, mid);
    big = temp[0];
    small = temp[1];
    return quickSork(small) + [mid] + quickSork(big);

nums = [5,3,2,6,7,9,1,4,10];
print(quickSork(nums));