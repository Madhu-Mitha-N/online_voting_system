const form =
    document.getElementById("adminCreateForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const admin_name =
        document.getElementById("admin_name").value;

    const password =
        document.getElementById("password").value;

    const confirm_password =
        document.getElementById("confirm_password").value;

    const message =
        document.getElementById("message");


    // VALIDATION

    if(
        !admin_name ||
        !password ||
        !confirm_password
    ){

        message.style.color = "red";

        message.innerText =
            "All fields are required";

        return;
    }


    if(password !== confirm_password){

        message.style.color = "red";

        message.innerText =
            "Passwords do not match";

        return;
    }


    if(password.length < 6){

        message.style.color = "red";

        message.innerText =
            "Password must contain minimum 6 characters";

        return;
    }


    try{

        const response = await fetch(
            "http://127.0.0.1:5000/admin/create",
            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    admin_name,
                    password
                })
            }
        );

        const data = await response.json();

        if(response.ok){

            message.style.color = "green";

            message.innerText =
                data.message;


            setTimeout(() => {

                window.location.href =
                    "/admin/login-page";

            }, 1000);

        }else{

            message.style.color = "red";

            message.innerText =
                data.error || "Creation Failed";
        }

    }catch(error){

        message.style.color = "red";

        message.innerText =
            "Server Error";
    }

});