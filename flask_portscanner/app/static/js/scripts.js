document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const targetInput = document.getElementById('target');
    const submitButton = form.querySelector('button[type="submit"]');
    const spinner = document.createElement('div');

    spinner.classList.add('spinner');
    spinner.style.display = 'none';
    submitButton.parentNode.insertBefore(spinner, submitButton.nextSibling);

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Validate the target input
        const targetValue = targetInput.value.trim();
        if (targetValue === '') {
            alert('Please enter a target IP address.');
            return;
        }

        // Show the spinner and disable the submit button
        spinner.style.display = 'inline-block';
        submitButton.disabled = true;

        // Simulate form submission
        setTimeout(() => {
            form.submit();
        }, 500); // Delay for the spinner to be visible
    });
});

// CSS for the spinner
const style = document.createElement('style');
style.innerHTML = `
    .spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(0, 0, 0, 0.3);
        border-radius: 50%;
        border-top-color: #000;
        animation: spin 1s ease-in-out infinite;
        margin-left: 10px;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);
