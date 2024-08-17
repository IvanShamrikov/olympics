// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



// Example 1:

// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
// Example 2:

// Input: nums = [0,1]
// Output: [[0,1],[1,0]]
// Example 3:

// Input: nums = [1]
// Output: [[1]]

var permute = function (nums) {
    const result = [nums];
    for (let i = 0; i < nums.length; i++) {
        result.forEach(item => {
            for (let j = i + 1; j < nums.length; j++) {
                const arr = [...item];
                result.push(swap(arr, i, j))
            }
        })
    }
    console.log(result)

    return result
};


function swap(arr, i1, i2) {
    const temp = arr[i1];
    arr[i1] = arr[i2];
    arr[i2] = temp;
    return arr
}