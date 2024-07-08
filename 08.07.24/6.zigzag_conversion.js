// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number of rows:

// string convert(string s, int numRows);

// Example 1:

// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
// Example 2:

// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I



/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    let arr = [];
    for (let i = 0; i < numRows; i++) {
        arr[i] = [];
    }
    let i = 0;
    let t = 0;
    if (numRows <= 1) return s
    while (s[t]) {
        if (i % (numRows - 1) == 0) {
            for (let j = 0; j < numRows; j++) {
                arr[j][i] = s[t];
                t++;
            }
        } else {
            if (arr[numRows - 1 - i % (numRows - 1)]) arr[numRows - 1 - i % (numRows - 1)][i] = s[t];
            t++
        }
        i++;
    }
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            arr[i][j] && result.push(arr[i][j])
        }
    }
    result = result.join("");
    return result;

};