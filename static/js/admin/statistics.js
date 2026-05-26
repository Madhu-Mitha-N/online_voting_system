async function loadStatistics(){

    // VOTERS

    const voterRes =
    await fetch("/voter/all");

    const voters =
    await voterRes.json();

    document.getElementById(
        "totalVoters"
    ).innerText = voters.length;


    // CANDIDATES

    const candidateRes =
    await fetch("/candidate/all");

    const candidates =
    await candidateRes.json();

    document.getElementById(
        "totalCandidates"
    ).innerText = candidates.length;


    // EMPLOYEES

    const employeeRes =
    await fetch("/employee/all");

    const employees =
    await employeeRes.json();

    document.getElementById(
        "totalEmployees"
    ).innerText = employees.length;


    // TOTAL VOTES

    let totalVotes = 0;

    candidates.forEach(c => {

        totalVotes += c.total_votes || 0;

    });

    document.getElementById(
        "totalVotes"
    ).innerText = totalVotes;


    // RANKING TABLE

    const rankingTable =
    document.getElementById("rankingTable");

    rankingTable.innerHTML = "";

    candidates
    .sort((a,b)=>
    b.total_votes - a.total_votes)

    .forEach(c => {

        rankingTable.innerHTML += `

            <tr>

                <td>${c.candidate_name}</td>

                <td>${c.party_name}</td>

                <td>${c.total_votes}</td>

            </tr>

        `;
    });


    // TASKS

    const taskRes =
    await fetch("/task/all");

    const tasks =
    await taskRes.json();

    const taskTable =
    document.getElementById("taskTable");

    taskTable.innerHTML = "";

    let completed = 0;
    let pending = 0;

    tasks.forEach(task => {

        if(task.status === "Completed"){

            completed++;

        }else{

            pending++;
        }

        taskTable.innerHTML += `

            <tr>

                <td>${task.task_name}</td>

                <td>${task.employee_name}</td>

                <td>${task.status}</td>

            </tr>

        `;
    });


    // BAR CHART — VOTING PERCENTAGE

const candidateNames = [];
const candidateVotes = [];

candidates.forEach(c => {

    candidateNames.push(
        c.candidate_name
    );

    candidateVotes.push(
        c.total_votes || 0
    );

});

const ctx =
document.getElementById("voteChart");

new Chart(ctx, {

    type: "bar",

    data: {

        labels: candidateNames,

        datasets: [{

            label: "Votes",

            data: candidateVotes,

            borderWidth: 1

        }]
    },

    options: {

        responsive: true,

        scales: {

            y: {

                beginAtZero: true

            }

        }

    }

});

}

loadStatistics();