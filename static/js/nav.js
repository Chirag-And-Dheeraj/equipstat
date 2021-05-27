const hamburgur = document.querySelector('.hamburgur')
const navItems = document.querySelector('.navItems')
const navContent = document.querySelector('.nav-content')
const mobNew = document.querySelector('.mobNew')
const mobNewContent = document.querySelector('.mobNewContent')
const mobRef = document.querySelector('.mobRef')
const mobRefContent = document.querySelector('.mobRefContent')

if(window.innerWidth <= 640) {
    hamburgur.addEventListener('click', e => {
        hamburgur.classList.toggle('change')
        navItems.classList.toggle('hidden')
    })
    
    mobNew.addEventListener('click', () => {
        if(mobNewContent.classList.contains('hidden')){
            mobNewContent.classList.remove('hidden')
            mobNew.querySelector('img').classList.add("transition-all", "transform", "rotate-180")
        }else{
            mobNewContent.classList.add('hidden')
            mobNew.querySelector('img').classList.remove("transform", "rotate-180")
        }
    })

    mobRef.addEventListener('click', () => {
        console.log("Ref Fired")
        if(mobRefContent.classList.contains('hidden')){
            mobRefContent.classList.remove('hidden')
            mobRef.querySelector('img').classList.add("transition-all", "transform", "rotate-180")
        }else{
            mobRefContent.classList.add('hidden')
            mobRef.querySelector('img').classList.remove("transform", "rotate-180")
        }
    })
}else {
    hamburgur.remove()
}

