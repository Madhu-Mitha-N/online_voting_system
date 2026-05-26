const voter =
JSON.parse(localStorage.getItem("voter"));

if(!voter){

    window.location.href =
    "/voter/login-page";
}

const inputs = document.querySelectorAll(
    ".profile-form input"
);

const message =
document.getElementById("message");


// LOAD PROFILE

async function loadProfile(){

    const response = await fetch(
        `/voter/${voter.voter_id}`
    );

    const data = await response.json();

    document.getElementById(
        "profileName"
    ).innerText = data.name;

    document.getElementById(
        "name"
    ).value = data.name;

    document.getElementById(
        "email"
    ).value = data.email;

    document.getElementById(
        "phone"
    ).value = data.phone;

    document.getElementById(
        "district"
    ).value = data.district;

    document.getElementById(
        "ward"
    ).value = data.ward;
}

loadProfile();


// EDIT

document.getElementById(
    "editBtn"
).addEventListener("click", () => {

    inputs.forEach(input => {

        input.disabled = false;
    });
});


// SAVE

document.getElementById(
    "saveBtn"
).addEventListener("click", async () => {

    const response = await fetch(

        `/voter/profile/update/${voter.voter_id}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                name:
                document.getElementById("name").value,

                email:
                document.getElementById("email").value,

                phone:
                document.getElementById("phone").value,

                district:
                document.getElementById("district").value,

                ward:
                document.getElementById("ward").value
            })
        }
    );

    const data = await response.json();

    if(response.ok){

        message.style.color = "green";

        message.innerText =
        data.message;

        inputs.forEach(input => {

            input.disabled = true;
        });
    }
});


// CHANGE PASSWORD

document.getElementById(
    "changePasswordBtn"
).addEventListener("click", async () => {

    const response = await fetch(

        `/voter/change-password/${voter.voter_id}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                current_password:
                document.getElementById(
                    "currentPassword"
                ).value,

                new_password:
                document.getElementById(
                    "newPassword"
                ).value
            })
        }
    );

    const data = await response.json();

    if(response.ok){

        message.style.color = "green";

    }else{

        message.style.color = "red";
    }

    message.innerText = data.message || data.error;
});


// LOGOUT

document.getElementById(
    "logoutBtn"
).addEventListener("click", () => {

    localStorage.removeItem("voter");

    window.location.href =
    "/voter/login-page";
});