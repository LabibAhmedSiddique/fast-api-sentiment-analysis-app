document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');
    const resultText = document.getElementById('result-text');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const text = formData.get('text');

        const response = await fetch('/predict/', {
            method: 'POST',
            body: new URLSearchParams({ 'text': text }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });

        const result = await response.json();

        resultText.textContent = `Sentiment: ${result.sentiment} (${(result.confidence * 100).toFixed(2)}%)`;
        resultDiv.style.display = 'block';
    });
});
