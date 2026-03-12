document.getElementById("predictBtn").addEventListener("click", function(){

const inputs = document.querySelectorAll(".feature-input")

const data = {}

inputs.forEach(input => {

const feature = input.dataset.feature

if(input.type === "checkbox"){

data[feature] = input.checked ? 1 : 0

}

else{

if(input.value !== "")
data[feature] = parseFloat(input.value)

}

})


fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})

.then(res=>res.json())

.then(result=>{

let current = result.probability
let improved = result.improved_probability

document.getElementById("riskPercent").innerText = current + "%"
document.getElementById("riskLevel").innerText = result.category

document.getElementById("currentBar").style.height = current*2 + "px"
document.getElementById("improvedBar").style.height = improved*2 + "px"

document.getElementById("currentPercent").innerText = current + "%"
document.getElementById("improvedPercent").innerText = improved + "%"

let reduction = (current-improved).toFixed(2)

document.getElementById("reductionText").innerText =
"Risk reduced by "+reduction+"%"


let html="<ul>"

result.suggestions.forEach(s=>{
html+="<li>"+s+"</li>"
})

html+="</ul>"

document.getElementById("insightText").innerHTML=html

})

})