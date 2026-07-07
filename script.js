async function predict() {

    let hours = Number(document.getElementById("hours").value);

    let attendance = Number(document.getElementById("attendance").value);

    let data = {

        Hours: hours,

        Attendance: attendance

    };

    let response = await fetch("http://127.0.0.1:8000/predict", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(data)

    });

    let result = await response.json();

    document.getElementById("result").innerHTML =
        "Prediction : " + result.prediction;

}