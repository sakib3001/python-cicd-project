function fetchQuote() {
    fetch('/get-quote')
        .then(response => response.json())
        .then(data => {
            const quoteElement = document.getElementById('quote');
            quoteElement.innerText = "";
            let i = 0;
            function typeWriter() {
                if (i < data.quote.length) {
                    quoteElement.innerHTML += data.quote.charAt(i);
                    i++;
                    setTimeout(typeWriter, 50);
                }
            }
            typeWriter();
        });
}
