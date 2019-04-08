function qS(selector) {
    return document.querySelector(selector)
}

function qSa(selector) {
    return document.querySelectorAll(selector)
}


let showResults = qS('.card-container');



// function updateResults() {
//     getResults(`decks/<slug:slug>/edit/`)
//         .then(response => {
//             f
//         })
// }

document.addEventListener('DOMContentLoaded', function () {


    function getResults(url) {
        let promise = fetch(url.action, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw Error(response.statusText)
                }
                return response.json()
            })
        return promise
    }

    function updateResults(url) {
        getResults(url)
            .then(function (cardData) {
                console.log(cardData)
            })
    }
    document.addEventListener('DOMContentLoaded', function () {
        updateResults(showResults)
    })
})