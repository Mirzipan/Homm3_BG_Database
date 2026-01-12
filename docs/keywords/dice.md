# Dice

There are 3 types of dice used throughout the game.


## Attack Die

A die most commonly used during Combat to modify the damage dealt or resolve a special ability of a [Unit](../units/index.md).

| Side | Count | Effect |
| :---: | :---: | :-- |
| -1 | 2 |-1 :attack:. |
| 0 | 2 |No change to :attack:. |
| +1 | 2 | +1 :attack: |


## Resource Die

A Resource die (also shown as :resource_die:) is used to determine how much of which Resource the Player gains. Each side is unique and all 3 Resources are represented equally, with each having a lower value and a higher value, where the higher value is double of the lower one.

| Sides |
| :---: |
| 3 :gold: |
| 6 :gold: |
| 2 :building_materials: |
| 4 :building_materials: |
| 1 :valuables: |
| 2 :valuables: |


## Treasure Die

The Treasure Die (also shown as :treasure_die:) is commonly used to reward the Player.

| Side | Count | Effect |
| :---: |  :---: | :--- |
| :experience: | 2 | The player’s Main [Hero](../heroes/index.md) gains half an Experience Level. |
| [:artifact:](../artifacts/index.md) | 2 |[**Search(2)**](search.md) the [Artifact](../artifacts/index.md) deck. |
| [:resource_die:](dice.md#resource-die) | 1 | Roll and resolve 1 [Resource die](dice.md#resource-die). |
| 2 [:resource_die:](dice.md#resource-die) | 1 | Roll 2 [Resource dice](dice.md#resource-die) and choose one result. |


## Notes

- When resolving a special ability of a [Unit](../units/index.md) or something outside of Combat, the typical effects of each side are instead replaced by whatever other mechanic is currently requiring an Attack die roll.
