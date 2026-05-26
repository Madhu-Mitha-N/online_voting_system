const voterForm = document.getElementById("voterForm");
const message = document.getElementById("message");

voterForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const voterData = {

        voter_id:
        document.getElementById("voter_id").value,

        name:
        document.getElementById("name").value,

        phone:
        document.getElementById("phone").value,

        dob:
        document.getElementById("dob").value,

        district:
        document.getElementById("district").value,

        ward:
        document.getElementById("ward").value,

        email:
        document.getElementById("email").value
    };

    const response = await fetch("/voter/create", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(voterData)
    });

    const data = await response.json();

    if(response.ok){

        message.style.color = "green";

        message.innerText =
        "Voter Registered Successfully";

        voterForm.reset();

    }else{

        message.style.color = "red";

        message.innerText = data.error;
    }

});
