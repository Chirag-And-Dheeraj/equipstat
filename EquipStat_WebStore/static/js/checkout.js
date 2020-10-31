let placeOrderButton = document.getElementsByClassName('checkout')
// console.log(placeOrderButton)


if (placeOrderButton[0]!=undefined){
    placeOrderButton[0].addEventListener('click', function (event) {
        let orderID = this.dataset.order
        let orderTotal = this.dataset.total
        // console.log(orderID)
        placeOrder(orderID, orderTotal)
    })
}



function placeOrder(orderID, orderTotal) {
    let url = "/place_order/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'orderID': orderID, 'orderTotal': orderTotal })
    })
        .then((response) => {
            // console.log("Fetch  executed successfully.")
            return response.json()
        })

        .then((data) => {
            console.log(data)
        })
}

let downloadButton = document.querySelector('.download')
console.log(downloadButton); 

downloadButton.addEventListener('click',function(){
    html2canvas(document.querySelector('.receipt'),{
        onrendered: function(canvas){
            return Canvas2Image.saveAsPNG(canvas)
        }
    })
    // window.print()
})