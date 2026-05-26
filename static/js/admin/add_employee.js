const employeeForm =
document.getElementById("employeeForm");

const message =
document.getElementById("message");


employeeForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const employeeData = {

        employee_id:
        document.getElementById("employee_id").value,

        name:
        document.getElementById("name").value,

        email:
        document.getElementById("email").value
    };

    const response = await fetch(

        "/employee/create",

        {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(employeeData)
        }
    );

    const data = await response.json();

    if(response.ok){

        alert(`

Employee Created Successfully

Employee ID:
${employeeData.employee_id}

Default Password:
${data.default_password}

        `);

        window.location.href =
        "/admin/employee-management";

    }

    else{

        message.style.color = "red";

        message.innerText =
        data.error || "Something went wrong";
    }

});