// DOM Elements
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.getElementById('result-screen');
const startBtn = document.getElementById('start-btn');
const nextBtn = document.getElementById('next-btn');
const restartBtn = document.getElementById('restart-btn');
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options');
const scoreElement = document.getElementById('score');
const totalQuestionsElement = document.getElementById('total-questions');
const finalScoreElement = document.getElementById('final-score');
const totalQuestionsFinalElement = document.getElementById('total-questions-final');
const resultMessage = document.getElementById('result-message');
const progressBar = document.querySelector('.progress');

// Animation and Audio elements
const correctSound = document.getElementById('correct-sound');
const wrongSound = document.getElementById('wrong-sound');
const completeSound = document.getElementById('complete-sound');
const clappingSound = document.getElementById('clapping-sound');
const sirenEffect = document.getElementById('siren-effect');
const clappingHands = document.getElementById('clapping-hands');

// Quiz state
let currentQuestionIndex = 0;
let score = 0;
let selectedOption = null;

// Quiz questions
const questions = [
    {
        question: "Quando foi fundada a companhia?",
        options: ["2011", "2013", "2008", "2007", "2005"],
        correct: 3,
        explanation: "A PortoEx foi fundada em 2007."
    },
    {
        question: "Quais desses serviços são oferecidos?",
        options: [
            "Serviços advocatícios",
            "Serviços empresariais",
            "Serviços logísticos",
            "Serviços de taxidriver",
            "Serviços navais"
        ],
        correct: 2,
        explanation: "A PortoEx é especializada em serviços logísticos."
    },
    {
        question: "Qual é a pessoa que aparece na homepage da empresa?",
        options: [
            "Ana Elícia",
            "Fabrício",
            "Marlon Marques",
            "José Aguinaldo",
            "Isadora"
        ],
        correct: 3,
        explanation: "Marlon Marques é a pessoa que aparece na homepage da empresa."
    },
    {
        question: "Quantos serviços oferecemos pela homepage?",
        options: [
            "TRANSPORTE ECONÔMICO, TRANSPORTE PERSONALIZADO, TRANSPORTE EXPRESSO e SERVIÇOS LOGÍSTICOS",
            "TRANSPORTE DE CARGA, TRANSPORTE ADUANEIRO, TRANSPORTE ENTRE BASES e ARMAZENAGEM",
            "TRANSPORTE DE VEÍCULOS (CEGONHA), TRANSPORTE DE CARGA PESADA (HEAVYLIFT), TRANSPORTE ADUANEIRO (NAVIO) e TRANSPORTE AÉREO",
            "SERVIÇOS LOGÍSTICOS GERAIS",
            "TRANSPORTE DE CARGAS GERAIS, TRANSPORTE DE CARGA VALIOSA, TRANSPORTE DE CARGA FRACIONADA e TRANSPORTE DEDICADO"
        ],
        correct: 0,
        explanation: "Os serviços oferecidos são: TRANSPORTE ECONÔMICO, TRANSPORTE PERSONALIZADO, TRANSPORTE EXPRESSO e SERVIÇOS LOGÍSTICOS."
    },
    {
        question: "Quais serviços são oferecidos no transporte personalizado?",
        options: [
            "Contêiner, DTA (Declaração de Trânsito Aduaneiro), Lotação e Veículo plataforma",
            "Entregas em shopping, Cargas Anvisa, Entregas em locais com grades de horário e Armazenagem",
            "Entregas sem agendamento fixo (possível antecipação), Crossdocking, Etiquetagem e Separação",
            "Cargas Anvisa e Cargas com valor agregado",
            "Nenhuma das alternativas"
        ],
        correct: 0,
        explanation: "No transporte personalizado, são oferecidos: Contêiner, DTA (Declaração de Trânsito Aduaneiro), Lotação e Veículo plataforma."
    },
    {
        question: "O que são cargas LTL e FTL?",
        options: [
            "LTL (Less Than Truckload): Refere-se ao transporte de cargas menores que não ocupam a totalidade do espaço ou da capacidade de peso de um caminhão. Nesse caso, a carga de um cliente é combinada com cargas de outros clientes no mesmo veículo, otimizando custos. É ideal para envios de pequeno a médio porte, como pallets ou caixas.\n   FTL (Full Truckload): Envolve o transporte de uma carga que ocupa todo o espaço ou a capacidade total de peso do caminhão, destinada a um único cliente. É usada para grandes volumes ou quando a carga exige entrega direta.",
            "LTL (Lotação de Tranporte Leve): Refere-se ao transporte de cargas leves, ou seja, cargas que não possuem alto valor e demandas expressas. Isso significa que a carga tem prioridade baixa e por esse motivo pode aguardar durante a transferência entre bases. FTL (Transporte Fracionado de Lotações): Refere-se a cargas que são fracionadas, por isso não há paletes serão sempre lotações batidas. Onde não há organização e proporções de clientes isso quer dizer que são diversos clientes."
        ],
        correct: 0,
        explanation: "LTL (Less Than Truckload) é para cargas menores que não enchem um caminhão, enquanto FTL (Full Truckload) é para cargas que ocupam um caminhão inteiro."
    },
    {
        question: "O que significa a lógica FIFO?",
        options: [
            "Federação Internacional de Organizações Futurísticas",
            "First In First Out (Primeiro a entrar, primeiro a sair)",
            "First Input Finally Output (Primeira Entrada, Finalmente Saída)"
        ],
        correct: 1,
        explanation: "FIFO significa 'First In, First Out' (Primeiro a Entrar, Primeiro a Sair), um método de organização de itens em que o primeiro item armazenado é o primeiro a ser retirado."
    }
];

