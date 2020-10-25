let updateButtons = document.getElementsByClassName('add')
// console.log(updateButtons)

for (let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click',function(event){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log("ProductId:" + productId , "action:" + action)
        console.log("User:" + loggedInUser)
        updateUserOrder(productId, action)
    })
}


function updateUserOrder(productId , action) {
    console.log("User is logged in sending data")

    let url = "/update_item/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'ProductId':productId,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data: '+ data)
    })
}