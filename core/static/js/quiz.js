document.addEventListener('DOMContentLoaded', function () {
  const nextCardForm = document.querySelector('#next-card-form')
  const nextCardButton = document.querySelector('#next-card-button')

  nextCardButton.addEventListener('click', function (event) {
    console.log('you clicked me')
    event.preventDefault()
    fetch(nextCardForm.action, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
      .then(response => response.json())
      .then(function (response) {
        console.log(response)
      })
  })
})
