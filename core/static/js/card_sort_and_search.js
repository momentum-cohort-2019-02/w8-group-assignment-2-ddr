const searchButton = document.querySelector('.search-button')
const searchBar = document.querySelector('.search-bar')
const cardsInDB = document.querySelector('#cards-in-db')

searchButton.addEventListener('click', function () {
  console.log(searchButton.dataset.action)
  fetch(searchButton.dataset.action + `?search=${searchBar.value}`, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
    .then(response => response.json())
    .then(function (response) {
      console.log(response)
      cardsInDB.innerHTML = ''
      for (let card in response) {
        if (response[card]['front_image_path']) {
          cardsInDB.innerHTML += `<div class="scene">
                                        <div class="card">
                                            <div class="card__face card__face--front" style="background: url('${response[card]['front_image_path']}'); background-size:contain; background-repeat: no-repeat; background-position: center;">
                                            </div>
                                            <div class="card__face card__face--back">
                                                <br> ${response[card]['back']}
                                            </div>
                                        </div>
                                    </div>`
        } else {
          cardsInDB.innerHTML += `<div class="scene">
                                        <div class="card">
                                            <div class="card__face card__face--front">
                                                <br> ${response[card]['front']}
                                                <br> <div class = "card-category">${response[card]['card_category']}</div>
                                            </div>
                                            <div class="card__face card__face--back">
                                                <br> ${response[card]['back']}
                                            </div>
                                        </div>
                                    </div>`
        }
      }
    })
})
