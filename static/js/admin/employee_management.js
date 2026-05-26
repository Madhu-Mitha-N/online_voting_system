const employeeTableBody =
document.getElementById("employeeTableBody");

const searchInput =
document.getElementById("searchInput");


// LOAD EMPLOYEES

async function loadEmployees() {

    try {

        const response =
        await fetch("/employee/all");

        const employees =
        await response.json();

        employeeTableBody.innerHTML = "";

        employees.forEach(emp => {

            employeeTableBody.innerHTML += `

                <tr>

                    <td>${emp.employee_id}</td>

                    <td>${emp.name}</td>

                    <td>${emp.email}</td>

                    <td>
                        Pending
                    </td>

                    <td>

                        <button
                        class="delete-btn"
                        onclick="deleteEmployee(${emp.employee_id})">

                            Delete

                        </button>

                    </td>

                </tr>

            `;
        });

    }

    catch(error){

        console.log(error);

    }
}


// DELETE

async function deleteEmployee(employeeId){

    await fetch(

        `/employee/delete/${employeeId}`,

        {
            method:"DELETE"
        }

    );

    loadEmployees();
}


// SEARCH

searchInput.addEventListener("keyup", () => {

    const value =
    searchInput.value.toLowerCase();

    const rows =
    document.querySelectorAll("tbody tr");

    rows.forEach(row => {

        const name =
        row.children[1]
        .textContent
        .toLowerCase();

        row.style.display =
        name.includes(value)
        ? ""
        : "none";

    });

});


loadEmployees();