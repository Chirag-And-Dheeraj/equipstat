const hamburgur = document.querySelector('.hamburgur')
const navItems = document.querySelector('.navItems')

if(window.innerWidth < 640) {
    hamburgur.addEventListener('click', e => {
        hamburgur.classList.toggle('change')
        navItems.classList.toggle('hidden')
    }) 
}else {
    hamburgur.remove()
}

