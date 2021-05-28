let logoutBtn = document.querySelectorAll(".logout");

logoutBtn.forEach ( (btn) => { 
    btn.addEventListener('click', () => {
        let url = "/accounts/logout/"
        fetch(url, 
            {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ })
            })
            window.location.replace('/')
    }
)})