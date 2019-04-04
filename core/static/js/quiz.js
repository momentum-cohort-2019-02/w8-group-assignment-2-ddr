document.addEventListener('DOMContentLoaded', function () {
    const game = document.querySelector('#game')

    if (game !== null) {
        playRound()
    }
        
})

function playRound() {
    console.log('you played a round!')
    console.log(game.dataset.deck)
}
