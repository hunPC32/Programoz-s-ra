let playerChoice=document.getElementById('player-choice')
let enemyChoice=document.getElementById('enemy-choice')

let choiceBtns=document.getElementsByClassName('choicebtn')

for(let i=0; i<choiceBtns.length; i++){
    choiceBtns[i].onClick=()=>{
        alert(choiceBtns[i].id)
    }
}