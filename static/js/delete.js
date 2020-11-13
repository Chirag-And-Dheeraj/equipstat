let deleteButtons = document.getElementsByClassName('delete-listing')

for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener('click', function (event) {
        let listingID = this.dataset.listing
        console.log("ListingID:" + listingID)
        console.log("user:" + loggedInUser)
        deleteListing(listingID)
    })
}

function deleteSuccessful(id) {
    url = '/user/' + id
    window.location.replace(url)
}

function deleteListing(listingID) {
    url = '/delete_listing/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'listingID': listingID })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log(data)
            deleteSuccessful(data)
        })
}