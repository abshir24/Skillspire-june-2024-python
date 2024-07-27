// Create a program that calculates the product off all of the numbers from 1 to 5 (1 * 2 * 3 * 4 * 5). 
// The final product for this program should be 120. (This does not have to be a function). 
// Hint: Use a for loop that starts from 1 to 5. Where are you going to save the product? ​

var total = 1

for(var counter = 1; counter <= 5 ; counter++){
    total *= counter
}

// console.log(total)


// Find the Average: Create a function that accepts an array as a parameter 
// and calculates the sum of all the numbers in the array. Afterwards return 
// that sum divided by the number of values in the array. Given [1,2,3,4,5], return sum/array.length​

function findAverage(array){
    var sum = 0

    for(var i = 0; i < array.length ;i++){
        sum += array[i]
    }

    var average = sum/array.length

    console.log(average)

    return average
}

// findAverage([1,2,3,4,5])

//Create a function that accepts an array of strings and returns a count of how may times 
//the word "skillspire" appears in the array. Given ["test","skillspire","test","skillspire"] 
//return 2 because "skillspire" appears twice in the array.

function skillspire(array){
    var count = 0

    for(var i = 0; i<array.length;i++){
        if(array[i] == "skillspire"){
            count+=1
        }
    }

    console.log(count)

    return count
}
// skillspire( ["test","skillspire","skillspire"] )




function sum(number1,number2){
    return number1 + number2
}

console.log( sum(1,2) )