// accordian animations -start

const accBtns = document.querySelectorAll('.btn')
const chevronArrow = document.querySelectorAll('.chevron')


for (let i = 0; i < accBtns.length; i++) {
    let panel = accBtns[i].nextElementSibling
    let childElements = Array.from(accBtns[i].children)
    accBtns[i].addEventListener('click', e => {
        let closed = false
        for (let j = 0; j < accBtns.length; j++) {
            if(accBtns[j].nextElementSibling.classList.contains('opened')){
                closed = true
                accBtns[j].nextElementSibling.style.maxHeight = null
                accBtns[j].nextElementSibling.classList.remove('opened')
                console.log("closing currently opened accordian")
                Array.from(accBtns[j].children)[1].classList.remove("transform", "-rotate-180")
            }
        }
        if(closed !== true){
            panel.style.maxHeight = `${panel.scrollHeight}px`;
            panel.classList.add('opened')
            childElements[1].classList.add("transition-all", "transform", "rotate-180")
        }
    })
}

// accordian animations -end



