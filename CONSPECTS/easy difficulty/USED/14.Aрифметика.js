process.stdin.on('data', function (data) {
    //обов'язково зчитуємо string
    let n = String(data).trim()

    //Розбиваємо на массив по 1 числу
    const stringArray = String(n).split("")
    let result = []
    //В новий масив записуємо уникальні значення
    stringArray.forEach(element => {
        ы
        if (!result.includes(element)) {
            result.push(element)
        }
    })
    //Виводимо довжину массиву
    console.log(result.length);
});
