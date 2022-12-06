let strenght = document.getElementById("strenght")

let agility = document.getElementById("agility")

let endurance = document.getElementById("endurance")

let luck = document.getElementById("luck")

let points = 10


function addStrenght(){
    if(points > 0){
    strenght.innerText = strenght.innerText*1 + 1
    points--
    document.getElementById("points").innerText = points*1

    document.getElementById("damage").innerText = strenght.innerText*1 + "-" + strenght.innerText*1.5
}
}

function addAgility(){
    if(points > 0){
    agility.innerText = agility.innerText*1 + 1
    points--
    document.getElementById("points").innerText = points*1
    document.getElementById("dodge").innerText = agility.innerText*1 + "-" + agility.innerText*1.5
}
}

function addEndurance(){
    if(points > 0){
    endurance.innerText = endurance.innerText*1 + 1
    points--
    document.getElementById("points").innerText = points*1
}
}

function addLuck(){
    if(points > 0){
    luck.innerText = luck.innerText*1 + 1
    points--
    document.getElementById("points").innerText = points
}
}