Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false



var isValid = function (s) {
    let i = 0;
    if (i % 2 != 0) return false;

    const validation = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    const stack = [];
    for (const c of s) {
        if (Object.values(validation).includes(c)) {
            stack.push(c)
        } else if (validation.hasOwnProperty(c)) {
            if (!stack.length || validation[c] !== stack.pop()) {
                return false;
            }
        }
    }

    return !stack.length;

};