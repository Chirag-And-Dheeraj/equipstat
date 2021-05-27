const newDrop = document.querySelector(".new")
const refDrop = document.querySelector(".ref")
const newList = document.querySelector(".newList")
const refList = document.querySelector(".refList")
newDrop.addEventListener('click' , () => {
    if(newList.classList.contains('hidden')){
        newList.classList.remove('hidden')
    }else{
        newList.classList.add('hidden')
    }
})

refDrop.addEventListener('click' , () => {
    if(refList.classList.contains('hidden')){
        refList.classList.remove('hidden')
    }else{
        refList.classList.add('hidden')
    }
})