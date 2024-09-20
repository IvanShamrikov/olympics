// Given an m x n matrix, return all elements of the matrix in spiral order.

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]
var spiralOrder = function (matrix) {
    const n = matrix.length;
    const m = matrix[0].length;
    const length = n * m;
    let l = 0;
    const arr = [];
    let offset = 0;
    let i = 0;
    let j = 0;
    while (l < length) {

        while (j < m - offset && l < length) {
            arr.push(matrix[i][j]);
            j++;
            l++;
        }
        j--
        i++

        while (i < n - offset && l < length) {
            arr.push(matrix[i][j]);
            i++;
            l++;
        }
        i--
        j--
        while (j >= offset && l < length) {
            arr.push(matrix[i][j]);
            j--;
            l++;
        }
        j++
        i--
        offset++;

        while (i >= offset && l < length) {
            arr.push(matrix[i][j]);
            i--;
            l++;
        }
        i++
        j++

    }
    return arr
};