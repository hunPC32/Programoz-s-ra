console.log("hello")

function greet(name="Hülyegyerek"){
    console.log("Hello "+name+"!")
}

function candrink(age){
    if(age>=18){
        return true
    }else{
        return false
    }
}

function korszamol(ev){
    return 2023-ev
}

function refreshAge(valaszto){
    let ev=korszamol(valaszto.value)
    document.getElementById('kor').innerText=ev

    if(candrink(ev)){
        document.body.style.backgroundColor="green"
    }else{
        document.body.style.backgroundColor="red"
    }
}


greet()
greet("dsjofdsjo")

console.log(candrink(16))
console.log(candrink(25))

console.log(candrink(korszamol(2008)))
console.log(candrink(korszamol(2000)))
console.log(korszamol(2008))
