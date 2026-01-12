# Adventure

Adventure is a Battlefield-only game mode that comes with the [Battlefield Expansion](../content/battlefield_expansion.md).


## Cards

Adventure mode includes Adventure cards of two types, Combat and Event.


### Adventure-Event Card

To resolve an Adventure Event card, resolve its effect.

| Name | Effect |
| :--- | :---: |
| Campfire | Roll 1 [Attack die](../keywords/dice.md#attack-die). On a "+1" result, roll 2 [:resource_die:](../keywords/dice.md#resource-die) and resolve 1 of them.<br>Otherwise, roll 1 [:resource_die:](../keywords/dice.md#resource-die) and resolve it. |
| Corpse | [**Search (2)**](../keywords/search.md) the [:artifact:](../artifacts/index.md) deck. | 
| Learning Stone | If your [Hero](../heroes/index.md) is below level 4, gain 2 :experience:.<br>Otherwise, gain 1 :experience:. |
| Magic Spring | [**Search (4)**](../keywords/search.md) the Adventure deck discard pile, choose a card, swap it for this one, and resolve it.<br>Magic Spring cannot be saved. |
| Obelisk | **1ˢᵗ Obelisk:**<br>[**Search (2)**](../keywords/search.md) the [Positive Morale](../keywords/morale.md#positive) deck.<br><br>**2ⁿᵈ Obelisk:**<br>Increase the production of one of your resources.<br><br>**3ʳᵈ/4ᵗʰ Obelisk:**<br>Roll and resolve 4 [:resource_die:](../keywords/dice.md#resource-die). |
| Pandora's Box | Roll 2 [:treasure_die:](../keywords/dice.md#treasure-die) and resolve 1 of them. Draw 1 [Negative Morale](../keywords/morale.md#negative) card.<br><br>— OR —<br><br>Roll 2 [:resource_die:](../keywords/dice.md#resource-die) and resolve 1 of them. Draw 1 [Positive Morale](../keywords/morale.md#positive) card. |
| Scholar | Roll 1 [Attack die](../keywords/dice.md#attack-die).<br>On a "+1," Draw 1 [Statistic](../statistics/index.md) card of your choice.<br>On a "0," [**Search (2)**](../keywords/search.md) the [Ability](../abilities/index.md) deck.<br>On a "-1," [**Search (2)**](../keywords/search.md) the [Spell](../spells/index.md) deck. |
| Shrine of Magic Gesture | [**Search (2)**](../keywords/search.md) the [:spell:](../spells/index.md) deck. |
| Spell Scroll | [**Search (3)**](../keywords/search.md) [:spell:](../spells/index.md) and place the card facedown on this card, beside your [Hero](../heroes/index.md) card.<br>This [spell](../spells/index.md) does not count toward your hand or [spell](../spells/index.md) limits and can be cast at its lowest :power:. |
| Temple | [**Search (2)**](../keywords/search.md) the [Positive Morale](../keywords/morale.md#positive) deck. |
| Trading Post | Trade resources:<br>6 :gold: → 1 :valuables:<br>2 :gold: → 1 :building_materials:<br>3 :building_materials: → 1 :valuables:<br>1 :building_materials: → 1 :gold:<br>1 :valuables: → 3 :gold:<br>1 :valuables: → 2 :building_materials: |
| Treasure Chest | Roll 2 [:treasure_die:](../keywords/dice.md#treasure-die) and resolve 1 of them. |
| Tree of Knowledge | :pay: 10 :gold: to gain 2 :experience:.<br><br>— OR —<br><br>:pay: 3 :valuables: to gain 2 :experience:. |
| Warrior's Tomb | [**Search (2)**](../keywords/search.md) the [:artifact:](../artifacts/index.md) deck twice.<br>Draw 2 [Negative Morale](../keywords/morale.md#negative) cards. |
| Water Wheel | Gain 3 :gold:. |
| Windmill | Gain 1 :valuables:. |
| Witch Hut | [**Search (1)**](../keywords/search.md) the [Ability](../abilities/index.md) deck. Add the card to your deck or discard it.<br><br>— OR —<br><br>[Remove](../keywords/remove.md) 1 card from your deck. |


### Adventure-Combat Card

Each card contains the Battle Reward and the Basic Reward, with the Battle Reward scaling based on which Combat Power (the number in the circle) the player chooses to challenge.

To resolve an Adventure Combat card, do the following:

- Choose one of the available Combat Powers (the number in the circle) from the card
- Select 2 of your [units](../units/index.md), add their :attack: values and roll 2 [Attack dice](../keywords/dice.md#attack-die)

If your total power is **equal or greater** than the chosen Combat Power:

- Take the Battle Reward corresponding to that Combat Power
- Take the Basic Reward

If your total power is **lower** than the chosen Combat Power:

- Take the Basic Reward
- Put a :paralysis: token on one of your [units](../units/index.md) that took part in this Combat

To get rid of the :paralysis: token, choose the [unit](../units/index.md) for Combat - do not add its :attack: to your power, then remove the :paralysis: token.


| Name | Battle Reward | Basic Reward |
| :--- | :--- | :---: |
| Crypt | 4 ➣ Roll and resolve 1 [:treasure_die:](../keywords/dice.md#treasure-die).<br>5 ➣ Roll 2 [:treasure_die:](../keywords/dice.md#treasure-die) and resolve 1 of them.<br>7 ➣ Roll 3 [:treasure_die:](../keywords/dice.md#treasure-die) and resolve 1 of them. | :experience: [:negative_morale:](../keywords/morale.md#negative) |
| Cyclops Stockpile | 6 ➣ Gain 3 :building_materials:.<br>8 ➣ Gain 5 :building_materials: and 1 :valuables:.<br>10 ➣ Gain 8 :building_materials:, 2 :valuables:, and 1 :experience:. | :experience: |
| Dragon Utopia | 6 ➣ Roll and resolve 1 [:resource_die:](../keywords/dice.md#resource-die). Gain 1 [:artifact:](../artifacts/index.md).<br>10 ➣ Roll and resolve 2 [:resource_die:](../keywords/dice.md#resource-die). Gain 1 [:artifact:](../artifacts/index.md).<br>12 ➣ Roll and resolve 2 [:resource_die:](../keywords/dice.md#resource-die). Gain 2 [:artifact:](../artifacts/index.md) and 1 :experience:. | :experience: |
| Dwarven Treasury | 6 ➣ Gain 5 :gold: or 1 :valuables:.<br>8 ➣ Gain 5 :gold: and 1 :valuables:.<br>11 ➣ Gain 10 :gold:, 3 :valuables:, and 1 :experience:. | :experience: |
| Imp Cache | 5 ➣ Roll and resolve 1 [:resource_die:](../keywords/dice.md#resource-die).<br>7 ➣ Roll and resolve 2 [:resource_die:](../keywords/dice.md#resource-die).<br>9 ➣ Roll and resolve 3 [:resource_die:](../keywords/dice.md#resource-die). | :experience: |
