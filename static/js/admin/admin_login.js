const form =
    document.getElementById("adminLoginForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const admin_name =
        document.getElementById("admin_name").value;

    const password =
        document.getElementById("password").value;

    const message =
        document.getElementById("message");


    // VALIDATION

    if(!admin_name || !password){

        message.style.color = "red";

        message.innerText =
            "All fields are required";

        return;
    }

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/admin/login",
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
                "Login Successful";


            // STORE ADMIN

            localStorage.setItem("admin", JSON.stringify(data.admin));
window.location.href = "/admin/dashboard";


            // REDIRECT DASHBOARD

            setTimeout(() => {

                window.location.href =
                    "/admin/dashboard";

            }, 1000);

        }else{

            message.style.color = "red";

            message.innerText =
                data.error || "Login Failed";
        }

    }catch(error){

        message.style.color = "red";

        message.innerText =
            "Server Error";
    }

});