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
    let navButtons = document.createElement('div')
    navButtons.classList.add("space-x-3")
    navButtons.innerHTML = `
    <div class="w-28 relative inline-block cursor-pointer md:text-lg">
        <div class="new">
            New
            <img class="inline w-5" src="../static/images/chevron-down.svg">
        </div>
        <div class="newList hidden mt-2 absolute right-0 bg-white border rounded z-10 p-2">
            <a href="/calculators/" class="p-2 block text-black hover:underline">
                Calculators
            </a>
            <a href="/instruments/" class="p-2 block text-black hover:underline">
                Instruments
            </a>
        </div>
    </div>
    <div class="w-32 relative inline-block cursor-pointer md:text-lg">
        <div class="ref">
            Refurbished
            <img class="inline w-5" src="../static/images/chevron-down.svg">
        </div>
        <div class="refList hidden mt-2 absolute right-0 bg-white border rounded z-10 p-2">
            <a href="/refurbished-books/" class="p-2 block text-black hover:underline">
                Books
            </a>
            <a href="/refurbished-instruments/" class="p-2 block text-black hover:underline">
                Instruments
            </a>
            <a href="/refurbished-labcoats/" class="p-2 block text-black hover:underline">
                Labcoats
            </a>
        </div>
    </div>
    <a href="/accounts/signup/" class="bg-pallete-buttonPrimary focus:outline-none p-2 text-lg text-white rounded cursor-pointer font-medium md:text-xl">
        Sign Up
    </a> 
    <a href="/accounts/login/" class="bg-gray-200 rounded focus:outline-none p-2 text-lg cursor-pointer font-medium md:text-xl">
        Sign in
    </a>
    `
    navContent.appendChild(navButtons)
}

