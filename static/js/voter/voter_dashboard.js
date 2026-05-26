const voter =
JSON.parse(localStorage.getItem("voter"));


// PROTECT PAGE

if(!voter){

    window.location.href =
    "/voter/login-page";
}


const candidateContainer =
document.getElementById("candidateContainer");

const voteStatus =
document.getElementById("voteStatus");


// PROFILE DROPDOWN

const profileBtn =
document.getElementById("profileBtn");

const profileDropdown =
document.getElementById("profileDropdown");

profileBtn.addEventListener("click", () => {

    profileDropdown.style.display =

    profileDropdown.style.display === "block"
    ? "none"
    : "block";
});


// LOGOUT

document.getElementById("logoutBtn")
.addEventListener("click", () => {

    localStorage.removeItem("voter");

    // prevent back navigation after logout
window.history.pushState(null, "", window.location.href);

window.onpopstate = function () {
    window.history.pushState(null, "", window.location.href);
};
});


// LOAD CANDIDATES

async function loadCandidates(){

    try{

        const response =
        await fetch("/candidate/all");

        const candidates =
        await response.json();

        candidateContainer.innerHTML = "";

        candidates.forEach(candidate => {

            candidateContainer.innerHTML += `

                <div class="candidate-card">

                    <h2>
                        ${candidate.candidate_name}
                    </h2>

                    <div class="party-name">
                        ${candidate.party_name}
                    </div>

                    <div class="symbol">
                        ${candidate.symbol || "🗳️"}
                    </div>

                    <button
                    class="vote-btn"

                    onclick="submitVote(${candidate.candidate_id})"

                    ${voter.has_voted == 1
                    ? "disabled"
                    : ""}>

                        ${voter.has_voted == 1
                        ? "Already Voted"
                        : "Vote"}

                    </button>

                </div>

            `;
        });

        // STATUS

        if(voter.has_voted == 1){

            voteStatus.innerText =
            "You have already voted.";
        }

    }

    catch(error){

        console.log(error);
    }
}


// SUBMIT VOTE

async function submitVote(candidateId){

    const confirmVote =
    confirm(
        "Are you sure to vote?"
    );

    if(!confirmVote){
        return;
    }

    try{

        const response =
        await fetch("/vote", {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                voter_id:voter.voter_id,

                candidate_id:candidateId
            })
        });

        const data =
        await response.json();

        if(response.ok){

            alert(
                "Successfully voted"
            );

            // UPDATE LOCAL STORAGE

            voter.has_voted = 1;

            localStorage.setItem(
                "voter",
                JSON.stringify(voter)
            );

            location.reload();
        }

        else{

            alert(data.error);
        }

    }

    catch(error){

        console.log(error);
    }
}


loadCandidates();