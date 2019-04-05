document.addEventListener('DOMContentLoaded', function () {
  const nextCardForm = document.querySelector('#next-card-form')
  const nextCardButton = document.querySelector('#next-card-button')
  const gameStatus = document.querySelector('#game-status')
  const cardDiv = document.querySelector('#card')
  let deckDict = {}
  let availableCards = []
  let numberOfCards = 0
  let box1 = []
  let box2 = []
  let box3 = []
  let box4 = []
  let box5 = []

  let box1div = document.createElement('div')
  let box2div = document.createElement('div')
  let box3div = document.createElement('div')
  let box4div = document.createElement('div')
  let box5div = document.createElement('div')
  gameStatus.appendChild(box1div)
  gameStatus.appendChild(box2div)
  gameStatus.appendChild(box3div)
  gameStatus.appendChild(box4div)
  gameStatus.appendChild(box5div)

  fetch(nextCardForm.action, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
    .then(response => response.json())
    .then(function (response) {
      deckDict = response
      for (let card in deckDict) {
        availableCards.push(deckDict[card])
        box1.push(deckDict[card])
        numberOfCards += 1
      }
      updateBoxes()
      shuffle(availableCards)
      console.log(box1)
    })

  nextCardButton.addEventListener('click', function (event) {
    event.preventDefault()

    if (availableCards.length === 0) {
      if (box5.length === numberOfCards) {
        console.log('you win!')
      } else {
        for (let card in box1) {
          availableCards.push(box1[card])
        }
        for (let card in box2) {
          availableCards.push(box2[card])
        }
        for (let card in box3) {
          availableCards.push(box3[card])
        }
        for (let card in box4) {
          availableCards.push(box4[card])
        }
        shuffle(availableCards)
      }
    }

    let currentCard = availableCards.shift()

    if (box5.includes(currentCard)) {
      console.log('something fucked up...')
    } else if (box4.includes(currentCard)) {
      box5.push(box4.splice(box4.indexOf(currentCard), 1))
    } else if (box3.includes(currentCard)) {
      box4.push(box3.splice(box3.indexOf(currentCard), 1))
    } else if (box2.includes(currentCard)) {
      box3.push(box2.splice(box2.indexOf(currentCard), 1))
    } else if (box1.includes(currentCard)) {
      box2.push(box1.splice(box1.indexOf(currentCard), 1))
    } else {
      console.log('card not in any of the boxes checked')
    }

    updateBoxes()
    console.log(box1, box2, box3, box4, box5)
  })

  function updateBoxes () {
    box1div.innerText = box1.length
    box2div.innerText = box2.length
    box3div.innerText = box3.length
    box4div.innerText = box4.length
    box5div.innerText = box5.length
    cardDiv.innerText = box1[0]['front']
  }

  function shuffle (array) {
    var currentIndex = array.length; var temporaryValue; var randomIndex

    // While there remain elements to shuffle...
    while (currentIndex !== 0) {
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex)
      currentIndex -= 1

      // And swap it with the current element.
      temporaryValue = array[currentIndex]
      array[currentIndex] = array[randomIndex]
      array[randomIndex] = temporaryValue
    }

    return array
  }
})
