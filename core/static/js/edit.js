/* globals fetch */
const Cookies = require('js-cookie')

function sQ(selector) {
    return document.querySelector(selector)
}

function sQa(selector) {
    return document.querySelectorAll(selector)
}

document.addEventListener('DOMContentLoaded', function () {
    const card_div = document.querySelector('.card')
    let cardContainer = sQ('.card-container')


    let url = `/core/decks/${ card_div.dataset.deckSlug }/edit/${ card_div.dataset.cardSlug }`
    console.log(card_div.dataset.thisUrl)
    console.log(url)
    const csrftoken = Cookies.get('csrftoken')


    cardContainer.addEventListener('click', (event) => {
        const {
            target
        } = event;
        let add_remove = sQ('.add_remove')
        if (!target.matches('.add_remove')) {
            return
        }
        event.preventDefault();
        promise = fetch(target.dataset.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(function (response) {
                if (!response.ok) {
                    // throw Error(response.statusText)
                }
                return response.json()
            })
            .then(function (response) {
                console.log(response)
                let cardSlug = sQ(`#card-${response['card-slug']}`)
                console.log(response.values['card-slug'])
                // console.log(`#card-${response[1]['card-slug']}`)
                cardSlug.classList.toggle('if-card-face-front')
            })

    })

})