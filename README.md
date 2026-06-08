# quantum-belot

## Rules:

### All Rules from Belot bg apply.
- dsa
- dsa
- das
- das

### Quantum rules:

- Cards are distributed independantly for each player / chosen by each player
- When a card is `declared` by a player (`holder`) other players (`observers`) either `agree` or `disagree` with the player in question having the card in question.
    - In case `observers` `agree` this card becomes `observed`.
    - In case `observers` `disagree` card stays.
    - In case `observers` do not manage to `agree` on a card the first card that the `holder` played becomes true and `observed`.
      After a decision is made players that `disagreed` with that decision adjust the `state` of their games so that they match the decision.

## During play:

1. All players draft their own verson of the deck with each player holding 8 cards. These cards remain in `superposition` until `declared` and `observed`.
2. In turn of play a player can pass or `declare` a card to announce a playing suit according to Belot rules. Depending on the card that is `declared` the following suit would be announced:
    - Any `Jack`: All Trumps
    - Any `Ace`; No Trumps
    - Any `Spade` except `Jack` or `Ace`: Spades
    - Any `Heart` except `Jack` or `Ace`: Hearts
    - Any `Diamond` except `Jack` or `Ace`: Diamonds
    - Any `Club` except `Jack` or `Ace`: Clubs
    - If the suit is already declared and is being re-declared will be considered as a `counter` and `re-counter`.
    - If the card becomes illegal to play after being `observed` it is instead returned to the player's hand and they pass.
3. In turn order each player either `declares` a card in `superposition` to play or plays an `observed` card.
    - If during play card 


