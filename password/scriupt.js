const pwdEl = document.getElementById("password")
const lengthNumEl = document.getElementById("lengthnum")
const sliderEl = document.getElementById("length")

const checkboxes = {
    upper: document.getElementById("checkboxxup"),
    lower: document.getElementById("checkboxxlow"),
    nums: document.getElementById("checkboxxnum"),
    symbols: document.getElementById("checkboxxsymbol"),
}

const genBtn = document.getElementById("generatebtn")


updateNum()
function updateNum(){
    lengthNumEl.innerText = sliderEl.value
}

sliderEl.addEventListener("input", updateNum)

generatePwd()
function generatePwd(){
    const letters = "abcdefghijklmnopqrstuqvwxyz"
    const upper = letters.toUpperCase()
    const numbers = "0123456789"
    const symbols = "§+!%/=()~ˇ^˘°˛`˙´˝¨×÷¤ß$ŁłíĐđ<>#&@{}<;>*"

    let charBank = ""

    if(checkboxes.lower.checked){charBank += letters;}
    if(checkboxes.upper.checked){charBank += upper;}
    if(checkboxes.nums.checked){charBank += numbers;}
    if(checkboxes.symbols.checked){charBank += symbols;}

    console.log(charBank);

    let li = charBank.split("")
    li.sort(()=> 0.5 - Math.random());
    for(let i = 0; i < (sliderEl.value*1); i++){
        res += li[i]
    }
    pwdEl.innerText(generatePwd)

}

genBtn.addEventListener("click", generatePwd)
