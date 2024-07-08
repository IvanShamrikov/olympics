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