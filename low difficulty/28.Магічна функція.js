process.stdin.on('data', function (data) {
    let arr = String(data).replace(/(\r\n|\n|\r)/gm, " ").trim();
    arr = arr.split(" ");
    const n = arr.shift();
    arr = arr.map(el => Number(el))
    const newArray = [];
    for (let i = 0; i < arr.length / n; i++) {
        newArray[i] = arr.slice(i * n, i * n + n)
    }
    let max = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i == j) continue
            const x = newArray[0][i] * newArray[1][j] + newArray[1][i] * newArray[0][j];
            if (x > max) max = x;
        }
    }
    console.log(max)
});

