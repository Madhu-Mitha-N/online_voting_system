// CHECK LOGIN
// CHECK LOGIN
const admin = JSON.parse(localStorage.getItem("admin"));

if (!admin) {
    window.location.replace("/admin/login-page");
}

// SHOW ADMIN NAME
const adminNameEl = document.getElementById("adminName");
if (adminNameEl && admin) {
    adminNameEl.innerText = admin.admin_name;
}
// PREVENT BACK BUTTON ACCESS AFTER LOGOUT
window.history.pushState(null, "", window.location.href);
window.addEventListener("popstate", function () {
    window.history.pushState(null, "", window.location.href);
});
// LOGOUT
const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {

        localStorage.removeItem("admin");

        // redirect first
        window.location.replace("/admin/login-page");
    });
}
// LOAD DASHBOARD
async function loadDashboardData() {

    try {

        // VOTERS
        const voterResponse =
        await fetch("/voter/all");

        const voters =
        await voterResponse.json();

        document.getElementById(
            "totalVoters"
        ).innerText = voters.length;


        // CANDIDATES
        const candidateResponse =
        await fetch("/candidate/all");

        const candidates =
        await candidateResponse.json();

        document.getElementById(
            "totalCandidates"
        ).innerText = candidates.length;


        // EMPLOYEES
        const employeeResponse =
        await fetch("/employee/all");

        const employees =
        await employeeResponse.json();

        document.getElementById(
            "totalEmployees"
        ).innerText = employees.length;


        // VOTES
        const voteResponse =
        await fetch("/vote/all");

        const votes =
        await voteResponse.json();

        document.getElementById(
            "totalVotes"
        ).innerText = votes.length;


        // CANDIDATE RANKING
        const rankingTable =
        document.getElementById("rankingTable");

        rankingTable.innerHTML = "";

        candidates.forEach(candidate => {

            rankingTable.innerHTML += `

                <tr>

                    <td>
                        ${candidate.candidate_name}
                    </td>

                    <td>
                        ${candidate.party_name}
                    </td>

                    <td>
                        ${candidate.total_votes || 0}
                    </td>

                </tr>

            `;
        });

    }

    catch(error){

        console.log(error);

    }
}


loadDashboardData();


// AUTO REFRESH EVERY 3 SECONDS

setInterval(() => {

    loadDashboardData();

}, 3000);