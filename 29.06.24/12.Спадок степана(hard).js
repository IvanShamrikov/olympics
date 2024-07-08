// D. Спадок Степана 
// Степан отримав у спадок від дідуся стоянку з N місць, пронумерованих від 1 до N. 
// Стоянка розбита на дві частини. Перші M місць знаходяться з лівого боку, а інші N - M місць з правого. 

// Кожного дня N жителів цього району паркують свої автомобілі на стоянці Степана. 
// Відомо, що перший житель приходить раніше усіх, потім другий, і так далі, тобто k-й приходить k-м. 
// Також для кожного жителя i відомо, скільки він буде платити, якщо його машину поставлять на j-е місце. 

// Степан придбав розподільник місць, який кожному автомобілю, що приїздить вказує, 
// на який бік паркуватись, після чого автомобіль паркується на мінімальне за номером вільне місце відповідного боку. 
// При цьому Степан вирішив зекономити і не придбав програмне забезпечення для розподільника, тому він працює не оптимально. 

// Степан просить Вас написати програму для цього розподільника, яка максимізує доходи Степана. 

// Формат вхідних даних: 
// у першому рядку записані два цілих числа N (2 ≤ N ≤ 1000) і M (1 ≤ M < N) – загальна кількість місць на стоянці і кількість місць з лівого боку відповідно. 
// У кожному із наступних N рядків записано по N цілих додатних чисел. j-е число i-го рядка означає, скільки буде платити i-ий житель за місце з номером j на цій стоянці. 
// Кожне з цих чисел не перевищує 106. 

// Формат вихідних даних: 
// єдиний рядок має містити одне число – максимальний прибуток стоянки. 

// Приклад вхідних і вихідних даних: 

// #EXAMPLE 1
// INPUT
// 2 1          
// 3 2 
// 6 4 

// OUTPUT
// 8 

// #EXAMPLE 2
// 4 1 
// 4 3 1 1 
// 3 1 1 1 
// 1 1 4 1 
// 1 1 1 2 

// OUTPUT
// 12


process.stdin.on('data', function (data) {
    let arr = String(data).replace(/(\r\n|\n|\r)/gm, " ").trim().split(' ').map(el => Number(el));
    const places = arr.shift();
    //місця справа і зліва
    const leftP = arr.shift();
    const rightP = places - leftP;

    // console.log("LEFT", leftP)
    //список цін
    const priceList = []
    for (let i = 0; i < arr.length / places; i++) {
        priceList[i] = arr.slice(i * places, i * places + places)
    }

    const leftSide = [];
    const rightSide = [];

    //ітеруємось по кожному місцю
    for (let i = 0; i < priceList.length; i++) {
        //знаходимо останнє вільне місце з кожної сторони
        const lastFreeLeft = leftSide.length;
        const lastFreeRight = rightSide.length;
        //якщо на одній з сторін закінчились місця

        if (lastFreeLeft == leftP) {
            rightSide.push(priceList[i][lastFreeRight + leftP]);
            continue;
        }
        if (lastFreeRight == rightP) {
            leftSide.push(priceList[i][lastFreeLeft]);
            continue;
        };

        //якщо останні житель

        if (i == priceList.length - 1) {

            if (priceList[i][lastFreeLeft] >= priceList[i][leftP + lastFreeRight]) {
                leftSide.push(priceList[i][lastFreeLeft]);
            }
            if (priceList[i][lastFreeLeft] < priceList[i][leftP + lastFreeRight]) {
                leftSide.push(priceList[i][leftP + lastFreeRight - 1]);
            }
            continue;
        }


        //знаходимо кількість претендентів на це місце
        const leftPretend = rightP - rightSide.length;
        const rightPretend = leftP - leftSide.length;
        //знаходимо максимальну ціну на це місце серед претендентів на ліве і відповідно на праве місце

        let maxLeft = maxPriceOnPlace(priceList, 0, lastFreeLeft, i + 1, i + leftPretend);
        let maxRight = maxPriceOnPlace(priceList, leftP, lastFreeRight, i + 1, i + rightPretend);

        //якщо вигідніше віддати місце майбутньому претенденту, повертаємо в протилежну сторону
        if (maxLeft + priceList[i][leftP + lastFreeRight] >= maxRight + priceList[i][lastFreeLeft]) {
            rightSide.push(priceList[i][leftP + lastFreeRight])
        } else {
            leftSide.push(priceList[i][lastFreeLeft])
        }
    }


    let sum1 = leftSide.reduce((cur, acc) => cur + acc, 0)
    let sum2 = rightSide.reduce((cur, acc) => cur + acc, 0)
    console.log("Result", leftSide, rightSide)

    console.log(sum1 + sum2)

});






function maxPriceOnPlace(priceList, offset, place, i1, i2) {
    let max = priceList[i1][offset + place];

    for (let i = i1; i <= (i2 <= priceList.length ? i2 : priceList.length); i++) {
        if (priceList[i][offset + place] > max) max = priceList[i][offset + place];
    }

    return max;
}