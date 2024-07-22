// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.



// Example 1:

// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Example 2:

// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
// Example 3:

// Input: nums = [], target = 0
// Output: [-1,-1]

var searchRange = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;
    let mid;
    let start, end;
    if (nums.length == 0) return [-1, -1];
    if (nums.length == 1) {
        if (nums[0] == target) {
            return [0, 0];
        } else {
            return [-1, -1]
        }
    }
    while (left <= right) {
        mid = Math.floor((left + right) / 2);
        if (nums[mid] == target) {
            start = mid;
            end = mid;
            while (nums[start] == target) {
                start--;
                if (start < 0 || nums[start] != target) {
                    start++;
                    break;
                }
            }
            while (nums[end] == target) {
                end++;
                if (end >= nums.length || nums[end] != target) {
                    end--;
                    break;
                }
            }

            break;
        }
        if (nums[mid] > target) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    console.log(start, end)

    if (start != undefined && end != undefined) return [start, end]
    return [-1, -1]
};