document.addEventListener('DOMContentLoaded', function() {
    fetchUsers();
    document.getElementById('submitBtn').addEventListener('click', function() {
        var user = document.getElementById('userSelect').value;
        var model = document.getElementById('modelSelect').value;
        var num = document.getElementById('numRecommend').value;
        fetch('/recommend_beers', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: user, model: model, n: num })
        })
        .then(response => response.json())
        .then(data => {
            displayRecommendations(data);
        })
        .catch(error => console.error('Error:', error));
    });
});

function fetchUsers() {
    fetch('/get_users')
    .then(response => response.json())
    .then(data => {
        const userSelect = document.getElementById('userSelect');
        data.forEach(user => {
            let option = document.createElement('option');
            option.value = user;
            option.textContent = user;
            userSelect.appendChild(option);
        });
    });
}

function displayRecommendations(beers) {
    const resultsDiv = document.getElementById('recommendationResults');
    resultsDiv.innerHTML = '';
    beers.forEach(beer => {
        let p = document.createElement('p');
        p.textContent = beer;
        resultsDiv.appendChild(p);
    });
}
