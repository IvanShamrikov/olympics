process.stdin.on('data', function (data) {
    let num = String(data).trim();
    if(!checkPalyndrome(num)){
        let p1 = changeChar(num, 0, num[2]);
        let p2 = changeChar(num, 2, num[0]);

        if(p1[0] == "0"){
            p1 = 0
        }
        if(p2[0] == "0"){
            p2 = 0
        }
        const sum = Number(p1) + Number(p2);
        console.log(sum)
    }else{
        let sum = 0;
        for(let i = 0; i<10; i++){
            if(i != num[1]){
                const p = changeChar(num, 1, i)
                sum+=Number(p);
            }
        }
        console.log(sum)
    }
    

});

function changeChar(s, i, char){
    const arr = s.split("");
    arr[i] = char;
    let newString = arr.join("");
    return newString;
}

function checkPalyndrome(s){
    if(s[0] == s[2]){
        return true;
    }else{
        return false;
    }

}
