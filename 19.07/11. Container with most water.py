var maxArea = function (height) {
    const length = height.length;
    let left = 0;
    let right = length - 1;
    let max = 0;
    let w, h, size;
    while (left < right) {
        w = right - left;
        h = Math.min(height[left], height[right]);
        size = w * h;
        if (size > max) max = size;
        if (height[right] < height[left]) {
            while (left < right && height[right] <= h) right--;
        } else {
            while (left < right && height[left] <= h) left++;
        }
    }
    console.log(max)
    return max
};