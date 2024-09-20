 Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 You must write an algorithm with O(log n) runtime complexity.



 Example 1:

 Input: nums = [1,3,5,6], target = 5
 Output: 2
 Example 2:

 Input: nums = [1,3,5,6], target = 2
 Output: 1
 Example 3:

 Input: nums = [1,3,5,6], target = 7
 Output: 4

var searchInsert = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;
    let center;

    while (left < right) {
        center = Math.floor((left + right) / 2);

        if (nums[center] == target) {
            return center;
        } else if (nums[center] < target) {
            left = center + 1;
        } else {
            right = center - 1;
        }
    }
    center = Math.floor((left + right) / 2)
    return nums[center] >= target ? center : center + 1;
};