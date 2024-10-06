# Посміхайлики
#
# Під час олімпіади з програмування журі та оргкомітет полюбляють спостерігати за перебігом подій.
# Щоб було веселіше та цікавіше голова журі малює крейдою на дошці посміхайлики:
# - коли будь-хто з учасників олімпіади здає задачу на максимальний бал, голова журі малює на дошці такий посміхайлик: :-).
# - коли виявляється, що на дошці намальовано три посміхайлика :-), голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик ;-).
# - коли виявляється, що на дошці намальовано п'ять посміхайликів ;-), голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик «:-D».
# - коли виявляється, що на дошці намальовано сім посміхайликів :-D, голова журі стирає ці посміхайлики, а замість них малює такий посміхайлик «;-D».
# Ось так буде змінювати набір посміхайликів на дошці голова журі:
#
# Перше правильне рішення        :-)
# Друге правильне рішення        :-):-)
# Трете правильне рішення        :-):-):-)               голова журі стирає ці три посміхайлики,
#                                ;-)                    а замість них малює один ;-)
# Четверте правильне рішення     ;-):-)
# П'яте правильне рішення        ;-):-):-)
# Шосте правильне рішення        ;-):-):-):-)           голова журі стирає останні три посміхайлики,
#                                ;-);-)                 а замість них малює один ;-)
# Сьоме правильне рішення        ;-);-):-)
# Восьме правильне рішення       ;-);-):-):-)
# Дев'яте правильне рішення      ;-);-):-):-):-)            голова журі стирає останні три посміхайлики,
#                                ;-);-);-)              а замість них малює один ;-)
# Десяте правильне рішення       ;-);-);-):-)
# Одинадцяте правильне рішення   ;-);-);-):-):-)
# Дванадцяте правильне рішення   ;-);-);-):-):-):-)     голова журі стирає останні три посміхайлики,
#                                ;-);-);-);-)           а замість них малює один ;-)
# Тринадцяте правильне рішення   ;-);-);-);-):-)
# Чотирнадцяте правильне рішення ;-);-);-);-):-):-)
# П'ятнадцяте правильне рішення  ;-);-);-);-):-):-):-)  голова журі стирає останні три посміхайлики,
#                                ;-);-);-);-);-)        а замість них малює один ;-)
#                                :-D                    а потім п'ять посміхайликів ;-) заміняє на :-D
# ...  ...  ...   ...   ...   ...   ...   ...  ...   ...   ...  ...
# Сто сорокове правильне рішення ;-D:-D:-D;-):-):-)
#
# Напишіть програму, яка з'ясує, що буде намальовано на дошці голови журі після того, як буде здано N-те правильне рішення.
#
# У вхідних даних записано натуральне число N (1≤N≤32767).
#
# Виведіть, що буде намальовано на дошці голови журі після того, як буде здано N-те правильне рішення


N = int(input("N = "))
first = 0
second = 0
third = 0
fourth = 0

first = N
first_remaining = N%3
second = first//3
second_remaining = second%5
third = second//5
third_remaining = third%7
forth = third//7

firstSmile = ":-)"
secondSmile = ";-)"
thirdSmile = ":-D"
fourthSmile = ";-D"


print(fourthSmile * forth, thirdSmile * third_remaining, secondSmile * second_remaining, firstSmile * first_remaining)

#JS
#
# process.stdin.on('data', function (data) {
#     let n = parseInt(data, 10)
#     let first = 0;
#     let second = 0;
#     let third = 0;
#     let fourth = 0;
#     if (Math.floor(n / 3)) {
#         first = n % 3;
#         second = Math.floor(n / 3);
#         if (Math.floor(second / 5)) {
#             third = Math.floor(second / 5);
#             second = second % 5;
#             if (Math.floor(third / 7)) {
#                 fourth = Math.floor(third / 7);
#                 third = third % 7;
#             }
#         }
#
#     } else {
#         first = n;
#     }
#     const firstSmile = ":-)";
#     const secondSmile = ";-)";
#     const thirdSmile = ":-D";
#     const fourthSmile = ";-D";
#
#     const result = fourthSmile.repeat(fourth) + thirdSmile.repeat(third) + secondSmile.repeat(second) + firstSmile.repeat(first);
#     console.log(result)
#
# });
