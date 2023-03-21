let playground=document.getElementById("playground")
let cards=[
    "A","A",
    "B","B",
    "C","C",
    "D","D",
    "E","E",
    "F","F",
    "G","G",
    "H","H"
]

cards.sort(
    (a,b)=>{
        let rnd=Math.random()-0.5
        return rnd
    })

    function test(){
        let picked=document.getElementsByClassName("picked")
        picked=Array.from(picked)

        if(picked.length<2){
            return 0;
        }else{
            if(picked[0].innerHTML===picked[1].innerHTML){
            }else{
                picked[1].innerHTML=""
                picked[0].innerHTML=""
            }
            picked[0].classList.remove("picked")
            picked[1].classList.remove("picked")

        }
    }

for(let i=0; i<16; i++){
    let card=document.createElement("div")
    card.classList.add("card")
    card.onclick=()=>{
        card.innerHTML=cards[i]
        card.classList.add("picked")
        test()
    }
    playground.appendChild(card)
}
