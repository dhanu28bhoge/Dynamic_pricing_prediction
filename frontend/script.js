// update slider value live
document.getElementById("price").oninput = function () {
    document.getElementById("priceValue").innerText = this.value;
};

function predictPrice() {

    let price = document.getElementById("price").value;
    let month = document.getElementById("month").value;
    let day = document.getElementById("day").value;

    fetch(`http://127.0.0.1:5000/predict?price=${price}&month=${month}&day=${day}`)
        .then(res => res.json())
        .then(data => {

            document.getElementById("demand").innerText =
                data.predicted_demand;

            document.getElementById("priceOutput").innerText =
                "₹ " + data.suggested_price;

            // 🔥 Smart insight
            let insight = "";

            if (data.predicted_demand > 50) {
                insight = "High demand detected. Consider increasing price.";
            } else if (data.predicted_demand < 20) {
                insight = "Low demand. Reduce price to attract customers.";
            } else {
                insight = "Stable demand. Maintain current pricing.";
            }

            document.getElementById("insight").innerText = insight;
        });
}
