let selectedCards = [];
let matchedPairs = 0;
let score = 0;
let stopwatchInterval;
let seconds = 0;

function startGame() {
    document.getElementById('game-grid').innerHTML = '';
    selectedCards = [];
    matchedPairs = 0;
    score = 0;
    seconds = 0;
    document.getElementById('score-value').textContent = score;
    clearInterval(stopwatchInterval);
    stopwatchInterval = setInterval(updateStopwatch, 1000);
    fetchCards();
}

function fetchCards() {
    fetch('/get_cards')
        .then(response => response.json())
        .then(cards => {
            const gameGrid = document.getElementById('game-grid');
            cards.forEach(card => {
                const cardElement = document.createElement('div');
                cardElement.className = 'card';
                cardElement.dataset.id = card.id;
                cardElement.dataset.content = card.content;
                cardElement.dataset.type = card.type;
                cardElement.textContent = '?';
                cardElement.addEventListener('click', () => selectCard(cardElement));
                gameGrid.appendChild(cardElement);
            });
        });
}

function selectCard(card) {
    if (selectedCards.length < 2 && !card.classList.contains('matched') && !selectedCards.includes(card)) {
        card.textContent = card.dataset.content;
        selectedCards.push(card);
        
        if (selectedCards.length === 2) {
            checkMatch();
        }
    }
}

function checkMatch() {
    const [card1, card2] = selectedCards;
    fetch('/check_match', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            card1: { content: card1.dataset.content, type: card1.dataset.type },
            card2: { content: card2.dataset.content, type: card2.dataset.type }
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.match) {
            matchedPairs++;
            score += 10;
            card1.classList.add('matched');
            card2.classList.add('matched');
            document.getElementById('score-value').textContent = score;
            if (matchedPairs === 8) {
                clearInterval(stopwatchInterval);
                alert(`Congratulations! You've matched all pairs. Your score: ${score}`);
            } else {
                replaceMatchedCards();
            }
        } else {
            setTimeout(() => {
                card1.textContent = '?';
                card2.textContent = '?';
            }, 1000);
        }
        selectedCards = [];
    });
}

function replaceMatchedCards() {
    fetch('/get_cards')
        .then(response => response.json())
        .then(newCards => {
            const gameGrid = document.getElementById('game-grid');
            const matchedCards = gameGrid.querySelectorAll('.card.matched');
            matchedCards.forEach((matchedCard, index) => {
                if (index < newCards.length) {
                    const newCard = newCards[index];
                    matchedCard.dataset.id = newCard.id;
                    matchedCard.dataset.content = newCard.content;
                    matchedCard.dataset.type = newCard.type;
                    matchedCard.textContent = '?';
                    matchedCard.classList.remove('matched');
                }
            });
        });
}

function updateStopwatch() {
    seconds++;
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    document.getElementById('stopwatch').textContent = 
        `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
}

document.getElementById('start-game').addEventListener('click', startGame);
