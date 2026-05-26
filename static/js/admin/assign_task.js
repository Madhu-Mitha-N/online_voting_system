const employeeSelect =
document.getElementById("employeeSelect");

const taskTableBody =
document.getElementById("taskTableBody");


// LOAD EMPLOYEES

async function loadEmployees(){

    const res =
    await fetch("/employee/all");

    const employees =
    await res.json();

    employees.forEach(emp => {

        employeeSelect.innerHTML += `

            <option value="${emp.employee_id}">

                ${emp.name}

            </option>

        `;
    });
}


// ASSIGN TASK

document.getElementById("assignBtn")
.addEventListener("click", async () => {

    const task_name =
    document.getElementById("taskName").value;

    const employee_id =
    employeeSelect.value;

    if(!task_name || !employee_id){

        alert("Fill all fields");
        return;
    }

    await fetch("/task/assign", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            task_name,
            employee_id
        })
    });

    document.getElementById("taskName").value = "";

    loadTasks();
});


// LOAD TASKS

async function loadTasks(){

    const res =
    await fetch("/task/all");

    const tasks =
    await res.json();

    taskTableBody.innerHTML = "";

    tasks.forEach(task => {

        taskTableBody.innerHTML += `

            <tr>

                <td>${task.task_id}</td>

                <td>${task.task_name}</td>

                <td>${task.employee_name}</td>

                <td>

                    <select
                    class="status-select"
                    onchange="updateStatus(
                    ${task.task_id},
                    this.value
                    )">

                        <option
                        ${task.status === "Pending" ? "selected" : ""}>
                        Pending
                        </option>

                        <option
                        ${task.status === "Completed" ? "selected" : ""}>
                        Completed
                        </option>

                    </select>

                </td>

                <td>

                    <button
                    class="delete-btn"
                    onclick="deleteTask(${task.task_id})">

                    Delete

                    </button>

                </td>

            </tr>

        `;
    });
}


// UPDATE STATUS

async function updateStatus(id, status){

    await fetch(`/task/update/${id}`, {

        method:"PUT",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            status
        })
    });

    loadTasks();
}


// DELETE

async function deleteTask(id){

    await fetch(`/task/delete/${id}`, {

        method:"DELETE"
    });

    loadTasks();
}


loadEmployees();
loadTasks();