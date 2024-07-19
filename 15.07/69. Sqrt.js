// Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

// You must not use any built-in exponent function or operator.

// For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


// Example 1:

// Input: x = 4
// Output: 2
// Explanation: The square root of 4 is 2, so we return 2.
// Example 2:

// Input: x = 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
var mySqrt = function (x) {
    let beg = 0, end = x, ans = 0;
    let iter = 0;

    while (beg <= end) {
        iter++;
        let mid = Math.floor((beg + end) / 2);

        if (mid * mid > x) {
            end = mid - 1;
        }

        else { // mid*mid <= x
            ans = mid;
            beg = mid + 1;
        }
    }
    console.log(iter)
    return ans;
};


mySqrt(100000000)

