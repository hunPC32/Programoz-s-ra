console.log("hello")

let a = 100
let b = "100"
let car = {
    brand: "Ferrari",
    type: "488",
    engine: {
        hp: 800,
        isRunning: false,
    },
    toggleMotor: function(){
        this.engine.isRunning = !this.engine.isRunning
    },
    showStatus: function(){
        let status = this.engine.isRunning ? "is running": "stopped"
        console.log(this.brand + " " + this.type + " ")
    }
}

let amIHungry=true

console.log(a)
console.log(b)

console.log(typeof(b))
console.log(typeof(a))

console.log(a-b)
console.log(a+b)

console.log(amIHungry)
console.log(typeof(amIHungry))

console.log(a===b)
console.log(a==b)