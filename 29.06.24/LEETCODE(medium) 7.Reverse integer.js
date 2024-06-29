// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21


var reverse = function (x) {

    const number = x < 0 ? -x : x
    const length = number.toString().length;
    const new_number = [];
    for (let i = 0; i < length; i++) {
        if (i != length - 1) {
            new_number.push(Math.floor(number / Math.pow(10, i)) % 10); continue;
        } else {
            new_number.push(Math.floor(number / Math.pow(10, i)))
        }

    }
    const result = x < 0 ? -new_number.join("") : new_number.join("")
    if (Math.abs(result) > Math.pow(2, 31) - 1) return 0
    return result
};
