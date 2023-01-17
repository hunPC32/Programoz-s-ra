let buttonholder=document.getElementById("buttonholder")

let letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

let word="BINHAM"

let mistake = 0

for(let i=0; i<letters.length; i++)(
buttonholder.innerHTML+='<button onclick="clicked(this)">'+letters[i]+' </button>'
)

for(let j=0; j<word.length; j++)(
    document.getElementById("status").innerText+="_"
)

function clicked(button){
    button.disabled=true

    let letter=button.innerText

    if(word.includes(letter)){
        let status=document.getElementById ("status").innerText

        let newstatus=""

        for(let i=0; i<word.length; i++){
            if(word[i]==letter){
                newstatus+=letter
            }else{
                newstatus+=status[i]
            }
        }

        document.getElementById ("status").innerText=newstatus

        if(newstatus==word){
            alert('Nyertél')
            buttonholder.innerHTML=""
        }

    }else{
        mistake++
        document.getElementById("imgholder").innerHTML=`<img src="${mistake}.png" width=30%>`

        if(mistake==10){
            buttonholder.innerHTML=""
            alert('Game over')
        }
    }
}