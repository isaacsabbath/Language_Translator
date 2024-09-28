function translateText() {
    const inputText = document.getElementById('inputText').value;
    const outputText = document.getElementById('outputText');

    // Simple mock translation (reverses the input text)
    const translatedText = inputText.split('').reverse().join('');
    outputText.innerText = translatedText;

    // Add active class for color change
    outputText.classList.add('active');

    // Remove active class after 2 seconds
    setTimeout(() => {
        outputText.classList.remove('active');
    }, 2000);
}

// Toggle night mode
document.body.addEventListener('dblclick', () => {
    document.body.classList.toggle('night-mode');
});
