const employee = JSON.parse(localStorage.getItem("employee"));

if (!employee) {
    window.location.replace("/employee/login-page");
}

document.getElementById("employeeName")
.innerText = employee.name;


// LOGOUT

document.getElementById("logoutBtn")
.addEventListener("click", () => {

    localStorage.removeItem("employee");

   // prevent back button access
window.history.pushState(null, "", window.location.href);

window.onpopstate = function () {
    window.history.pushState(null, "", window.location.href);
};
});


// LOAD TASKS

async function loadTasks(){

    const response = await fetch(

        `/employee/tasks/${employee.employee_id}`

    );

    const tasks = await response.json();

    const taskTableBody =
    document.getElementById("taskTableBody");

    taskTableBody.innerHTML = "";

    tasks.forEach(task => {

        taskTableBody.innerHTML += `

            <tr>

                <td>${task.task_id}</td>

                <td>${task.task_name}</td>

                <td>${task.status}</td>

                <td>

                    ${
                        task.status === "Completed"

                        ?

                        "Done"

                        :

                        `<button
                        class="complete-btn"
                        onclick="completeTask(${task.task_id})">

                            Mark Complete

                        </button>`
                    }

                </td>

            </tr>

        `;
    });
}


// COMPLETE TASK

async function completeTask(taskId){

    await fetch(

        `/employee/task/update/${taskId}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                status:"Completed"
            })
        }
    );

    loadTasks();
}


// AUTO REFRESH

setInterval(() => {

    loadTasks();

}, 3000);


loadTasks();