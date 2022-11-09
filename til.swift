/*
2022.11.8 Today, I Learned
ABOUT Data Type
*/


let a = 3 //which means (I'll make "a" equals 3, it can't be changed)
var b = 3 //which means (I'll make "b" equals 3, it can be changed)

// so what we know about var and let, let is literally strong. so we can't change
// and var means variable so we can change the value.
// we can also explain the type next to the values(a,b)

let c: Int = 3
var d: Int = 53

// Int => Integer 

// To sum up, we can use (or have to use) "var" when we have to change the value or the value will likely to be changed.

let myname: String = "김은상"

// In String Type case, we can write whatever we wanted to say inside the "" 

let anyString: String = "12아무말34.fdgq"

let someFloat: Float = -12.333
let someDouble: Double = -13.1313133

// Double is more deliberate than Float

let someCharacter: Charater = "a"
// just one charater.

let someBool: Bool = true //or flase

//we have to use Capital letter at first to explain the type.




//we can change type

var intValue = 123
let stringValue = String(intValue) 