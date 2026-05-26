const loginForm =
document.getElementById("loginForm");

const message =
document.getElementById("message");


loginForm.addEventListener("submit",

async (e) => {

    e.preventDefault();

    const voterData = {

        voter_id:
        document.getElementById("voter_id").value,

        password:
        document.getElementById("password").value
    };

    try{

        const response =
        await fetch("/voter/login", {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(voterData)
        });

        const data =
        await response.json();

        if (response.ok) {

    localStorage.setItem("voter", JSON.stringify(data.voter));

    message.style.color = "green";
    message.innerText = "Login Successful";

    setTimeout(() => {

        // FORCE PASSWORD CHANGE FLOW
        if (data.voter.is_default_password === 1) {
            window.location.href = "/voter/change-password";
        } else {
            window.location.href = "/voter/dashboard";
        }

    }, 1000);
}

        else{

            message.style.color = "red";

            message.innerText =
            data.error;
        }

    }

    catch(error){

        console.log(error);

        message.style.color = "red";

        message.innerText =
        "Something went wrong";
    }

});