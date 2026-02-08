# AI

## Combat

AI Combat rules are the same, regardless of fighting against [Neutral](../units/index.md#neutral-units) or Enemy AI units.


### Initiative

Just like non-AI combat, the unit with the highest [:initiative:](../units/index.md#statistics) goes first. In case of a tie, the attacking [Hero](../heroes/index.md) has priority. If both sides have units with the same initiative, they activate in an alternating fashion, so first the attacker, then the defender.

When fighting an AI [Hero](../heroes/index.md), every time one of their [units](../units/index.md) activates, draw a card from their AI and resolve the effect in their stead. The strength of the effect depends on the [game difficulty](../difficulties.md).

| Card | Type | Effect | Easy | Normal | Expert | Impossible |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Attack | :might: | The [unit](../units/index.md) that is about to attack gains... | ...nothing. | +1 :attack: | +1 :attack: | +2 :attack: |
| Attack | :might: | The [unit](../units/index.md) that is about to attack gains... | +1 :attack: | +1 :attack: | +2 :attack: | +2 :attack: |
| Defense | :might: | Put this card on the [unit](../units/index.md) with the highest :health_points: in the army.<br>When this [unit](../units/index.md) is about to be attacked, it gains... | ...nothing. | +1 :defense: | +1 :defense: | +2 :defense: |
| Defense | :might: | Put this card on the [unit](../units/index.md) that is to activate next.<br>When this [unit](../units/index.md) is about to be attacked, it gains... | +1 :defense: | +1 :defense: | +2 :defense: | +2 :defense: |
| Cast a spell | :magic: | Draw a [spell](../spells/index.md) and cast it on the [unit](../units/index.md) with the highest :defense: in:<br>1. The player's army, if it inflicts damage or special status, or decreases the [unit's statistics](../units/index.md#statistics).<br>2. The AI's army, if it increases the [unit's statistics](../units/index.md#statistics).<br>The [spell](../spells/index.md) is cast with... | 0 :power: | 1 :power: | 1 :power: | 2 :power: |
| Cast a spell | :magic: | Draw a [spell](../spells/index.md) and cast it on the [unit](../units/index.md) with the highest :defense: in:<br>1. The player's army, if it inflicts damage or special status, or decreases the [unit's statistics](../units/index.md#statistics).<br>2. The AI's army, if it increases the [unit's statistics](../units/index.md#statistics).<br>The [spell](../spells/index.md) is cast with... | 0 :power: | 1 :power: | 2 :power: | 3 :power: |
| Use a skill | :skill: | Use the [skill](../abilities/index.md) described in the scenario. And... | ...nothing more. | ...nothing more. | ...do it again. | ...do it again. |
| Use a skill | :skill: | Use the [skill](../abilities/index.md) described in the scenario. And... | ...nothing more. | ...if it is the first [Combat round](../keywords/combat.md#round), shuffle this card back into the AI deck. | ...if it is the first [Combat round](../keywords/combat.md#round), shuffle this card back into the AI deck. | ...do it again. |


### Targeting

The targeting priorities below assume that conditions are checked from the top and the first matching target is then selected.

| Attacker | Priorities |
| :---: | :--- |
| :bronze:&nbsp;:unit_ground: | - :bronze:<br>- :silver:<br>- :golden:<br>- :azure: |
| :silver:&nbsp;:unit_ground: | - :silver:<br>- :bronze:<br>- :golden:<br>- :azure: |
| :golden:&nbsp;:unit_ground: | - :golden:<br>- :silver:<br>- :bronze:<br>- :azure: |
| :azure:&nbsp;:unit_ground: | - :azure:<br>- :golden:<br>- :silver:<br>- :bronze: |
| :bronze:&nbsp;:unit_flying: | - :bronze:<br>- :silver:<br>- :golden:<br>- :azure: |
| :silver:&nbsp;:unit_flying: | - :silver:<br>- :bronze:<br>- :golden:<br>- :azure: |
| :golden:&nbsp;:unit_flying: | - :golden:<br>- :silver:<br>- :bronze:<br>- :azure: |
| :azure:&nbsp;:unit_flying: | - :azure:<br>- :golden:<br>- :silver:<br>- :bronze: |
| :bronze:&nbsp;:unit_ranged: | - :bronze:&nbsp;:unit_ranged:<br>- :silver:&nbsp;:unit_ranged:<br>- :golden:&nbsp;:unit_ranged:<br>- :azure:&nbsp;:unit_ranged:<br>- :bronze:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :silver:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :golden:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :azure:&nbsp;:unit_ground:&nbsp;:unit_flying: |
| :silver:&nbsp;:unit_ranged: | - :silver:&nbsp;:unit_ranged:<br>- :bronze:&nbsp;:unit_ranged:<br>- :golden:&nbsp;:unit_ranged:<br>- :azure:&nbsp;:unit_ranged:<br>- :silver:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :bronze:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :golden:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :azure:&nbsp;:unit_ground:&nbsp;:unit_flying: |
| :golden:&nbsp;:unit_ranged: | - :golden:&nbsp;:unit_ranged:<br>- :silver:&nbsp;:unit_ranged:<br>- :bronze:&nbsp;:unit_ranged:<br>- :azure:&nbsp;:unit_ranged:<br>- :golden:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :silver:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :bronze:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :azure:&nbsp;:unit_ground:&nbsp;:unit_flying: |
| :azure:&nbsp;:unit_ranged: | - :azure:&nbsp;:unit_ranged:<br>- :golden:&nbsp;:unit_ranged:<br>- :silver:&nbsp;:unit_ranged:<br>- :bronze:&nbsp;:unit_ranged:<br>- :azure:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :golden:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :silver:&nbsp;:unit_ground:&nbsp;:unit_flying:<br>- :bronze:&nbsp;:unit_ground:&nbsp;:unit_flying: |

In case there's more than one valid target, attack the closest one. If there is a tie between equally valid targets, the player chooses which [Unit](../units/index.md) to attack.


## Movement

AI [Heroes](../heroes/index.md) have 3 MP (:movement:), which they spend to perform the following actions in descending priority:

- If a player's [Hero](../heroes/index.md) is on the same [Tile](../tiles/index.md) as the AI, spend all MP to move towards them and attempty to start [Combat](../keywords/index.md).
- If there are any [Mines](../fields/mine.md) or [Settlements](../fields/settlement.md) that can be flagged, move towards the closest one.
- Move towards the player's [Town](../towns/index.md).
