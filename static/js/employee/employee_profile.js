const employee =
JSON.parse(localStorage.getItem("employee"));

if(!employee){

    window.location.href =
    "/employee/login-page";
}

const inputs = document.querySelectorAll(
    ".profile-form input"
);

const message =
document.getElementById("message");


// LOAD PROFILE

async function loadProfile(){

    const response = await fetch(
        "/employee/all"
    );

    const employees =
    await response.json();

    const data =
    employees.find(

        e =>
        e.employee_id ==
        employee.employee_id
    );

    document.getElementById(
        "profileName"
    ).innerText = data.name;

    document.getElementById(
        "name"
    ).value = data.name;

    document.getElementById(
        "email"
    ).value = data.email;
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

        `/employee/profile/update/${employee.employee_id}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                name:
                document.getElementById("name").value,

                email:
                document.getElementById("email").value
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

        `/employee/change-password/${employee.employee_id}`,

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

    message.innerText =
    data.message || data.error;
});


// LOGOUT

document.getElementById(
    "logoutBtn"
).addEventListener("click", () => {

    localStorage.removeItem("employee");

    window.location.href =
    "/employee/login-page";
});