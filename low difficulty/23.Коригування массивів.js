process.stdin.on('data', function (data) {
    let input = String(data).replace(/(\r\n|\n|\r)/gm, " ").trim().split(' ')

    const length = input.shift();
    let prev = input[0];
    let sorted = "YES";
    input = input.map(el => Number(el))
    for (let i = 1; i < length; i++) {
        if (input[i] <= prev) {

            if (-prev <= input[i]) {
                input[i - 1] = -prev;

            } else if (-input[i] >= prev) {
                input[i] = -input[i];

            } else {
                sorted = "NO"
            }
            prev = input[i];

        }
    }
    console.log(sorted);
    console.log(input.join(" "))

});
