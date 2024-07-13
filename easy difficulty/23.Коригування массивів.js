
process.stdin.on('data', function (data) {
    let input = String(data).replace(/(\r\n|\n|\r)/gm, " ").trim().split(' ')

    const length = input.shift();
    let sorted = "YES";
    input = input.map(el=>Number(el))


    let prev = -100000;
    for(let i = 0; i<length-1; i++){
        // console.log(prev, input[i], input[i+1])

        if( input[i] >= input[i+1]  ){
            // console.log(prev, input[i], input[i+1])
            if(-input[i]<=input[i+1] && -input[i]>=prev){
                input[i] = -input[i];
                prev = input[i]
            }else if(input[i]<=-input[i+1]){
                input[i+1] =-input[i+1];
                prev = input[i]
            }
            else{
                if(input[i] != input[i+1]){
                    sorted = "NO"
                    break;
                }
            }
            prev = input[i];

        }
        prev = input[i]
    }
    if(sorted === "YES"){
        console.log(sorted);
        console.log(input.join(" "))
    }else{
        console.log(sorted);
        // console.log(input.join(" "))
    }
});

10 -5 -6  6 -6