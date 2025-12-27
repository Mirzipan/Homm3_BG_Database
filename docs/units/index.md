# Units


## Tiers

Units are divided into 4 tiers, based on their level of power:

- :bronze: - Bronze tier
- :silver: - Silver tier
- :golden: - Gold tier
- :azure: - Azure tier - only [Neutral Units](index.md#neutral-units) exist in this tier


## Types

There are 3 types of units:

- [:unit_ground: Ground Units](index.md#ground-units)
- [:unit_ranged: Ranged Units](index.md#ranged-units)
- [:unit_flying: Flying Units](index.md#flying-units)


## Statistics

All units have the following statistics shown on their cards.

| Symbol | Name | Meaning |
| :---: | :--- | :--- |
| :attack: | Attack | How much damage this unit will deal to another unit. |
| :defense: | Defense | Decreases the damage received from non-magical sources — damage received cannot be less than 0. |
| :health_points: | Health Points | How much damage this unit can receive, before being removed from Combat. |
| :initiative: | Initiative | How fast the unit is. Higher number means they'll get to activate sooner in Combat. |


## Symbols

The following symbols are commonly used with the association of units or their abilities.

| Symbol | Meaning |
| :---: | :--- |
| :empower: | Spell Power |
| :damage: | Damage |
| :unit_passive: | Effect is always active. |
| :activation: | Effect activates when this unit activates. |
| :unit_other: | Effect can be activated instead of moving and attacking. |
| :unit_attack: | Effect activates when this unit attacks another unit. |
| :unit_retaliate: | Effect activates when this unit retaliates against an attacker. |
| :effect_map: | Effect can be activated outside of Combat. |


## Ground Units

Also shown as :unit_ground:.

Units that move on the ground and can only attack adjacent units.

- [^1] Ground units may move up to 3 spaces in Combat on the small battlefield. On the [large battlefield](../content/battlefield_expansion.md), their movement range is equal to their :initiative: value instead.
- Ground units may move first and then attack during their activation.


## Ranged Units

Also shown as :unit_ranged:.

Units that move on the ground and can also attack units that are not adjacent to them.

- [^1] Ranged units may move up to 1 space in Combat on the small battlefield. On the [large battlefield](../content/battlefield_expansion.md), their movement range is equal to their :initiative: value instead.
- [^1] Ranged units may attack first, and then move. On the [large battlefield](../content/battlefield_expansion.md) they can either move or attack.
- Should an enemy unit occupy any space that is adjacent to the ranged unit, the ranged unit can only attack the adjacent unit.
- Should there be no enemy unit adjacent to the ranged unit, the ranged unit may attack an enemy unit anywhere on the battlefield.
- [^1] Should the ranged attack originate in the back row of the battlefield and the attacked unit is in the opposite back row of the battlefield, a ranged penalty applies. On the [large battlefield](../content/battlefield_expansion.md), the ranged penalty applied when attacking a unit that is 8 or more hexes away.
- There is no retaliation against a ranged attack. There is, however, retaliation if the ranged unit attacks a unit that is adjacent to it.


## Flying Units

Also shown as :unit_flying:.

Flying units move through the air and can only attack adjacent units.

- [^1] Flying units may move up to 3 spaces in Combat on the small battlefield. On the [large battlefield](../content/battlefield_expansion.md), their movement range is equal to their :initiative: value instead.
- [^1] Flying units may attack first, and then move. On the [large battlefield](../content/battlefield_expansion.md), their movement always comes first.
- Flying units may move first and then attack during their activation.
- Flying units may move over obstacles, as long as their movement ends on an empty space.


## Neutral Units

Neutral units are variants of regular units, expect they are only used in Neutral Unit Combat.
There are some [Ability](../abilities/index.md), [Astrologers Proclaim](../astrologers_proclaim/index.md), [Event](../events/index.md), and [Hero](../heroes/index.md) specialty cards that allow the player to [Recruit](../keywords/recruit.md) Neutral Units.



## Summoned Units

These units can only comes into Combat by someone casting a summoning [spell](../spells/index.md).
None of these units can be [Recruited](../keywords/recruit.md) normally.

There are currently 4 summoning spells:

- [Summon Air Elemental](../spells/summon_air_elemental.md)
- [Summon Earth Elemental](../spells/summon_earth_elemental.md)
- [Summon Fire Elemental](../spells/summon_fire_elemental.md)
- [Summon Water Elemental](../spells/summon_water_elemental.md)


## Creature Bank Units

Special units that are only used when challenging the guards of a [Creature Bank](../fields/creature_bank.md).
None of these units can be [Recruited](../keywords/recruit.md) normally.


## Other Units

Although these are not strictly speaking Units, they can be part of Combat and have either Unit-like statistics or effects.

- [Arrow Tower](arrow_tower.md)
- [War Machines](../war_machines/index.md)


## List of Units

For the "Few" and "Pack" version of the same unit, stat changes are shown in **bold**.

| Name | Town | # |Tier | Type | :attack: | :defense: | :health_points: | :initiative: | Recruitment Cost | Abilities | Content |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | ---: | :--- | :--- |
| [Halberdiers](halberdiers.md) | [Castle](../towns/castle.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 2 | 4 | 2 :gold: | - | [Core Game](../content/core_game.md) |
| [Halberdiers](halberdiers.md) | [Castle](../towns/castle.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 1 | 2 | **5** | 3 :gold: | :unit_passive: When the unit is targeted by any attack, you can discard a card and ignore the [Attack die's](../keywords/dice.md#attack-die) roll result. | [Core Game](../content/core_game.md) |
| [Marksmen](marksmen.md) | [Castle](../towns/castle.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 2 | 4 | 3 :gold: | - | [Core Game](../content/core_game.md) |
| [Marksmen](marksmen.md) | [Castle](../towns/castle.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 2 | **6** | 5 :gold: | :unit_attack: If a target is a non-adjacent unit, attack this target again. | [Core Game](../content/core_game.md) |
| [Griffins](griffins.md) | [Castle](../towns/castle.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 4 | 6 | 4 :gold: | :unit_retaliate: This unit can perform an unlimited number of Retaliation Attacks. | [Core Game](../content/core_game.md) |
| [Griffins](griffins.md) | [Castle](../towns/castle.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | **3** | 0 | 4 | **9** | 6 :gold: | :unit_retaliate: This unit can perform an unlimited number of Retaliation Attacks. | [Core Game](../content/core_game.md) |
| [Crusaders](crusaders.md) | [Castle](../towns/castle.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 4 | 5 | 6 :gold: | - | [Core Game](../content/core_game.md) |
| [Crusaders](crusaders.md) | [Castle](../towns/castle.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | **4** | 2 | 4 | **6** | 10 :gold: | :unit_attack: You can reroll every "0" on this unit's [Attack die](../keywords/dice.md#attack-die). | [Core Game](../content/core_game.md) |
| [Zealots](zealots.md) | [Castle](../towns/castle.md) | Few | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 1 | 5 | 5 | 8 :gold: | - | [Core Game](../content/core_game.md) |
| [Zealots](zealots.md) | [Castle](../towns/castle.md) | Pack | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | **4** | 1 | 5 | **7** | 12 :gold: | :unit_passive: Ignore the combat penalty against adjacent units. | [Core Game](../content/core_game.md) |
| [Champions](champions.md) | [Castle](../towns/castle.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 2 | 7 | 7 | 12 :gold: | :effect_map: If your hero is on a field with Stables, this unit's reinforcement cost is reduced by 6 :gold:. | [Core Game](../content/core_game.md) |
| [Champions](champions.md) | [Castle](../towns/castle.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 2 | 7 | **9** | 20 :gold:<br>1 :valuables: | :unit_attack: If this unit's movement ends in a space other than where it started, you may reroll an [Attack die](../keywords/dice.md#attack-die). | [Core Game](../content/core_game.md) |
| [Archangels](archangels.md) | [Castle](../towns/castle.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 3 | 8 | 12 | 20 :gold:<br>1 :valuables: | :unit_passive: When combat begins, draw 1 card. | [Core Game](../content/core_game.md) |
| [Archangels](archangels.md) | [Castle](../towns/castle.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **7** | 3 | **10** | **18** | 30 :gold:<br>2 :valuables: | :unit_passive: Once per Combat. Cancel an attack that would reduce another unit's :health_points: to 0. | [Core Game](../content/core_game.md) |
| [Skeletons](skeletons.md) | [Necropolis](../towns/necropolis.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 2 | 4 | 2 :gold: | - | [Core Game](../content/core_game.md) |
| [Skeletons](skeletons.md) | [Necropolis](../towns/necropolis.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 1 | 2 | **5** | 3 :gold: | - | [Core Game](../content/core_game.md) |
| [Zombies](zombies.md) | [Necropolis](../towns/necropolis.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 3 | 3 :gold: | :unit_passive: If the attacker resolves a "+1" on [Attack die](../keywords/dice.md#attack-die), gain +1 :defense:. | [Core Game](../content/core_game.md) |
| [Zombies](zombies.md) | [Necropolis](../towns/necropolis.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | **4** | 4 :gold: | :unit_passive: If the attacker resolves a "0" or a +1" on [Attack die](../keywords/dice.md#attack-die), gain +1 :defense:. | [Core Game](../content/core_game.md) |
| [Wraiths](wraiths.md) | [Necropolis](../towns/necropolis.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 3 | 5 | 4 :gold: | :activation: Remove up to 1 :damage: from this unit. | [Core Game](../content/core_game.md) |
| [Wraiths](wraiths.md) | [Necropolis](../towns/necropolis.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | **5** | **7** | 6 :gold: | :activation: Remove up to 1 :damage: from this unit, then discard 1 random card from the enemy's hand. | [Core Game](../content/core_game.md) |
| [Vampires](vampires.md) | [Necropolis](../towns/necropolis.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 4 | 1 | 4 | 6 | 8 :gold: | :unit_attack: Ignore the Retaliation Attack. | [Core Game](../content/core_game.md) |
| [Vampires](vampires.md) | [Necropolis](../towns/necropolis.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | **5** | 1 | 4 | **9** | 12 :gold: | :unit_attack: Ignore the Retaliation Attack. Then remove up to 2 :damage: from this unit. | [Core Game](../content/core_game.md) |
| [Liches](liches.md) | [Necropolis](../towns/necropolis.md) | Few | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 1 | 5 | 6 | 8 :gold: | - | [Core Game](../content/core_game.md) |
| [Liches](liches.md) | [Necropolis](../towns/necropolis.md) | Pack | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | **4** | 1 | 5 | **7** | 14 :gold: | :unit_attack: Choose a unit adjacent to the target and attack it. For the purpose of this attack, your :attack: is 2. | [Core Game](../content/core_game.md) |
| [Dread Knights](dread_knights.md) | [Necropolis](../towns/necropolis.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 2 | 7 | 7 | 12 :gold: | :unit_attack: When retaliating after this attack, the enemy rolls 2 [Attack dice](../keywords/dice.md#attack-die) and resolves the lower result. | [Core Game](../content/core_game.md) |
| [Dread Knights](dread_knights.md) | [Necropolis](../towns/necropolis.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 2 | 7 | **9** | 20 :gold:<br>1 :valuables: | :unit_attack: If you resolve a "0" or a "+1" on the [Attack die](../keywords/dice.md#attack-die), increase this unit's total attack value by another "+1". | [Core Game](../content/core_game.md) |
| [Ghost Dragons](ghost_dragons.md) | [Necropolis](../towns/necropolis.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 3 | 8 | 9 | 19 :gold:<br>1 :valuables: | :activation: Discard the enemy's :morale_positive: token. | [Core Game](../content/core_game.md) |
| [Ghost Dragons](ghost_dragons.md) | [Necropolis](../towns/necropolis.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **7** | 3 | **9** | **14** | 32 :gold:<br>2 :valuables: | :activation: Discard the enemy's :morale_positive: token.<br>:unit_attack: Add +1 to your [Attack die](../keywords/dice.md#attack-die) result. | [Core Game](../content/core_game.md) |
| [Troglodytes](troglodytes.md) | [Dungeon](../towns/dungeon.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 2 | 4 | 2 :gold: | - | [Core Game](../content/core_game.md) |
| [Troglodytes](troglodytes.md) | [Dungeon](../towns/dungeon.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 1 | 2 | **5** | 3 :gold: | :unit_passive: This unit ignores :paralysis: effect. | [Core Game](../content/core_game.md) |
| [Harpies](harpies.md) | [Dungeon](../towns/dungeon.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 3 | 6 | 3 :gold: | :unit_attack: After the enemy's Retaliation Attack, this unit can return to the space from which it moved to attack. | [Core Game](../content/core_game.md) |
| [Harpies](harpies.md) | [Dungeon](../towns/dungeon.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | **3** | 0 | 3 | **9** | 5 :gold: | :unit_attack: Ignore the Retaliation Attack. This unit can return to the space from which it moved to attack. | [Core Game](../content/core_game.md) |
| [Evil Eyes](evil_eyes.md) | [Dungeon](../towns/dungeon.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 3 | 5 | 4 :gold: | - | [Core Game](../content/core_game.md) |
| [Evil Eyes](evil_eyes.md) | [Dungeon](../towns/dungeon.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | **1** | 3 | **7** | 6 :gold: | :unit_passive: Ignore the combat penalty against adjacent units. | [Core Game](../content/core_game.md) |
| [Medusas](medusas.md) | [Dungeon](../towns/dungeon.md) | Few | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 1 | 4 | 5 | 6 :gold: | :unit_passive: After the Retaliation Attack, roll an [Attack die](../keywords/dice.md#attack-die), on a "0" the target is :paralysis:. | [Core Game](../content/core_game.md) |
| [Medusas](medusas.md) | [Dungeon](../towns/dungeon.md) | Pack | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | **4** | 1 | 4 | **6** | 12 :gold: | :unit_passive: Ignore the combat penalty against adjacent units.<br>:unit_retaliate: The target gains :paralysis:. | [Core Game](../content/core_game.md) |
| [Minotaurs](minotaurs.md) | [Dungeon](../towns/dungeon.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 4 | 6 | 8 :gold: | :unit_attack: If you resolve a "-1" on the [Attack die](../keywords/dice.md#attack-die), draw a card, | [Core Game](../content/core_game.md) |
| [Minotaurs](minotaurs.md) | [Dungeon](../towns/dungeon.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | **5** | 2 | 4 | **8** | 14 :gold: | :unit_attack: If you resolve a "-1" on the [Attack die](../keywords/dice.md#attack-die), draw a card, | [Core Game](../content/core_game.md) |
| [Manticores](manticores.md) | [Dungeon](../towns/dungeon.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 1 | 6 | 7 | 10 :gold: | - | [Core Game](../content/core_game.md) |
| [Manticores](manticores.md) | [Dungeon](../towns/dungeon.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 1 | 6 | **11** | 18 :gold:<br>1 :valuables: | :unit_attack: For this attack, ignore the :defense: value from the target unit's card. | [Core Game](../content/core_game.md) |
| [Manticores](manticores.md) | [Dungeon](../towns/dungeon.md) | Pack Alt | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | **2** | 6 | **11** | 18 :gold:<br>1 :valuables: | :unit_attack: After the Attack, roll an [Attack die](../keywords/dice.md#attack-die), on a "0" or a "+1" the target is :paralysis:. | [Regular Stretch Goals 2024](../content/regular_stretch_goals.md) |
| [Black Dragons](black_dragons.md) | [Dungeon](../towns/dungeon.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 3 | 8 | 11 | 19 :gold:<br>1 :valuables: | :unit_passive: Reduce :damage: taken by this unit from [:spellpower:](../spells/index.md) by 2 to a minimum of 0. | [Core Game](../content/core_game.md) |
| [Black Dragons](black_dragons.md) | [Dungeon](../towns/dungeon.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **8** | 3 | 8 | **15** | 33 :gold:<br>2 :valuables: | :unit_passive: Ignore any [:spellpower:](../spells/index.md) effects and :damage: from [Specialty](../heroes/index.md). | [Core Game](../content/core_game.md) |
| [Gremlins](gremlins.md) | [Tower](../towns/tower.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 2 | 4 | 0 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Gremlins](gremlins.md) | [Tower](../towns/tower.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 2 | **5** | 2 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Gargoyles](gargoyles.md) | [Tower](../towns/tower.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 1 | 3 | 6 | 3 :gold: | :unit_passive: This unit ignores any :ongoing: [Spell](../spells/index.md) effects. | [Tower Expansion](../content/tower_expansion.md) |
| [Gargoyles](gargoyles.md) | [Tower](../towns/tower.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | **3** | 1 | 3 | **9** | 4 :gold: | :unit_passive: This unit ignores any :ongoing: [Spell](../spells/index.md) effects. | [Tower Expansion](../content/tower_expansion.md) |
| [Iron Golems](iron_golems.md) | [Tower](../towns/tower.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 1 | 3 | 4 | 4 :gold: | :unit_passive: This unit reduces any :damage: it takes from [spells](../spells/index.md) by 1 - to a minimum of 0. | [Tower Expansion](../content/tower_expansion.md) |
| [Iron Golems](iron_golems.md) | [Tower](../towns/tower.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 3 | **2** | 3 | **5** | 7 :gold: | :unit_passive: This unit reduces any :damage: it takes from [spells](../spells/index.md) by 2 - to a minimum of 0. | [Tower Expansion](../content/tower_expansion.md) |
| [Magi](magi.md) | [Tower](../towns/tower.md) | Few | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 4 | 5 | 6 :gold: | :unit_attack: Ignore combat penalties. | [Tower Expansion](../content/tower_expansion.md) |
| [Magi](magi.md) | [Tower](../towns/tower.md) | Pack | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | **4** | **1** | 4 | 6 | 11 :gold: | :unit_attack: Ignore combat penalties. :activation: Add +1 :empower: to the first [spell](../spells/index.md) you cast this round. | [Tower Expansion](../content/tower_expansion.md) |
| [Genies](genies.md) | [Tower](../towns/tower.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | 6 | 7 | 8 :gold: | :unit_other: Discard 3 cards from your deck and take a [:spellpower:](../spells/index.md) discarded this way to your hand. | [Tower Expansion](../content/tower_expansion.md) |
| [Genies](genies.md) | [Tower](../towns/tower.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | **4** | 1 | 6 | **8** | 12 :gold: | :unit_attack: Discard 3 cards from your deck and take a [:spellpower:](../spells/index.md) discarded this way to your hand. | [Tower Expansion](../content/tower_expansion.md) |
| [Nagas](nagas.md) | [Tower](../towns/tower.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 2 | 7 | 6 | 13 :gold: | :unit_attack: Ignore Retaliation Attacks. | [Tower Expansion](../content/tower_expansion.md) |
| [Nagas](nagas.md) | [Tower](../towns/tower.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 2 | 7 | **8** | 18 :gold:<br>1 :valuables: | :unit_attack: Ignore Retaliation Attacks. | [Tower Expansion](../content/tower_expansion.md) |
| [Titans](titans.md) | [Tower](../towns/tower.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 6 | 3 | 8 | 7 | 18 :gold:<br>1 :valuables: | :unit_passive: Ignore any :ongoing: effects on this unit. | [Tower Expansion](../content/tower_expansion.md) |
| [Titans](titans.md) | [Tower](../towns/tower.md) | Pack | :golden: | [:unit_ranged:](../keywords/ranged_unit.md) | 6 | 3 | 8 | **11** | 32 :gold:<br>2 :valuables: | :unit_passive: Ignore any :ongoing: effects on this unit and combat penalties against adjacent units. | [Tower Expansion](../content/tower_expansion.md) |
| [Centaurs](centaurs.md) | [Rampart](../towns/rampart.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 3 | 6 | 2 :gold: | - | [Rampart Expansion](../content/rampart_expansion.md) |
| [Centaurs](centaurs.md) | [Rampart](../towns/rampart.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 0 | 3 | **8** | 3 :gold: | - | [Rampart Expansion](../content/rampart_expansion.md) |
| [Dwarves](dwarves.md) | [Rampart](../towns/rampart.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 3 | 3 :gold: | :unit_passive: If this unit is targeted by any [Spell](../spells/index.md) or [Specialty](../heroes/index.md) card, roll 1 [Attack die](../keywords/dice.md#attack-die). On a "+1" result, ignore the card's effect. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Dwarves](dwarves.md) | [Rampart](../towns/rampart.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 1 | 3 | **5** | 4 :gold: | :unit_passive: If this unit is targeted by any [Spell](../spells/index.md) or [Specialty](../heroes/index.md) card, roll 1 [Attack die](../keywords/dice.md#attack-die). On a "+1" result, ignore the card's effect. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Elves](elves.md) | [Rampart](../towns/rampart.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 1 | 3 | 6 | 4 :gold: | - | [Rampart Expansion](../content/rampart_expansion.md) |
| [Elves](elves.md) | [Rampart](../towns/rampart.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | **3** | 1 | 3 | **7** | 7 :gold: | :unit_attack: If a target is a non adjacent unit, on a "-1" or "0" result, attack this target again. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Pegasi](pegasi.md) | [Rampart](../towns/rampart.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 5 | 8 | 6 :gold: | - | [Rampart Expansion](../content/rampart_expansion.md) |
| [Pegasi](pegasi.md) | [Rampart](../towns/rampart.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | **4** | 0 | **6** | **12** | 10 :gold: | :unit_passive: The :empower: of all enemy [spells](../spells/index.md) is reduced by 1 (to a minimum of 0). | [Rampart Expansion](../content/rampart_expansion.md) |
| [Dendroids](dendroids.md) | [Rampart](../towns/rampart.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 5 | 3 | 8 :gold: | - | [Rampart Expansion](../content/rampart_expansion.md) |
| [Dendroids](dendroids.md) | [Rampart](../towns/rampart.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | **6** | **4** | 15 :gold: | :unit_passive: Enemy units that start activation adjacent to this unit cannot move. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Unicorns](unicorns.md) | [Rampart](../towns/rampart.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 1 | 8 | 7 | 11 :gold: | :unit_passive: Reduce any :damage: from [:spellpower:](../spells/index.md) dealt to this unit by 1 (to a minimum of 0), | [Rampart Expansion](../content/rampart_expansion.md) |
| [Unicorns](unicorns.md) | [Rampart](../towns/rampart.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 1 | 8 | **9** | 18 :gold:<br>1 :valuables: | :unit_passive: Reduce any :damage: from [:spellpower:](../spells/index.md) dealt to this and adjacent friendly unit(s) by 1 (to a minimum of 0), | [Rampart Expansion](../content/rampart_expansion.md) |
| [Gold Dragons](gold_dragons.md) | [Rampart](../towns/rampart.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 3 | 9 | 10 | 22 :gold:<br>1 :valuables: | :unit_attack: Attack 2 spaces in a line. The first attack resolves normally, and the second has 2 :attack:, | [Rampart Expansion](../content/rampart_expansion.md) |
| [Gold Dragons](gold_dragons.md) | [Rampart](../towns/rampart.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **6** | 3 | **10** | **16** | 30 :gold:<br>2 :valuables: | :unit_attack: Attack 2 spaces in a line. The first attack resolves normally, and the second has 3 :attack:. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Gnolls](gnolls.md) | [Fortress](../towns/fortress.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 4 | 2 :gold: | - | [Fortress Expansion](../content/fortress_expansion.md) |
| [Gnolls](gnolls.md) | [Fortress](../towns/fortress.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | **4** | **5** | 3 :gold: | - | [Fortress Expansion](../content/fortress_expansion.md) |
| [Lizardmen](lizardmen.md) | [Fortress](../towns/fortress.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 3 | 4 | 3 :gold: | - | [Fortress Expansion](../content/fortress_expansion.md) |
| [Lizardmen](lizardmen.md) | [Fortress](../towns/fortress.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | **3** | 0 | 3 | **5** | 5 :gold: | - | [Fortress Expansion](../content/fortress_expansion.md) |
| [Dragon Flies](dragon_flies.md) | [Fortress](../towns/fortress.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 3 | 8 | 4 :gold: | :unit_attack: Remove all :ongoing: effects played on the target by the enemy player. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Dragon Flies](dragon_flies.md) | [Fortress](../towns/fortress.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | **1** | 3 | **12** | 7 :gold: | :unit_attack: Remove all :ongoing: effects played on the target by the enemy player. If the target retaliates, it suffers - 1 :attack:. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Basilisks](basilisks.md) | [Fortress](../towns/fortress.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 1 | 4 | 5 | 6 :gold: | :unit_attack: On "-1" outcomes on the [Attack die](../keywords/dice.md#attack-die), the attacked unit gains a :paralysis: token. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Basilisks](basilisks.md) | [Fortress](../towns/fortress.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 1 | **5** | **7** | 9 :gold: | :unit_attack: On "-1" outcomes on the [Attack die](../keywords/dice.md#attack-die), the attacked unit gains a :paralysis: token. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Gorgons](gorgons.md) | [Fortress](../towns/fortress.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 5 | 5 | 9 :gold: | - | [Fortress Expansion](../content/fortress_expansion.md) |
| [Gorgons](gorgons.md) | [Fortress](../towns/fortress.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | **5** | 2 | 5 | **6** | 14 :gold: | :unit_attack: After the attack, roll 2 [Attack dice](../keywords/dice.md#attack-die); on a double "0", decrease the target unit's :health_points: to 0. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Wyverns](wyverns.md) | [Fortress](../towns/fortress.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 1 | 8 | 7 | 12 :gold: | :unit_attack: Place 1 faction cube on the target. At the beginning of its every activation, remove it to inflict 1 :damage:. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Wyverns](wyverns.md) | [Fortress](../towns/fortress.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **6** | 1 | 8 | **11** | 18 :gold:<br>1 :valuables: | :unit_attack: Place 2 faction cubes on the target. At the beginning of its every activation, remove 1 of them to inflict 1 :damage:. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Hydras](hydras.md) | [Fortress](../towns/fortress.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 6 | 3 | 8 | 5 | 20 :gold:<br>1 :valuables: | :unit_attack: Ignore the Retaliation Attack. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Hydras](hydras.md) | [Fortress](../towns/fortress.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **7** | 3 | **10** | **7** | 28 :gold:<br>2 :valuables: | :unit_attack: Ignore the Retaliation Attack. This unit attacks up to 2 adjacent enemy units. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Familiars](familiars.md) | [Inferno](../towns/inferno.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 2 | 5 | 2 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Familiars](familiars.md) | [Inferno](../towns/inferno.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **3** | 1 | 2 | **7** | 3 :gold: | :unit_passive: Whenever an enemy casts a [:spellpower:](../spells/index.md) from hand, they must discard 1 card from hand. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Magogs](magogs.md) | [Inferno](../towns/inferno.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 2 | 4 | 3 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Magogs](magogs.md) | [Inferno](../towns/inferno.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | **3** | **6** | 5 :gold: | :unit_attack: When [Magogs](magogs.md) attack a target that is not adjacent to them, they also deal 1 :damage: to a unit adjacent to the target. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Cerberi](cerberi.md) | [Inferno](../towns/inferno.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 0 | 4 | 7 | 4 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Cerberi](cerberi.md) | [Inferno](../towns/inferno.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 3 | **1** | **5** | **8** | 7 :gold: | :unit_attack: Ignores Retaliation Attacks. Additionally, deals 1 :damage: to another enemy unit adjacent to Cerberi. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Demons](demons.md) | [Inferno](../towns/inferno.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 4 | 5 | 6 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Demons](demons.md) | [Inferno](../towns/inferno.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | **5** | **6** | 8 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Pit Lords](pit_lords.md) | [Inferno](../towns/inferno.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 1 | 6 | 6 | 8 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Pit Lords](pit_lords.md) | [Inferno](../towns/inferno.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | **5** | 1 | 6 | **7** | 15 :gold: | :unit_other: If one of your units has been removed from the board during this Combat, Summon or Reinforce [Demons](demons.md). | [Inferno Expansion](../content/inferno_expansion.md) |
| [Efreet](efreet.md) | [Inferno](../towns/inferno.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 1 | 7 | 9 | 12 :gold: | :unit_passive: Ignores any :damage: from [Magic Arrows](../spells/magic_arrow.md). | [Inferno Expansion](../content/inferno_expansion.md) |
| [Efreet](efreet.md) | [Inferno](../towns/inferno.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **6** | 1 | 7 | **13** | 18 :gold:<br>1 :valuables: | :unit_passive: Ignores any :damage: from [Magic Arrows](../spells/magic_arrow.md) or [spells](../spells/index.md) from the [Fire School of Magic](../spells/school_of_fire_magic.md). | [Inferno Expansion](../content/inferno_expansion.md) |
| [Arch Devils](arch_devils.md) | [Inferno](../towns/inferno.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 3 | 8 | 11 | 22 :gold:<br>1 :valuables: | :unit_attack: Ignores Retaliation Attacks. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Arch Devils](arch_devils.md) | [Inferno](../towns/inferno.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **7** | 3 | **9** | **15** | 30 :gold:<br>2 :valuables: | :unit_attack: Ignores Retaliation Attacks.<br>:unit_passive: As a regular movement, the Arch Devils can move to any empty space. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Goblins](goblins.md) | [Stronghold](../towns/stronghold.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 1 | 0 | 4 | 6 | 1 :gold: | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Goblins](goblins.md) | [Stronghold](../towns/stronghold.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | **2** | 0 | 4 | **8** | 2 :gold: | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Wolf Raiders](wolf_raiders.md) | [Stronghold](../towns/stronghold.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 3 | 7 | 3 :gold: | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Wolf Raiders](wolf_raiders.md) | [Stronghold](../towns/stronghold.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | **5** | **8** | 5 :gold: | :unit_attack: Attack this target again. The second attack happens after the target retaliates (if possible). | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Orcs](orcs.md) | [Stronghold](../towns/stronghold.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 1 | 4 | 4 | 4 | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Orcs](orcs.md) | [Stronghold](../towns/stronghold.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | **3** | 1 | **5** | **5** | 7 :gold: | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Ogres](ogres.md) | [Stronghold](../towns/stronghold.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 4 | 4 | 6 :gold: | :unit_other: Place a +1 :attack: token on a chosen [:unit_ground:](../keywords/ground_unit.md) or [:unit_flying:](../keywords/flying_unit.md) unit for 2 Combat rounds. | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Ogres](ogres.md) | [Stronghold](../towns/stronghold.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | **5** | **5** | 8 :gold: | :unit_other: Place a +2 :attack: token on a chosen [:unit_ground:](../keywords/ground_unit.md) or [:unit_flying:](../keywords/flying_unit.md) unit for 2 Combat rounds. | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Thunderbirds](thunderbirds.md) | [Stronghold](../towns/stronghold.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 4 | 1 | 6 | 9 | 8 :gold: | - | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Thunderbirds](thunderbirds.md) | [Stronghold](../towns/stronghold.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | **5** | 1 | 6 | **11** | 14 :gold: | :unit_passive: Right after this unit's attack and before any Retaliation, roll 1 [Attack die](../keywords/dice.md#attack-die), on a "+1", deal 1 :spell: :damage: to the target. | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Cyclopes](cyclopes.md) | [Stronghold](../towns/stronghold.md) | Few | :golden: | [:unit_ranged:](../keywords/ranged_unit.md) | 4 | 1 | 6 | 6 | 13 :gold: | :unit_other: This unit can destroy the Gate or a Wall. | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Cyclopes](cyclopes.md) | [Stronghold](../towns/stronghold.md) | Pack | :golden: | [:unit_ranged:](../keywords/ranged_unit.md) | **5** | 1 | **7** | **8** | 17 :gold:<br>1 :valuables: | :unit_other: This unit can destroy the Gate, a Wall, or the [Arrow Tower](arrow_tower.md). | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Behemoths](behemoths.md) | [Stronghold](../towns/stronghold.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 7 | 2 | 8 | 6 | 19 :gold:<br>1 :valuables: | :unit_attack: Decrease the target's :defense: by 1 (to a minimum of 0). | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Behemoths](behemoths.md) | [Stronghold](../towns/stronghold.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **8** | 2 | **10** | **9** | 29 :gold:<br>2 :valuables: | :unit_attack: Decrease the target's :defense: by 2 (to a minimum of 0). After the attack, place 1 Corrosion token on the target. | [Stronghold Expansion](../content/stronghold_expansion.md) |
| [Sprites](sprites.md) | [Conflux](../towns/conflux.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 2 | 7 | 2 :gold: | - | [Conflux Expansion](../content/conflux_expansion.md) |
| [Sprites](sprites.md) | [Conflux](../towns/conflux.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | **4** | **9** | 4 :gold: | :unit_attack: Ignore Enemy's Retaliation Attack. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Storm Elementals](storm_elementals.md)  | [Conflux](../towns/conflux.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 3 | 7 | 3 :gold: | - | [Conflux Expansion](../content/conflux_expansion.md) |
| [Storm Elementals](storm_elementals.md)  | [Conflux](../towns/conflux.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | **5** | **8** | 5 :gold: | :activation: Add +1 :empower: to the first [Air Magic](../spells/school_of_air_magic.md) spell you cast during this Activation. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Ice Elementals](ice_elementals.md)  | [Conflux](../towns/conflux.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 4 | 5 | 4 :gold: | - | [Conflux Expansion](../content/conflux_expansion.md) |
| [Ice Elementals](ice_elementals.md)  | [Conflux](../towns/conflux.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | **3** | 1 | **5** | **6** | 7 :gold: | :activation: Add +1 :empower: to the first [Water Magic](../spells/school_of_water_magic.md) spell you cast during this Activation. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Energy Elementals](energy_elementals.md) | [Conflux](../towns/conflux.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | 5 | 5 | 5 :gold: | - | [Conflux Expansion](../content/conflux_expansion.md) |
| [Energy Elementals](energy_elementals.md) | [Conflux](../towns/conflux.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | **4** | 1 | **6** | **8** | 8 :gold: | :activation: Add +1 :empower: to the first [Fire Magic](../spells/school_of_fire_magic.md) spell you cast during this Activation. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Magma Elementals](magma_elementals.md) | [Conflux](../towns/conflux.md) | Few | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 6 | 4 | 9 :gold: | - | [Conflux Expansion](../content/conflux_expansion.md) |
| [Magma Elementals](magma_elementals.md) | [Conflux](../towns/conflux.md) | Pack | :silver: | [:unit_ground:](../keywords/ground_unit.md) | **5** | 2 | **6** | **6** | 13 :gold: | :activation: Add +1 :empower: to the first [Earth Magic](../spells/school_of_earth_magic.md) spell you cast during this Activation. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Magic Elementals](magic_elementals.md) | [Conflux](../towns/conflux.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 2 | 7 | 7 | 12 :gold: | :unit_attack: Ignore Enemy's Retaliation Attack. Attack all adjacent units. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Magic Elementals](magic_elementals.md) | [Conflux](../towns/conflux.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 2 | **8** | **9** | 18 :gold:<br>1 :valuables: | :unit_attack: Ignore Enemy's Retaliation Attack. Attack all adjacent units. :unit_passive: Ignore any [:spell:](../spells/index.md) effects and :damage: from Specialty. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Phoenixes](phoenixes.md) | [Conflux](../towns/conflux.md) | Few | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 2 | 7 | 12 | 21 :gold:<br>1 :valuables: | :unit_passive: Once per Combat. When this unit's :health_points: drops to 0, set it to 1 instead. :unit_passive: Immune to [Fire Magic](../spells/school_of_fire_magic.md) :spell:. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Phoenixes](phoenixes.md) | [Conflux](../towns/conflux.md) | Pack | :golden: | [:unit_flying:](../keywords/flying_unit.md) | **7** | 2 | **9** | **18** | 27 :gold:<br>2 :valuables: | :unit_attack: Attack 2 spaces in a line. The first attack resolves normally, and the second has 2 :attack:. :unit_passive: Immune to [Fire Magic](../spells/school_of_fire_magic.md) :spell:. | [Conflux Expansion](../content/conflux_expansion.md) |
| [Oceanids](oceanids.md) | [Cove](../towns/cove.md) | Few | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 3 | 6 | 2 :gold: | - | [Cove Expansion](../content/cove_expansion.md) |
| [Oceanids](oceanids.md) | [Cove](../towns/cove.md) | Pack | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | **4** | **8** | 3 :gold: | :unit_passive: Ignore any effect from spells from the [School of Water Magic](../spells/school_of_water_magic.md). | [Cove Expansion](../content/cove_expansion.md) |
| [Seamen](seamen.md) | [Cove](../towns/cove.md) | Few | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 5 | 3 :gold: | - | [Cove Expansion](../content/cove_expansion.md) |
| [Seamen](seamen.md) | [Cove](../towns/cove.md) | Pack | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | **5** | **6** | 5 :gold: | :effect_map: +1 :movement: if you start the round on a Sea tile. | [Cove Expansion](../content/cove_expansion.md) |
| [Sea Dogs](sea_dogs.md) | [Cove](../towns/cove.md) | Few | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 4 | 6 | 4 :gold: | :unit_passive: Ignore the combat penalty against adjacent units. | [Cove Expansion](../content/cove_expansion.md) |
| [Sea Dogs](sea_dogs.md) | [Cove](../towns/cove.md) | Pack | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | **5** | **8** | 6 :gold: | :unit_attack: Ignore Enemy's Retaliation Attack.<br>:unit_passive: Ignore the combat penalty against adjacent units. | [Cove Expansion](../content/cove_expansion.md) |
| [Ayssids](ayssids.md) | [Cove](../towns/cove.md) | Few | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | 5 | 9 | 6 :gold: | - | [Cove Expansion](../content/cove_expansion.md) |
| [Ayssids](ayssids.md) | [Cove](../towns/cove.md) | Pack | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | **6** | **11** | 10 :gold: | :unit_attack: If the attack reduces the target to 0 :health_points:, the Ayssids can attack another unit adjacent to them. | [Cove Expansion](../content/cove_expansion.md) |
| [Sorceresses](sorceresses.md) | [Cove](../towns/cove.md) | Few | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 4 | 1 | 5 | 6 | 8 :gold: | :unit_other: Place a Weakness token on any unit for 2 Combat rounds. | [Cove Expansion](../content/cove_expansion.md) |
| [Sorceresses](sorceresses.md) | [Cove](../towns/cove.md) | Pack | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | **5** | 1 | **6** | 6 | 13 :gold: | :unit_attack: After the attack, place a Weakness token on the target for 2 Combat rounds. | [Cove Expansion](../content/cove_expansion.md) |
| [Nix](nix.md) | [Cove](../towns/cove.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 2 | 7 | 6 | 12 :gold: | - | [Cove Expansion](../content/cove_expansion.md) |
| [Nix](nix.md) | [Cove](../towns/cove.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 2 | **8** | **7** | 20 :gold:<br>1 :valuables: | :unit_passive: This unit cannot take more than 4 :damage: from a single attack. | [Cove Expansion](../content/cove_expansion.md) |
| [Haspids](haspids.md) | [Cove](../towns/cove.md) | Few | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 3 | 7 | 9 | 18 :gold:<br>1 :valuables: | :unit_attack: If this unit turns from Pack side in this combat, gain +2 :attack: | [Cove Expansion](../content/cove_expansion.md) |
| [Haspids](haspids.md) | [Cove](../towns/cove.md) | Pack | :golden: | [:unit_ground:](../keywords/ground_unit.md) | **6** | 3 | **9** | **12** | 32 :gold:<br>2 :valuables: | :unit_attack: Place 2 faction cubes on the target. At the beginning of its every activation, remove 1 of them to inflict 1 :damage:. | [Cove Expansion](../content/cove_expansion.md) |
| [Boars](boars.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 4 | 6 | 4 :gold: | - | [Core Game](../content/core_game.md) |
| [Centaurs](centaurs.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 5 | 7 | 3 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Cerberi](cerberi.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 5 | 8 | 10 :gold: | :unit_attack: Ignores Retaliation Attacks. Additionally, deals 1 :damage: to another enemy unit adjacent to Cerberi. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Dragon Flies](dragon_flies.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 3 | 8 | 7 :gold: | :unit_attack: Retaliation Attacks against Dragon Flies suffer -1 :attack:. | [Tower Expansion](../content/tower_expansion.md) |
| [Dwarves](dwarves.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 4 | 3 | 4 :gold: | :unit_passive: If this unit is targeted by any [Spell](../spells/index.md) or [Specialty](../heroes/index.md) card, roll 1 [Attack die](../keywords/dice.md#attack-die). On a "+1" result, ignore the card's effect. | [Tower Expansion](../content/tower_expansion.md) |
| [Elves](elves.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 1 | 3 | 6 | 7 :gold: | :unit_attack: If a target is a non adjacent unit, on a "-1" or "0" result, attack this target again. | [Tower Expansion](../content/tower_expansion.md) |
| [Evil Eyes](evil_eyes.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 1 | 3 | 6 | 6 :gold: | :unit_passive: Ignore the combat penalty against adjacent units. | [Core Game](../content/core_game.md) |
| [Familiars](familiars.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 1 | 2 | 7 | 6 :gold: | :unit_passive: Whenever an enemy cast a [:spellpower:](../spells/index.md) from hand, they must discard 1 card from hand. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Gargoyles](gargoyles.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 1 | 3 | 9 | 4 :gold: | :unit_passive: This unit ignores :paralysis: effect. | [Tower Expansion](../content/tower_expansion.md) |
| [Gnolls](gnolls.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 2 | 4 | 3 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Gremlins](gremlins.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 2 | 5 | 2 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Griffins](griffins.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 4 | 8 | 7 :gold: | :unit_retaliate: This unit can perform and unlimited number of Retaliation Attacks. | [Core Game](../content/core_game.md) |
| [Halberdiers](halberdiers.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 4 | 4 | 4 :gold: | :unit_passive: Treat allied adjacent units as if they had a Defense token. | [Core Game](../content/core_game.md) |
| [Halflings](halflings.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 3 | 6 | 5 :gold: | :unit_attack: Roll 2 [Attack dice](../keywords/dice.md#attack-die) and resolve the higher one. Ignore combat penalties. | [Core Game](../content/core_game.md) |
| [Harpies](harpies.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 4 | 8 | 5 :gold: | :unit_attack: Ignore the Retaliation Attack. This unit can return to the space from which it moved to attack. | [Core Game](../content/core_game.md) |
| [Iron Golems](iron_golems.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 4 | 3 | 6 :gold: | :unit_passive: Reduce any :damage: from [spells](../spells/index.md) by 2 - to a minimum of 0. | [Tower Expansion](../content/tower_expansion.md) |
| [Leprechaun](leprechaun.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 3 | 5 | 3 :gold: | | :unit_attack: Roll 2 [Attack dice](../keywords/dice.md#attack-die) and resolve the higher one. | [Regular Stretch Goals 2024](../content/regular_stretch_goals.md) |
| [Lizardmen](lizardmen.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 4 | 5 | 4 :gold: | - | [Tower Expansion](../content/tower_expansion.md) |
| [Magogs](magogs.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 4 | 6 | 8 :gold: | :unit_attack: When Magogs attack a target that is non adjacent to them, they also deal 1 :damage: to a unit adjacent to the target. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Marksmen](marksmen.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ranged:](../keywords/ranged_unit.md) | 2 | 0 | 3 | 5 | 7 :gold: | :unit_attack: If a target is a non-adjacent unit, attack this target again. | [Core Game](../content/core_game.md) |
| [Peasants](peasants.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 1 | 0 | 2 | 3 | 3 :gold: | :effect_map: At the beginning of each Resource round, gain 3 :gold:. | [Core Game](../content/core_game.md) |
| [Rogues](rogues.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 6 | 5 :gold: | :effect_map: Once during your turn, look at the top card from any deck, then put it back on the top or on the bottom of that deck. | [Core Game](../content/core_game.md) |
| [Skeletons](skeletons.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 3 | 4 | 3 :gold: | :unit_passive: After defeating Skeletons, if you control a [:necro: Hero](../towns/necropolis.md#heroes), immediately Reinforce 1 of your :bronze: units. | [Core Game](../content/core_game.md) |
| [Troglodytes](troglodytes.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 1 | 3 | 6 | 4 :gold: | :unit_passive: This unit ignores :paralysis: effects. | [Core Game](../content/core_game.md) |
| [Wraiths](wraiths.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_flying:](../keywords/flying_unit.md) | 2 | 0 | 4 | 7 | 7 :gold: | :activation: Remove up to 2 :damage: from this unit. | [Core Game](../content/core_game.md) |
| [Zombies](zombies.md) | [Neutral](../towns/neutral.md) | - | :bronze: | [:unit_ground:](../keywords/ground_unit.md) | 2 | 0 | 4 | 3 | 5 :gold: | :unit_passive: If the attacker resolves a "0" or a "+1" on an [Attack die](../keywords/dice.md#attack-die), gain +1 :defense: | [Core Game](../content/core_game.md) |
| [Basilisks](basilisks.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 1 | 4 | 5 | 12 :gold: | :unit_attack: After the attack, roll 1 [Attack die](../keywords/dice.md#attack-die). On a "0" result, :paralysis: the target. | [Tower Expansion](../content/tower_expansion.md) |
| [Crusaders](crusaders.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 4 | 5 | 11 :gold: | :unit_passive: During any attack, roll 2 [Attack dice](../keywords/dice.md#attack-die) and resolve the higher outcome. | [Core Game](../content/core_game.md) |
| [Demons](demons.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 0 | 8 | 6 | 13 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Dendroids](dendroids.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 6 | 3 | 12 :gold: | :unit_passive: Enemy units that start activation adjacent to this unit cannot move. | [Tower Expansion](../content/tower_expansion.md) |
| [Fangarm](fangarm.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | 5 | 8 | 14 :gold: | :unit_passive: Ignore all [:spellpower:](../spells/index.md) and [Specialty](../heroes/index.md) effects other than :damage:. | [Regular Stretch Goals 2024](../content/regular_stretch_goals.md) |
| [Genies](genies.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 1 | 4 | 9 | 11 :gold: | :unit_attack: When attacking [Efreet](efreet.md), this unit gains +1 :attack:. | [Tower Expansion](../content/tower_expansion.md) |
| [Gorgons](gorgons.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 4 | 5 | 13 :gold: | :unit_attack: After the attack, roll 2 [Attack dice](../keywords/dice.md#attack-die). On two "-1" results, reduce the attacked unit's :health_points: to 0. | [Tower Expansion](../content/tower_expansion.md) |
| [Liches](liches.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 6 | 7 | 12 :gold: | :unit_attack: Choose a unit adjacent to the target and attack it. For the purpose of this attack, your :attack: is 2. | [Core Game](../content/core_game.md) |
| [Magi](magi.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 5 | 6 | 11 :gold: | :unit_attack: Ignore combat penalties. After this unit's attack, the enemy discards a random card or a card with :empower:. | [Tower Expansion](../content/tower_expansion.md) |
| [Medusas](medusas.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 1 | 4 | 6 | 11 :gold: | :unit_passive: Ignore the combat penalty against adjacent units.<br>:unit_retaliate: The target is :paralysis:. | [Core Game](../content/core_game.md) |
| [Minotaurs](minotaurs.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 4 | 7 | 11 :gold: | :unit_attack: Reroll this unit's "-1" outcome on the [Attack die](../keywords/dice.md#attack-die). | [Core Game](../content/core_game.md) |
| [Mummies](mummies.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 1 | 4 | 5 | 8 :gold: | :unit_attack: Ignore the result on the [Attack die](../keywords/dice.md#attack-die). :unit_passive: Whenever this unit is attacked, set your opponent's [Attack die](../keywords/dice.md#attack-die) to "-1". | [Core Game](../content/core_game.md) |
| [Nomads](nomads.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 1 | 4 | 7 | 10 :gold: | :effect_map: At the end of your turn, move your [Hero's](../heroes/index.md) model to an adjacent empty field. | [Core Game](../content/core_game.md) |
| [Pegasi](pegasi.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 5 | 8 | 14 :gold: | :unit_passive: Whenever an enemy casts a [:spellpower:](../spells/index.md), they must discard an additional card with :empower:. | [Tower Expansion](../content/tower_expansion.md) |
| [Pit Lords](pit_lords.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 1 | 5 | 7 | 15 :gold: | - | [Inferno Expansion](../content/inferno_expansion.md) |
| [Satyrs](satyrs.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 0 | 5 | 7 | 11 :gold: | :effect_map: Roll a [die](../keywords/dice.md#attack-die). On a "-1" outcome, gain a :morale_positive: token. | [Regular Stretch Goals 2024](../content/regular_stretch_goals.md) |
| [Sharpshooters](sharpshooters.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 6 | 9 | 10 :gold: | :unit_attack: Ignore the combat penalties. | [Core Game](../content/core_game.md) |
| [Steel Golems](steel_golems.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 3 | 5 | 12 :gold: | :unit_passive: Reduce :damage: taken by this unit from [:spellpower:](../spells/index.md) or [Specialty](../heroes/index.md) by 2 - to a minimum of 0. | [Regular Stretch Goals 2024](../content/regular_stretch_goals.md) |
| [Vampires](vampires.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_flying:](../keywords/flying_unit.md) | 3 | 0 | 5 | 8 | 9 :gold: | :unit_attack: Ignore Enemy's Retaliation Attack. Then remove up to 2 :damage: from this unit. | [Core Game](../content/core_game.md) |
| [Zealots](zealots.md) | [Neutral](../towns/neutral.md) | - | :silver: | [:unit_ranged:](../keywords/ranged_unit.md) | 3 | 0 | 5 | 5 | 12 :gold: | :unit_passive: Ignore the combat penalty against adjacent units. | [Core Game](../content/core_game.md) |
| [Arch Devils](arch_devils.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 2 | 7 | 10 | 23 :gold: | :unit_attack: When attacking [Archangels](archangels.md), this unit gains +2 :attack:. | [Inferno Expansion](../content/inferno_expansion.md) |
| [Archangels](archangels.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 2 | 7 | 10 | 29 :gold: | :unit_attack: When attacking [Arch Devils](arch_devils.md), this unit gains +2 :attack:. | [Core Game](../content/core_game.md) |
| [Black Dragons](black_dragons.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 2 | 7 | 9 | 30 :gold: | :unit_attack: Attack 2 spaces in a line. The first attack resolves normally, and the second has 2 :attack:. | [Core Game](../content/core_game.md) |
| [Champions](champions.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 6 | 8 | 18 :gold: | :unit_attack: Roll 2 [Attack dice](../keywords/dice.md#attack-die) and apply both outcomes.<br>:unit_passive: Reroll this unit's all "-1" rolls. | [Core Game](../content/core_game.md) |
| [Diamond Golems](diamond_golems.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 2 | 6 | 6 | 16 :gold: | :unit_passive: Reduce any :damage: from [spells](../spells/index.md) by 3 - to a minimum of 0. | [Core Game](../content/core_game.md) |
| [Dread Knights](dread_knights.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 1 | 7 | 7 | 18 :gold: | :unit_passive: When this unit is targeted by a Retaliation Attack, it gains +1 :defense:. | [Core Game](../content/core_game.md) |
| [Efreet](efreet.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 4 | 2 | 6 | 13 | 20 :gold: | :unit_passive: Ignores any :damage: from [Magic Arrows](../spells/magic_arrow.md) or [spells](../spells/index.md) from the[Fire School of Magic](../spells/school_of_fire_magic.md). | [Inferno Expansion](../content/inferno_expansion.md) |
| [Enchanters](enchanters.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ranged:](../keywords/ranged_unit.md) | 4 | 1 | 5 | 5 | 16 :gold: | :activation: Remove up to 2 :damage: from a friendly unit. Otherwise, Enchanters gain +1 :attack:. | [Core Game](../content/core_game.md) |
| [Ghost Dragons](ghost_dragons.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 2 | 6 | 9 | 28 :gold: | :unit_attack: After the attack, roll 1 [Attack die](../keywords/dice.md#attack-die); if the result is "0", the target must immediately move away 1 space. | [Core Game](../content/core_game.md) |
| [Gold Golems](gold_golems.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 3 | 2 | 6 | 5 | 14 :gold: | :unit_passive: Reduce any :damage: from [spells](../spells/index.md) by 2 - to a minimum of 0. | [Core Game](../content/core_game.md) |
| [Manticores](manticores.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 4 | 1 | 7 | 8 | 18 :gold: | :unit_passive: On a "0" or a "+1" outcomes on the enemy's [Attack die](../keywords/dice.md#attack-die), gain +1 :defense:. | [Core Game](../content/core_game.md) |
| [Nagas](nagas.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 1 | 6 | 6 | 16 :gold: | :unit_attack: Ignore Retaliation Attacks. | [Tower Expansion](../content/tower_expansion.md) |
| [Trolls](trolls.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 4 | 0 | 7 | 7 | 13 :gold: | :activation: Remove up to 3 :damage: from this unit. | [Core Game](../content/core_game.md) |
| [Unicorns](unicorns.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_ground:](../keywords/ground_unit.md) | 5 | 1 | 7 | 7 | 18 :gold: | :unit_retaliate: The target is :paralysis:. | [Tower Expansion](../content/tower_expansion.md) |
| [Wyverns](wyverns.md) | [Neutral](../towns/neutral.md) | - | :golden: | [:unit_flying:](../keywords/flying_unit.md) | 4 | 1 | 7 | 8 | 17 :gold: | :unit_attack: After the attack, roll 1 [Attack die](../keywords/dice.md#attack-die). On a "0" result, deal 1 :damage: to the target unit. | [Tower Expansion](../content/tower_expansion.md) |
| [Azure Dragons](azure_dragons.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_flying:](../keywords/flying_unit.md) | 8 | 3 | 10 | 19 | 45 :gold:<br>2 :valuables: | :unit_attack: If you resolve a "-1" on the [Attack die](../keywords/dice.md#attack-die), the target gains :paralysis:.<br>:unit_passive: Ignore any [:spellpower:](../spells/index.md) effects and :damage: from [Specialty](../heroes/index.md). | [Core Game](../content/core_game.md) |
| [Crystal Dragons](crystal_dragons.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_ground:](../keywords/ground_unit.md) | 7 | 3 | 9 | 16 | 40 :gold:<br>2 :valuables: | :effect_map: At the beginning of each Resource round, gain 2 :valuables:. | [Core Game](../content/core_game.md) |
| [Faerie Dragons](faerie_dragons.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_flying:](../keywords/flying_unit.md) | 5 | 2 | 8 | 15 | 35 :gold:<br>2 :valuables: | :activation: The selected unit suffers 2 :damage:. This is a [:spellpower:](../spells/index.md) that does not count towards your [spell](../spells/index.md) limit. | [Rampart Expansion](../content/rampart_expansion.md) |
| [Gold Dragons](gold_dragons.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_flying:](../keywords/flying_unit.md) | 6 | 3 | 9 | 10 | 42 :gold: | :unit_attack: Attack 2 spaces in a line. The first attack resolves normally, and the second has 3 :attack:. | [Tower Expansion](../content/tower_expansion.md) |
| [Hydras](hydras.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_ground:](../keywords/ground_unit.md) | 7 | 3 | 8 | 5 | 40 :gold: | :unit_attack: Ignore Retaliation Attacks. This unit attacks up to 2 adjacent enemy units. | [Tower Expansion](../content/tower_expansion.md) |
| [Rust Dragons](rust_dragons.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_flying:](../keywords/flying_unit.md) | 7 | 3 | 10 | 17 | 38 :gold:<br>1 :valuables: | :unit_attack: On "-1" results on the [Attack die](../keywords/dice.md#attack-die), decrease the attacked unit's :defense: by 2 - to a minimum of 0. | [Fortress Expansion](../content/fortress_expansion.md) |
| [Titans](titans.md) | [Neutral](../towns/neutral.md) | - | :azure: | [:unit_ranged:](../keywords/ranged_unit.md) | 6 | 2 | 10 | 10 | 39 :gold: | :unit_passive: Ignore the combat penalty against adjacent units.<br>:unit_attack: When attacking [Black Dragons](black_dragons.md), this unit gains +2 :attack:. | [Tower Expansion](../content/tower_expansion.md) |


## See Also

- [List of Towns](../towns/index.md)


[^1]: Exceptions for specific game modes. This explanation is not valid for all game modes. The specific variant for the game mode is mentioned in the text.