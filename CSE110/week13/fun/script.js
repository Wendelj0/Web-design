// script.js
const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');

// Game variables
let dinoX = 50;
let dinoY = 150;
let dinoWidth = 40;
let dinoHeight = 40;
let obstacleX = 400;
let obstacleY = 150;
let obstacleWidth = 20;
let obstacleHeight = 20;
let score = 0;
let speed = 2;

// Game loop
function update() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw dino
  ctx.fillStyle = '#000';
  ctx.fillRect(dinoX, dinoY, dinoWidth, dinoHeight);
  
  // Draw obstacle
  ctx.fillStyle = '#000';
  ctx.fillRect(obstacleX, obstacleY, obstacleWidth, obstacleHeight);
  
  // Update obstacle position
  obstacleX -= speed;
  
  // Check collision
  if (obstacleX < dinoX + dinoWidth && obstacleX + obstacleWidth > dinoX && obstacleY < dinoY + dinoHeight && obstacleY + obstacleHeight > dinoY) {
    alert('Game Over!');
    score = 0;
  }
  
  // Update score
  score++;
  
  // Draw score
  ctx.font = '24px Arial';
  ctx.fillStyle = '#000';
  ctx.textAlign = 'left';
  ctx.textBaseline = 'top';
  ctx.fillText(`Score: ${score}`, 10, 10);
  
  // Request next frame
  requestAnimationFrame(update);
}

// Handle key press
document.addEventListener('keydown', (e) => {
  if (e.key === ' ') {
    // Jump
    dinoY -= 20;
    setTimeout(() => {
      dinoY += 20;
    }, 200);
  }
});

// Start game
update();