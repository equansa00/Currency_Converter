// Main.js
document.addEventListener('DOMContentLoaded', function () {
    // This function runs once the document is fully loaded.

    // Example of adding an event listener to a button with id "convertButton"
    const convertButton = document.getElementById('convertButton');
    if (convertButton) {
        convertButton.addEventListener('click', function () {
            // Logic for the conversion operation can go here.
            convertCurrency();
        });
    }
});

/**
 * An example function to convert currency.
 */
function convertCurrency() {
    const amount = parseFloat(document.getElementById('amount').value);
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    // Validate inputs
    if (isNaN(amount)) {
        alert('Please enter a valid amount.');
        return;
    }

    // This is just an example. In a real application, you'd likely fetch 
    // conversion rates from an API and then perform the conversion.
    const conversionRate = 1.2;  // Example conversion rate
    const convertedAmount = amount * conversionRate;

    document.getElementById('result').innerText = `${amount} ${fromCurrency} is approximately ${convertedAmount.toFixed(2)} ${toCurrency}.`;
}

/**
 * Any other utility functions or logic can be added below.
 */
