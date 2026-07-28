const rankingsDiv = document.getElementById("rankings");

const sortedTeams = [...teams].sort(
    (a, b) => b.rating - a.rating
);


sortedTeams.forEach((team, index) => {

    rankingsDiv.innerHTML +=
    `
    <p>
    ${index + 1}. ${team.name} — ${team.rating}
    </p>
    `;

});


const predictionsDiv = document.getElementById("predictions");

predictions.forEach((game) => {

    predictionsDiv.innerHTML +=
    `
    <p>
    ${game.matchup}
    </p>

    <p>
    Pick: ${game.pick}
    </p>

    <p>
    Win Probability: ${game.probability}
    </p>
    `;

});
