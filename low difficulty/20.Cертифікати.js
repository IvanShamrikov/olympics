process.stdin.on('data', function (data) {
    let n = String(data).replace(/(\r\n|\n|\r)/gm, " ").trim().split(' ');
    const M = Number(n[0]);
    const K = Number(n[1]);
    let result = K / M;
    if (result < 0.6) {
        result = "PARTICIPANT"
    } else if (result >= 0.6 && result < 0.74) {
        result = "VERY GOOD"
    } else if (result >= 0.74 && result < 0.9) {
        result = "EXCELLENT"
    } else {
        result = "OUTSTANDING"
    }
    console.log(result)
});
