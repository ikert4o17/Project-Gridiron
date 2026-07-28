const rankingsDiv = document.getElementById("rankings");

rankings.forEach((team, index) => {

    rankingsDiv.innerHTML +=
    `
    <p>
    ${index + 1}. ${team.team} — ${team.rating}
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
