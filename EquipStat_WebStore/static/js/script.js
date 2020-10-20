const user = document.getElementById("userBtn")
const dropDown = document.getElementById("dropdownList")
user.addEventListener('click' , function (event) {
    if(dropDown.classList.contains('hidden')){
        dropDown.classList.remove('hidden')
    }else{
        dropDown.classList.add('hidden')
    }
})