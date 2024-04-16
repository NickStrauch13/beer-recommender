document.addEventListener('DOMContentLoaded', function() {
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


function displayRecommendations(beers) {
    const resultsDiv = document.getElementById('recommendationResults');
    resultsDiv.innerHTML = '';  // Clear previous results

    // Create a table element
    let table = document.createElement('table');
    table.classList.add('recommendation-table'); // Add a class for styling if needed

    // Create table header
    let thead = document.createElement('thead');
    let headerRow = document.createElement('tr');
    ['Beer Name', 'Brewery', 'Beer Style', 'Predicted Rating'].forEach(headerText => {
        let header = document.createElement('th');
        header.textContent = headerText;
        headerRow.appendChild(header);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    let tbody = document.createElement('tbody');
    beers.forEach(beer => {
        let tr = document.createElement('tr');
        // Access each property by key to ensure the correct order
        tr.appendChild(createCell(beer['Beer Name']));
        tr.appendChild(createCell(beer['Brewery']));
        tr.appendChild(createCell(beer['Beer Style']));
        tr.appendChild(createCell(beer['Predicted Rating']));
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    // Append the table to the resultsDiv
    resultsDiv.appendChild(table);
}

function createCell(text) {
    let td = document.createElement('td');
    td.textContent = text;
    return td;
}

