let points = document.getElementById("points")
let clickpoint = 5
let grandmaPrice = document.getElementById("grandmaPrice").innerText*1

function cookieClicked(){
    points.innerText = points.innerText*1+clickpoint
}

function buyGrandma(){
    if(points.innerText*1>=grandmaPrice){
        points.innerText*1-grandmaPrice
        clickpoint+=5
        grandmaPrice=grandmaPrice*1.2
        document.getElementById("grandmaPrice").innerText=grandmaPrice
    }else{
            alert("Nincs elég pénzed")
        }
    }