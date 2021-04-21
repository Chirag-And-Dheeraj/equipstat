setTimeout(() => {
    try {
        const messages = document.querySelector('.messages')
        messages.classList.add('hidden') 
    } catch (error) {
        console.log("Message not available.")
    }
}, 5000);
