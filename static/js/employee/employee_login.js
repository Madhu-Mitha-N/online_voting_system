const form =
document.getElementById("employeeLoginForm");

const message =
document.getElementById("message");


form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const loginData = {

        email:
        document.getElementById("email").value,

        password:
        document.getElementById("password").value
    };

    const response = await fetch("/employee/login", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(loginData)
    });

    const data = await response.json();

    if(response.ok){

        localStorage.setItem(
            "employee",
            JSON.stringify(data.employee)
        );

        window.location.href =
        "/employee/dashboard";

    }else{

        message.style.color = "red";

        message.innerText = data.error;
    }

});