const content = document.querySelector('.content')

const templateHomeCards = dataset => {
    let html = ``
    dataset.forEach(data => {
        html += `
            <div class="grid justify-items-center gap-y-3 card p-5">
                <img src="${data.src}" alt="${data.alt}" title="${data.title}">
                <h6 class="text-xl font-medium">${data.text}</h6>
            </div>
        `
        
        content.innerHTML = html
    })
}

const getHomeCardsData = async () => {
    const response = await fetch("../static/json/homeCards.json")
    const dataset = await response.json()
    
    return dataset
}

getHomeCardsData()
    .then(dataset => {
        templateHomeCards(dataset)
    })
    .catch(err => console.log(err))

