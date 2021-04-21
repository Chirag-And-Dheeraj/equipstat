// accordian animations - start - sm

const accBtns = document.querySelectorAll('.btn')
const chevronArrow = document.querySelectorAll('.chevron')

console.log(chevronArrow)

if(innerWidth < 768) {
    const btns = [...accBtns]
    const btnsState = btns.map( btn => ({btn, closed:null}))

    for (let i = 0; i < accBtns.length; i++) {
        let panel = accBtns[i].nextElementSibling
        let childElements = Array.from(accBtns[i].children)
        btnsState[i].btn.addEventListener('click', e => {
            
            //close accordian if any other accordian is open and rotate chevron
            for (let j = 0; j < accBtns.length; j++) {
                btnsState[j].closed = false
                if(accBtns[j].nextElementSibling.classList.contains('opened')) {
                    accBtns[j].nextElementSibling.style.maxHeight = null
                    btnsState[j].closed = true
                    accBtns[j].nextElementSibling.classList.remove('opened')
                    Array.from(accBtns[j].children)[1].classList.remove("transform", "-rotate-180")
                }
            }

            //open accordian and rotate chevron
            if(btnsState[i].closed !== true){
                panel.style.maxHeight = `${panel.scrollHeight}px`;
                panel.classList.add('opened')
                childElements[1].classList.add("transition-all", "transform", "rotate-180")
            }
        })
    }
}
// accordian animations - end - sm

if(innerWidth >= 768) {
    chevronArrow.forEach(arrow => arrow.classList.add("transform", "-rotate-90"))
}