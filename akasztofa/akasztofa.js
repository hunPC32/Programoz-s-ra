let buttonholder=document.getElementById("buttonholder")

let letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

let word="binham"

for(let i=0; i<letters.length; i++)(
buttonholder.innerHTML+='<button onclick="clicked(this)">'+letters[i]+' </button>'
)

for(let j=0; j<word.length; j++)(
    document.getElementById("status").innerText+="_"
)

function clicked(button){
    button.disabled=true

    let letter=button.innerText

    if(word.includes(letter))
        alert("benne van")

    else(
        alert("nincs benne")
    )
}