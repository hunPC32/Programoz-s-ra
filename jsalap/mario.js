let mario=document.getElementById("mario")

let marioX=200
let marioY=200

mario.style.top=marioY+"px"
mario.style.left=marioX+"px"

function up(){
    marioY=marioY-10
    mario.style.left=marioY+"px"
}
function down(){
    marioY=marioY+10
    mario.style.left=marioY+"px"
}

function left(){
    marioX=marioX-10
    mario.style.top=marioX+"px"
}
function right(){
    marioX=marioX+10
    mario.style.top=marioX+"px"
}