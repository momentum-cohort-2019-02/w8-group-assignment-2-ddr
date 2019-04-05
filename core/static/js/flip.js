// card flip functionality found at https://codepen.io/desandro/pen/LmWozd

const cards = document.querySelectorAll('.card')
for (let card of cards){
  card.addEventListener( 'click', function() {
    card.classList.toggle('is-flipped')
  });
}