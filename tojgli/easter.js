let eggs=[]

document.title=0

function giveMeEgg(){
    let egg=document.createElement("div")
    egg.classList.add("egg")


    egg.onmouseenter=()=>{
        if(egg.classList.contains("rotten")){
            document.title=document.title*1-10
            egg.classList.remove("rotten")
        }
        document.title=document.title*1+1
        egg.style.left=Math.floor(Math.random()*window.innerWidth)+"px"
        egg.style.top=(Math.floor(Math.random()*1000)-1200)+"px"
        if(Math.random()*10<3){
            egg.classList.add("rotten")
        }
        
    }


    egg.style.left=Math.floor(Math.random()*window.innerWidth)+"px"
    egg.style.top=(Math.floor(Math.random()*1000)-1200)+"px"
    document.body.appendChild(egg)
    return egg
}

for(let i=0; i<50 ; i++){
    eggs.push(giveMeEgg())
}

setInterval(()=>{
    eggs.forEach((egg)=>{
        let newTop=egg.style.top.replace("px","")*1+5
        
        if(newTop>window.innerHeight+200){
            newTop=Math.floor(Math.random()*-500)
        }
        
        egg.style.top=newTop+"px"
    })
},20)