// Initialize the quiz
function init() {
    const totalQuestions = questions.length;
    totalQuestionsElement.textContent = totalQuestionsFinalElement.textContent = totalQuestions;
    
    startBtn.addEventListener('click', startQuiz);
    nextBtn.addEventListener('click', nextQuestion);
    restartBtn.addEventListener('click', restartQuiz);
}

// Start the quiz
function startQuiz() {
    currentQuestionIndex = score = 0;
    updateScore();
    startScreen.classList.remove('active');
    quizScreen.classList.add('active');
    showQuestion();
}

// Show current question
function showQuestion() {
    const question = questions[currentQuestionIndex];
    updateProgressBar();
    questionText.textContent = question.question;
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, index) => {
        const optionElement = document.createElement('button');
        optionElement.className = 'option';
        optionElement.textContent = option;
        optionElement.dataset.index = index;
        optionElement.addEventListener('click', selectOption);
        optionsContainer.appendChild(optionElement);
    });
    
    nextBtn.disabled = true;
    selectedOption = null;
}

// Select an option
function selectOption(e) {
    if (selectedOption !== null) return;
    
    const selectedElement = e.target.closest('.option');
    if (!selectedElement) return;
    
    const selectedIndex = parseInt(selectedElement.dataset.index);
    const question = questions[currentQuestionIndex];
    const isCorrect = selectedIndex === question.correct;
    
    selectedElement.classList.add(isCorrect ? 'correct' : 'wrong');
    
    if (isCorrect) {
        score++;
        updateScore();
        playSound('correct');
        showCorrectAnswerAnimation();
    } else {
        optionsContainer.querySelector(`[data-index="${question.correct}"]`).classList.add('correct');
        playSound('wrong');
        showWrongAnswerAnimation();
    }
    
    optionsContainer.querySelectorAll('.option').forEach(opt => {
        opt.style.pointerEvents = 'none';
    });
    
    nextBtn.disabled = false;
    selectedOption = selectedIndex;
    
    setTimeout(() => {
        showExplanation(question.explanation);
    }, 1000);
}

// Show explanation
function showExplanation(explanation) {
    const explanationElement = document.createElement('div');
    explanationElement.className = 'explanation';
    explanationElement.innerHTML = `<strong>Explicação:</strong> ${explanation}`;
    
    const existingExplanation = document.querySelector('.explanation');
    if (existingExplanation) existingExplanation.remove();
    
    optionsContainer.parentNode.insertBefore(explanationElement, nextBtn);
}

