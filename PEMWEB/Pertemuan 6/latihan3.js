//Control Flow
//If Else
let age = 20;
if (age >= 18) {
    console.log("You Are Eligible To Vote.");
} else {
    console.log("You Are Not Eligible TO Vote.");
}
//Ternary Operator
let vote = 
age >= 20 ? "You're Eligible to Vote" : "You're not eligible to vote";
console.log(vote);

let hours = new Date().getHours();
let discount = hours <= 1 ? "20%"
                : hours <= 3 ? "15%"
                : "0%";
console.log(discount);

//switch
let day = new Date().getDay();
switch (day) {
    case 0:
        console.log("Sunday");
        break;
    case 1:
        console.log("Monday")
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        consol.log("Wednesday")
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    default:
        console.log("Invalid Day")
}