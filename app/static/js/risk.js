document.getElementById("simulateBtn").addEventListener("click", function () {

    const selected = [];
    document.querySelectorAll(".improve-check:checked")
        .forEach(cb => selected.push(cb.value));

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            selected_features: selected
        })
    })
    .then(res => res.json())
    .then(data => {

        let current = data.current_probability;
        let improved = data.improved_probability;
        let reduction = (current - improved).toFixed(2);

        // Update gauge text
        document.getElementById("riskPercent").innerText = current + "%";
        document.getElementById("riskLevel").innerText = data.risk_level;

        // Update bars (scale height)
        document.getElementById("currentBar").style.height = current * 2 + "px";
        document.getElementById("improvedBar").style.height = improved * 2 + "px";

        document.getElementById("reductionText").innerText =
            "Risk reduced by " + reduction + "%";

        document.getElementById("insightText").innerText =
            "Improving " + selected.join(", ") +
            " may reduce your heart disease risk.";
    });

});