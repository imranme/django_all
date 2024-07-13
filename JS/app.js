// console.log("hello tushar")

// var lastName = "Tushar Imran";

// console.log(typeof lastName); // typeof tag use see what type of variabel

// var num1 = 70.78;
// var num2 = 70;
// var result = num1 + num2;

// console.log(parseInt(result));  

// var num = 100;

// if(num>= 100){
//     console.log("ami borolox");
// } else{
//     console.log("ami goribs");  // if-else stetment 
// }

// Object 

// var person = {
//     hands: 2,
//     friends:5,
//     age:  12,
//     collage: {
//         name: "magura collage",
//         location: "magura"
//     },
// };

// console.log(person.collage.name);

//   Array 5-7


// var friends = ["rahim", "korim", "jobbar"];

// // friends.pop()
// // friends.unshift("salam");
// friends.shift()
// console.log(friends)

// loop 

// problem solving 

// var num = 2;

// if (num % 2 == 0){
//     console.log("this is even number");
// }
// else{
//     console.log("this is odd number");
// }


// var nums = [2, 3, 5, 4,7,6, 9,1,11,10];

// console.log(
//     nums.sort(function (a,b){
//         return a-b;
//     })
// );

20

var Arr = [1, 7, 2, 8, 3, 4, 5, 0, 9];

for (var i = 1; i < Arr.length; i++)
    for (var j = 0; j < i; j++)
        if (Arr[i] < Arr[j]) {
            var x = Arr[i];
            Arr[i] = Arr[j];
            Arr[j] = x;
        }

console.log(Arr);