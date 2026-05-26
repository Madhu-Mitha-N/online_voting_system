const form = document.getElementById("candidateForm");
const message = document.getElementById("message");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const data = {

        candidate_name: document.getElementById("name").value,

        party_name: document.getElementById("party_name").value,

        symbol: "",

        district: "",

        ward: ""
    };

    try {

        const res = await fetch("/candidate/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        if (res.ok) {

            message.style.color = "green";
            message.innerText = "Candidate Added Successfully";

            form.reset();

            // refresh list page automatically
            setTimeout(() => {
                window.location.href = "/admin/candidate-management";
            }, 800);

        } else {

            message.style.color = "red";
            message.innerText = result.error || "Error creating candidate";
        }

    } catch (err) {
        console.log(err);
        message.innerText = "Server error";
    }
});