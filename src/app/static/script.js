document.getElementById('submitBtn').addEventListener('click', function() {
    var user = document.getElementById('userSelect').value;
    fetch('/recommend_beers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: user})
    })
    .then(response => response.json())
    .then(data => {
        displayRecommendations(data);
    })
    .catch(error => console.error('Error:', error));
});

function displayRecommendations(beers) {
    const resultsDiv = document.getElementById('recommendationResults');
    resultsDiv.innerHTML = '';  // Clear previous results
    beers.forEach(beer => {
        let p = document.createElement('p');
        p.textContent = beer;
        resultsDiv.appendChild(p);
    });
}
