const inputs = document.querySelectorAll('.validate')
const submit = document.querySelector('input[type=submit]')

submit.disabled = true

const patterns = {
    password: /^[\w@-]{8,}$/,
    login: /^[a-z\d_]{3,}$/i, 
    contact: /^\d{10}$/,
    fname: /^[a-zA-z ?]{2,30}$/,
    email: /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/
}

let check = (inputField, regex) => { 
    inputField.classList.remove('border-gray-300')
    if(regex.test(inputField.value)){
        inputField.classList.remove('border-red-500')
        inputField.classList.add('border-green-500')
    }else{
        inputField.classList.remove('border-green-500')
        inputField.classList.add('border-red-500')
    }

    inputs.forEach(input => {
        if(input.classList.contains('border-green-500')){
            submit.disabled = false
        }
    }) 
}

inputs.forEach(input => {
    input.addEventListener('focusout', e => {
      check(e.target, patterns[e.target.getAttribute('name')]) 
    })
}) 