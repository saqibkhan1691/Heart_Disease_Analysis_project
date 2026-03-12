// document.getElementById("simulateBtn").addEventListener("click", function () {

//     const selected = [];
//     document.querySelectorAll(".improve-check:checked")
//         .forEach(cb => selected.push(cb.value));

//     fetch("/predict", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({
//             selected_features: selected
//         })
//     })
//     .then(res => res.json())
//     .then(data => {

//         let current = data.current_probability;
//         let improved = data.improved_probability;
//         let reduction = (current - improved).toFixed(2);

//         // Update gauge text
//         document.getElementById("riskPercent").innerText = current + "%";
//         document.getElementById("riskLevel").innerText = data.risk_level;

//         // Update bars (scale height)
//         document.getElementById("currentBar").style.height = current * 2 + "px";
//         document.getElementById("improvedBar").style.height = improved * 2 + "px";

//         document.getElementById("reductionText").innerText =
//             "Risk reduced by " + reduction + "%";

//         document.getElementById("insightText").innerText =
//             "Improving " + selected.join(", ") +
//             " may reduce your heart disease risk.";
//     });

// });



document.getElementById("predictBtn").addEventListener("click", function () {

    const inputs = document.querySelectorAll(".feature-input")

    const data = {}

    inputs.forEach(input => {

        const feature = input.dataset.feature

        if (input.type === "checkbox") {

            data[feature] = input.checked ? 1 : 0

        } else {

            if (input.value !== "") {
                data[feature] = parseFloat(input.value)
            }

        }

    })


    fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(data)

    })
    .then(res => res.json())
    .then(result => {

        let current = result.probability
        let improved = result.improved_probability

        document.getElementById("riskPercent").innerText = current + "%"
        document.getElementById("riskLevel").innerText = result.category

        document.getElementById("currentBar").style.height = current * 2 + "px"
        document.getElementById("improvedBar").style.height = improved * 2 + "px"

        let reduction = (current - improved).toFixed(2)

        document.getElementById("reductionText").innerText =
            "Risk reduced by " + reduction + "%"

        document.getElementById("insightText").innerText =
            "Improving lifestyle factors may reduce heart disease risk."

    })

})