function createConfetti() {
    const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'];
    const container = document.body;
    
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = `${Math.random() * 100}%`;
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDuration = `${2 + Math.random() * 3}s`;
        confetti.style.animationDelay = `${Math.random() * 2}s`;
        container.appendChild(confetti);
        
        // Remove confetti after animation completes
        setTimeout(() => {
            confetti.remove();
        }, 5000);
    }
}

function showCorrectAnswerAnimation() {
    // Show clapping hands
    clappingHands.classList.add('active');
    clappingSound.currentTime = 0;
    clappingSound.play().catch(e => console.log("Clapping sound play failed:", e));
    
    // Create confetti
    createConfetti();
    
    // Remove clapping hands after animation
    setTimeout(() => {
        clappingHands.classList.remove('active');
    }, 2000);
}

function showWrongAnswerAnimation() {
    // Show siren effect
    sirenEffect.classList.add('active');
    
    // Remove siren effect after animation
    setTimeout(() => {
        sirenEffect.classList.remove('active');
    }, 2000);
}

// Play sound effect
function playSound(type) {
    const sound = type === 'correct' ? correctSound : 
                 type === 'wrong' ? wrongSound : completeSound;
    const soundClone = sound.cloneNode();
    soundClone.volume = 0.5;
    soundClone.play().catch(e => console.log("Audio play failed:", e));
}

// Update progress bar
function updateProgressBar() {
    progressBar.style.width = `${(currentQuestionIndex / questions.length) * 100}%`;
}

// Update score display
function updateScore() {
    scoreElement.textContent = score;
}

// Next question or show results
function nextQuestion() {
    document.querySelector('.explanation')?.remove();
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        showResults();
    }
}

// Show quiz results
function showResults() {
    const totalQuestions = questions.length;
    const correctAnswers = score;
    const wrongAnswers = totalQuestions - correctAnswers;
    
    // Update the final score display
    finalScoreElement.textContent = `${correctAnswers}`;
    document.getElementById('total-questions-final').textContent = totalQuestions;
    
    // Create a detailed result message
    let resultHTML = `
        <div class="score-summary">
            <div class="score-correct">✅ Respostas corretas: ${correctAnswers}</div>
            <div class="score-wrong">❌ Respostas incorretas: ${wrongAnswers}</div>
        </div>
        <div class="score-percentage">
            ${Math.round((correctAnswers / totalQuestions) * 100)}% de acerto
        </div>
    `;
    
    const percentage = (correctAnswers / totalQuestions) * 100;
    
    // Add appropriate message based on score
    let message = '';
    if (percentage === 100) {
        message = '🎉 Parabéns! Você é um verdadeiro especialista da PortoEx! 🎉';
        createConfetti();
        playSound('complete');
    } else if (percentage >= 80) {
        message = '👏 Excelente trabalho! Você conhece muito bem a PortoEx!';
        playSound('complete');
    } else if (percentage >= 60) {
        message = '👍 Bom trabalho! Continue aprendendo sobre a PortoEx!';
    } else {
        message = '📚 Continue explorando a PortoEx para conhecer melhor nossos serviços!';
    }
    
    resultMessage.innerHTML = resultHTML + '<div class="result-message-text">' + message + '</div>';
    
    quizScreen.classList.remove('active');
    resultScreen.classList.add('active');
}

// Create confetti effect
function createConfetti() {
    const colors = ['#0066cc', '#ff9900', '#4caf50', '#f44336', '#9c27b0'];
    
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = `${Math.random() * 100}%`;
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animation = `confetti ${2 + Math.random() * 3}s ease-out ${Math.random() * 3}s forwards`;
        document.body.appendChild(confetti);
    }
}

// Restart quiz
function restartQuiz() {
    resultScreen.classList.remove('active');
    startQuiz();
    
    // Remove confetti
    document.querySelectorAll('.confetti').forEach(el => el.remove());
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
