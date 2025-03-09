// Words to guess
const words = ["apple", "blaze", "chair", "stone", "candy"];
const wordToGuess = words[Math.floor(Math.random() * words.length)].toUpperCase(); // Random word for the user to guess
let currentGuess = "";
let attempts = 0;
const maxAttempts = 6;

// Create a grid for the game board (5 rows, 5 columns)
const gameBoard = document.getElementById("game-board");
for (let i = 0; i < maxAttempts; i++) {
    for (let j = 0; j < 5; j++) {
        const cell = document.createElement("div");
        cell.classList.add("cell");
        gameBoard.appendChild(cell);
    }
}

// Handle the guess submission
document.getElementById("submit-button").addEventListener("click", function () {
    currentGuess = document.getElementById("guess-input").value.toUpperCase();
    if (currentGuess.length === 5 && words.includes(currentGuess.toLowerCase())) {
        submitGuess();
    } else {
        alert("Please enter a valid 5-letter word.");
    }
});

// Function to process the guess
function submitGuess() {
    const cells = document.querySelectorAll(".cell");
    const guessArray = currentGuess.split("");

    // Check if the user has won the game
    if (currentGuess === wordToGuess) {
        document.getElementById("message").textContent = "You Win!";
        return;
    }

    // Provide feedback on each letter
    for (let i = 0; i < 5; i++) {
        const cell = cells[attempts * 5 + i];
        cell.textContent = guessArray[i];

        // Check if the letter is in the correct position (green)
        if (guessArray[i] === wordToGuess[i]) {
            cell.style.backgroundColor = "green";
        }
        // Check if the letter is in the word (yellow)
        else if (wordToGuess.includes(guessArray[i])) {
            cell.style.backgroundColor = "yellow";
        }
        // Otherwise, letter is not in the word (gray)
        else {
            cell.style.backgroundColor = "gray";
        }
    }

    attempts++;
    document.getElementById("guess-input").value = "";

    // If the user has exhausted all attempts
    if (attempts === maxAttempts) {
        document.getElementById("message").textContent = `Game Over! The word was: ${wordToGuess}`;
    }
}
