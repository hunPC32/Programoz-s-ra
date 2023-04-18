let sides = document.getElementById("sides")
let result = document.getElementById("result")
let rollnumber = document.getElementById("rollnumber")

function random(sidesNum){
    let rnd = Math.floor(Math.random()*sidesNum)+1
    return rnd
}

function roll(){
    let rollNum = rollnumber.value*1
    let sidesNum = sides.value*1
   
    result.innerText = ""

    for(let i = 0; i<rollNum; i++){
        result.innerText += random(sidesNum)+","
    }
}