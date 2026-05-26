const voterTableBody =
document.getElementById("voterTableBody");

const searchInput =
document.getElementById("searchInput");


// LOAD VOTERS

async function loadVoters() {

    try {

        const response =
        await fetch("/voter/all");

        const voters =
        await response.json();

        voterTableBody.innerHTML = "";

        voters.forEach(voter => {

            voterTableBody.innerHTML += `

                <tr>

                    <td>${voter.voter_id}</td>

                    <td>${voter.name}</td>

                    <td>${voter.phone}</td>

                    <td>${voter.district}</td>

                    <td>${voter.ward}</td>

                    <td>${voter.email}</td>

                    <td>

                        <button
                        class="delete-btn"
                        onclick="deleteVoter(${voter.voter_id})">

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


// DELETE VOTER

async function deleteVoter(voterId){

    const response = await fetch(

        `/voter/delete/${voterId}`,

        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);

    loadVoters();
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

        if(name.includes(value)){

            row.style.display = "";

        }

        else{

            row.style.display = "none";

        }

    });

});


// INITIAL LOAD

loadVoters();