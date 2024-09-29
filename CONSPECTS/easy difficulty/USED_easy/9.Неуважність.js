process.stdin.on('data', function (data) {
    let n = String(data).trim().split("");
    n = n.map(el => {
        if (el == el.toUpperCase()) {
            return el.toLowerCase()
        }
        if (el == el.toLowerCase()) {
            return el.toUpperCase()
        }
    })
    n = n.join("");
    console.log(n)
});
