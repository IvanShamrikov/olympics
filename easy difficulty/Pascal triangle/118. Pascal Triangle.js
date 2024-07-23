 Given an integer numRows, return the first numRows of Pascal's triangle.
 In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 Example 1:
 Input: numRows = 5
 Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

 Example 2:
 Input: numRows = 1
 Output: [[1]]

var generate = function (numRows) {
    const arr = [];
    for (let i = 0; i < numRows; i++) {
        const newRow = [];
        for (let j = 0; j <= i; j++) {
            if (j == 0 || j == i) {
                newRow.push(1)
            } else {
                const number = arr[i - 1][j] + arr[i - 1][j - 1];
                newRow.push(number)
            }
        }
        arr.push(newRow)
    }
    return arr;
};