// editable fields interface for user - start
const inputFields = document.querySelectorAll('#profile-form input[type="text"]')
const editButton = document.querySelector('.edit-info')
const saveButton = document.querySelector('.save-info')

inputFields.forEach(input => {
    input.disabled = true
})

editButton.addEventListener('click', () => {
    inputFields.forEach(input => {
        input.disabled = false
    })
})

saveButton.addEventListener('click', e => {
    inputFields.forEach(input => {
        input.disabled = true
    })
    saveButton.disabled = true
})
// editable fields interface for user - end