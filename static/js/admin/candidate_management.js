const candidateTableBody =
document.getElementById("candidateTableBody");

const searchInput =
document.getElementById("searchInput");


// LOAD CANDIDATES
async function loadCandidates() {

    try {

        const res = await fetch("/candidate/all");
        const candidates = await res.json();

        candidateTableBody.innerHTML = "";

        candidates.forEach(c => {

            candidateTableBody.innerHTML += `

                <tr>

                    <td>${c.candidate_id}</td>
                    <td>${c.candidate_name}</td>
                    <td>${c.party_name}</td>
                    <td>${c.total_votes}</td>

                    <td>
                        <button class="delete-btn"
                        onclick="deleteCandidate(${c.candidate_id})">
                            Delete
                        </button>
                    </td>

                </tr>

            `;
        });

    } catch (err) {
        console.log(err);
    }
}


// DELETE
async function deleteCandidate(id) {

    await fetch(`/candidate/delete/${id}`, {
        method: "DELETE"
    });

    loadCandidates();
}


// SEARCH
searchInput.addEventListener("keyup", () => {

    const value = searchInput.value.toLowerCase();

    document.querySelectorAll("tbody tr").forEach(row => {

        const name =
        row.children[1].textContent.toLowerCase();

        row.style.display =
        name.includes(value) ? "" : "none";
    });

});

loadCandidates();