const voter =
JSON.parse(localStorage.getItem("voter"));


// PROTECT PAGE

if(!voter){

    window.location.href =
    "/voter/login-page";
}


const form =
document.getElementById("changePasswordForm");

const message =
document.getElementById("message");


form.addEventListener("submit",

async (e) => {

    e.preventDefault();

    const newPassword =
    document.getElementById("newPassword").value;

    try{

        const response =
        await fetch(

            `/voter/change-password/${voter.voter_id}`,

            {

                method:"PUT",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    new_password:newPassword
                })
            }
        );

        const data =
        await response.json();

        if(response.ok){

            message.style.color = "green";

            message.innerText =
            "Password Changed Successfully";

            // UPDATE LOCAL STORAGE

            voter.is_default_password = 0;

            localStorage.setItem(
                "voter",
                JSON.stringify(voter)
            );

            setTimeout(() => {

                window.location.href =
                "/voter/dashboard";

            }, 1500);

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