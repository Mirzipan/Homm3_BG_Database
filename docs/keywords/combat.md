# Combat

## Statistics

All [units](../units/index.md) have the following statistics shown on their cards.

| Symbol | Name | Meaning |
| :---: | :--- | :--- |
| :attack: | Attack | How much damage this unit will deal to another unit. |
| :defense: | Defense | Decreases the damage received from non-magical sources — damage received cannot be less than 0. |
| :health_points: | Health Points | How much damage this unit can receive, before being removed from Combat. |
| :initiative: | Initiative | How fast the unit is. Higher number means they'll get to activate sooner in Combat. |


## Damage

Also shown as :damage:.

Should a [unit](../units/index.md) receive damage from any source, it will be subtracted from its [health points](combat.md#statistics) directly. The [defense value](combat.md#statistics) only reduces the [attack value](combat.md#statistics) of the attacking [unit](../units/index.md), but not the damage received of the [unit](../units/index.md) that is being attacked.


## Obstacle

Any space that is occupied by a [unit](../units/index.md), an obstacle marker, a Wall or a Gate may not be stepped on.
[Flying units](../units/index.md#flying-units) may move through these spaces, but their movement is not allowed to end in such a space.


## Round

A combat round is a complete cycle of activations during Combat. At the start of a round, determine the order of activation for all participating [units](../units/index.md), usually by their :initiative: value from highest to lowest.

During a round, each eligible unit normally gains one activation in this order. When a unit activates, it may move and/or perform actions as allowed by the rules of the game. After all units that can act this round have taken their activation (or passed), the round ends.

When a new round begins, repeat the process of determining activation order if required by the scenario or rules. Some effects or abilities may last until the end of the current round or trigger at the start or end of a round.