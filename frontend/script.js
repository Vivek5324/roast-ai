const API_URL = 'https://roast-ai.onrender.com';

let userName = '';
let userLevel = '';

function startBattle() {
    userName = document.getElementById('name').value.trim();
    userLevel = document.getElementById('level').value;
    
    if (!userName) {
        alert('Please enter your name first!');
        return;
    }

    document.getElementById('setupCard').style.display = 'none';
    document.getElementById('battleCard').style.display = 'block';
}

async function sendRoast() {
    const comeback = document.getElementById('comeback').value.trim();
    if (!comeback) return;

    const loading = document.getElementById('loading');
    const chatContainer = document.getElementById('chatContainer');
    loading.style.display = 'block';

    try {
        const response = await fetch(`${API_URL}/roast`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: userName,
                comeback: comeback,
                level: userLevel
            })
        });

        const data = await response.json();
        
        const messageHTML = `
            <div class="message">
                <p><strong>Your Roast:</strong> ${comeback}</p>
                <p class="rating">🎯 ${data.rating}</p>
                <p><strong>AI's Comeback:</strong> ${data.roast}</p>
            </div>
        `;

        chatContainer.style.display = 'block';
        chatContainer.insertAdjacentHTML('afterbegin', messageHTML);
        document.getElementById('comeback').value = '';

    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong! Try again.');
    }

    loading.style.display = 'none';
}

// Allow sending roast with Enter key
document.getElementById('comeback').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendRoast();
    }
}); 