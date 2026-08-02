---
search:
  exclude: true
---
# Fields

Fields are single cells on a [tile](../tiles/index.md).
When your [Hero](../heroes/index.md) moves to a field, they must immediately visit it, or first start a Combat against the enemies guarding it before visiting.
Roman numerals written on a field indicate that the field is guarded by [Neutral enemies](../units/index.md) that must be fought to visit it.


## Visitable Field

Once you visit this field, place a Black Cube on it. Treat it as an [Empty Field](empty_field.md) as long as it has a Black Cube.


## Revisitable Field

You can visit this field multiple times. Do not place any Cubes when you visit it. You may pay 1 MP to fisit this field again.


## Flaggable Field

These fields can be captured by players and provide passive benefits. When you visit one, place your Faction Cube on it. Enemy Heroes who visit your flagged fields will replace your Cube with theirs to steal the field’s effects. Allied [Heroes](../heroes/index.md) treat flagged fields as if they were empty.


## List of Fields

| Name | Type | Effect |
| :--- | :---: | :--- |
| [Artifact Symbol](artifact_symbol.md) | [Visitable Field](index.md#visitable-field) | You may [**Search(2)**](../keywords/search.md) the [Artifact](../artifacts/index.md) deck. |
| [Black Market](black_market.md) | [Revisitable Field](index.md#revisitable-field) | Look at the top 4 cards from the [Artifact](../artifacts/index.md) discard pile. You may buy one of them for:<br><br>5 :gold: if it is a [Minor Artifact](../artifacts/index.md#minor-artifacts)<br>7 :gold: if it is a [Major Artifact](../artifacts/index.md#major-artifacts)<br>10 :gold: if it is a [Relic Artifact](../artifacts/index.md#relic-artifacts) |
| [Blocked Field](blocked_field.md) | A blocked field is fully enclosed by a thick border and heroes are not allowed to enter it in general. |  |
| [Buoy](buoy.md) | [Visitable Field](index.md#visitable-field) | Gain a [Positive Morale](../keywords/morale.md#positive) token. |
| [Creature Bank](creature_bank.md) | [Visitable Field](index.md#visitable-field) | Please refer to individual Creature Banks for effects. |
| [Crypt (Creature Bank)](crypt_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>6 :gold:.<br><br>**Extra:**<br>2 :gold: for every Stacked unit. |
| [Cyclops Stockpile](cyclops_stockpile.md) | [Visitable Field](index.md#visitable-field) | When preparing the Neutral Army guarding this location, instead of drawing 1 :azure_tier: unit, find 2 :gold_tier: [Cyclopes](../units/cyclopes.md) and add them to the Neutral Army (look for them first in the :gold_tier: discard pile, and then in the :gold_tier: Neutral Unit deck). If you win the Combat, roll and resolve 4 [:resource_die:](../keywords/dice.md#resource-die). Any additional effects depend on the scenario. |
| [Cyclops Stockpile (Creature Bank)](cyclops_stockpile_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>8 :building_materials: and 2 :valuables:.<br><br>**Extra:**<br>2 :building_materials: and 1 :valuables: for every Stacked unit. |
| [Derelict Ship](derelict_ship.md) | [Visitable Field](index.md#visitable-field) | You may [**Search(2)**](../keywords/search.md) the [Artifact](../artifacts/index.md) deck. If you do so, you also gain 2 :gold:. |
| [Derelict Ship (Creature Bank)](derelict_ship_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>[:positive_morale:](../keywords/morale.md#positive) and 7 :gold:.<br><br>**Extra:**<br>2 :gold: for every Stacked unit and [**Search(X)**](../keywords/search.md) the [Spell](../spells/index.md) deck, where X is the number of Stacked units. |
| [Dragon Fly Hive (Creature Bank)](dragon_fly_hive_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>1x&nbsp;[Dragon&nbsp;Flies](../units/dragon_flies.md#dragon-fly-hive) unit.<br><br>**Extra:**<br>If the Creature Bank was guarded by at least 2 Stacked units, gain Stacked [Dragon&nbsp;Flies](../units/dragon_flies.md#dragon-fly-hive) instead. |
| [Dragon Utopia](dragon_utopia.md) | [Flaggable Field](index.md#flaggable-field) | Effects depend on the Scenario. |
| [Dragon Utopia (Creature Bank)](dragon_utopia_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>40 :gold: and [**Search(3)**](../keywords/search.md) the [Artifact](../artifacts/index.md) deck.<br><br>**Extra:**<br>[**Search(5)**](../keywords/search.md) the [Artifact](../artifacts/index.md) deck or the [Spell](../spells/index.md) deck for every Stacked unit. |
| [Dwarven Treasury (Creature Bank)](dwarven_treasury_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>7 :gold:.<br><br>**Extra:**<br>3 :gold: for every Stacked unit. |
| [Elemental Conflux](elemental_conflux.md) | [Visitable Field](index.md#visitable-field) | When you enter this location, for every [Dwelling](../keywords/dwelling.md) you have, draw from the corresponding [Neutral Unit](../units/index.md) deck until you find an "Elementals" card. You can [Recruit](../keywords/recruit.md) one of these units if you :pay: its [Recruitment cost](../keywords/recruit.md). Shuffle the rest of the cards back into their decks. |
| [Empty Field](empty_field.md) | A field with no effect and no restriction of movement. |  |
| [Faerie Ring](faerie_ring.md) | [Visitable Field](index.md#visitable-field) | When you enter this location, [**Remove**](../keywords/remove.md) 1 card from your hand, then [**Search (2)**](../keywords/search.md) the card’s deck. You cannot [**Remove**](../keywords/remove.md) [Statistic](../statistics/index.md), Starting [Ability](../abilities/index.md), or [Specialty](../heroes/index.md) cards this way. |
| [Flotsam](flotsam.md) | [Visitable Field](index.md#visitable-field) | Gain 2 :building_materials:. |
| [Fountain of Youth](fountain_of_youth.md) | [Visitable Field](index.md#visitable-field) | Gain [:positive_morale:](../keywords/morale.md#positive) token. Gain +1 :movement_points: for this turn. |
| [Grail](grail.md) | [Visitable Field](index.md#visitable-field) | Gain a Grail Token. Only one Grail Token can exist in the game, do not gain another if this Field’s Black Cube is removed or if there are multiple Grail Fields. The Token’s effects are described in the Scenario’s description. |
| [Grave](grave.md) | [Visitable Field](index.md#visitable-field) | Gain [Negative Morale](../keywords/morale.md#negative) token, 3 :gold:, and [**Search(2)**](../keywords/search.md) [:artifact:](../artifacts/index.md). |
| [Griffin Conservatory (Creature Bank)](griffin_conservatory_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>1x&nbsp;[Griffins](../units/griffins.md#griffin-conservatory) unit.<br><br>**Extra:**<br>If the Creature Bank was guarded by at least 2 Stacked units, gain Stacked [Griffins](../units/griffins.md#griffin-conservatory) instead. |
| [Hill Fort](hill_fort.md) | [Visitable Field](index.md#visitable-field) | You may immediately [Reinforce](../keywords/reinforce.md) one of your :bronze_tier: or :silver_tier: [Units](../units/index.md). The [Reinforcement](../keywords/reinforce.md) cost is reduced by 3 :gold: to a minimum of 0. |
| [Imp Cache (Creature Bank)](imp_cache_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>3 :gold:.<br><br>**Extra:**<br>1 :gold: for every Stacked unit. |
| [Jetsam](jetsam.md) | [Visitable Field](index.md#visitable-field) | Roll 1 [Attack Die](../keywords/dice.md#attack-die). Depending on the result, do the following:<br><br>**+1** - Roll and resolve 2 [:resource_die:](../keywords/dice.md#resource-die).<br><br>**0** - Roll and resolve 1 [:resource_die:](../keywords/dice.md#resource-die).<br><br>**-1** - Gain nothing. |
| [Learning Stone](learning_stone.md) | [Visitable Field](index.md#visitable-field) | Gain one :experience:. |
| [Library of Enlightentment](library_of_enlightenment.md) | [Revisitable Field](index.md#revisitable-field) | You can :pay: 3 :gold: to [Remove](../keywords/remove.md) 1 [Statistic](../statistics/index.md) card from your hand or discard pile and replace it with any other [Statistic](../statistics/index.md) card. You can do it twice per visit. |
| [Magic Spring](magic_spring.md) | [Visitable Field](index.md#visitable-field) | You may look at the top 3 Cards of your Discard Pile and return one of them to your Hand. Return the remaining cards to the top of your Discard Pile in any order. |
| [Market of Time](market_of_time.md) | [Visitable Field](index.md#visitable-field) | Remove one card from your hand. Then [**Search(2)**](../keywords/search.md) the [Ability](../abilities/index.md), [Spell](../spells/index.md), or [Artifact](../artifacts/index.md) Deck. |
| [Medusa Stores (Creature Bank)](medusa_stores_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>6 :gold: and 1 :valuables:.<br><br>**Extra:**<br>3 :gold: or 1 :valuables: for every Stacked unit. |
| [Mermaid](mermaid.md) | [Visitable Field](index.md#visitable-field) | The [Hero](../heroes/index.md) who entered this field gains 1 additional MP this turn. You also gain a [Positive Morale](../keywords/morale.md#positive) token. |
| [Mine](mine.md) | [Flaggable Field](index.md#flaggable-field) | When flagged, increases the specific resource income (shown on the field). The first player to flag the Mine also gains its income immediately. There are following types of Mines:<br><br>+5 :gold: income<br>+2 :building_materials: income<br>+1 :valuables: income |
| [Monolith (One-Way)](monolith_one_way.md) | [Revisitable Field](index.md#revisitable-field) | When you enter this location, move your Hero to the corresponding Exit Monolith location. You **cannot** use the Exit Monolith to move back to the Entrance Monolith. |
| [Monolith (Two-Way)](monolith_two_way.md) | [Revisitable Field](index.md#revisitable-field) | When you enter this location, move your Hero to the corresponding Exit Monolith location. You can **use** the Exit Monolith to move back to the Entrance Monolith. |
| [Mystical Garden](mystical_garden.md) | [Visitable Field](index.md#visitable-field) | Gain 2 :gold:.<br><br>— OR —<br><br>Gain 1 :valuables:. |
| [Naga Bank (Creature Bank)](naga_bank_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>6 :gold: and 2 :valuables:.<br><br>**Extra:**<br>6 :gold: and 1 :valuables: for every Stacked unit. |
| [Obelisk](obelisk.md) | [Flaggable Field](index.md#flaggable-field) | Effects depend on the Scenario. When you Flag this Field, do not remove any enemy Faction Cubes; multiple players may have a [Faction](../towns/index.md) Cube on this Field. |
| [Pandora's Box](pandoras_box.md) | [Visitable Field](index.md#visitable-field) | Roll 2 [Treasure Dice](../keywords/dice.md#treasure-die) and choose 1 result to gain.<br><br>— OR —<br><br>Roll 2 [Resource Dice](../keywords/dice.md#resource-die) and choose 1 result to gain. |
| [Prison](prison.md) | [Visitable Field](index.md#visitable-field) | Gain a Secondary [Hero](../heroes/index.md). Place their model on this Field. If you already have a Secondary [Hero](../heroes/index.md), gain 3 :gold: instead. |
| [Pyramid (Creature Bank)](pyramid_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅳ-Ⅴ)](../fields/creature_bank.md) | **Reward:**<br>[**Search(5)**](../keywords/search.md) the [Spell](../spells/index.md) deck.<br><br>**Extra:**<br>For every Stacked unit, you may [Remove](../keywords/remove.md) 1 [Spell](../spells/index.md), [Ability](../abilities/index.md), or [Artifact](../artifacts/index.md) card from your hand or discard pile, then [**Search(5)**](../keywords/search.md) the appropriate deck. |
| [Random Town](random_town.md) | [Flaggable Field](index.md#flaggable-field) | When revealed, all players roll 2 [Resource dice](../keywords/dice.md#resource-die). The highest roller chooses an unused [Faction](../towns/index.md). The random [Town](../towns/index.md) is defended by [Units](../units/index.md) from that [Faction](../towns/index.md). They have a "Pack" of :bronze_tier:, two "Packs" of :silver_tier:, and two "Fews" of :gold_tier: [Units](../units/index.md). The :bronze_tier: [Unit](../units/index.md) is chosen by the player who controls the [Units](../units/index.md) during that Combat.<br><br>When flagged, increases :gold: income by 10. The first player to flag the [Town](../towns/index.md) also gains its income immediately. |
| [Redwood Observatory](redwood_observatory.md) | [Visitable Field](index.md#visitable-field) | Discover a face down [Tile](../tiles/index.md) adjacent to this one. |
| [Resource Symbol](resource_symbol.md) | [Visitable Field](index.md#visitable-field) | Roll a specified number of [Resource dice](../keywords/dice.md#resource-die), then select one to resolve its effect. |
| [Sanctuary](sanctuary.md) | [Revisitable Field](index.md#revisitable-field) | Heroes on this Field cannot be attacked by other [Heroes](../heroes/index.md). Friendly Heroes can move through enemy [Heroes](../heroes/index.md) on this Field but cannot stop here. |
| [Scholar](scholar.md) | [Visitable Field](index.md#visitable-field) | Roll 1 [Attack Die](../keywords/dice.md#attack-die). Depending on the result, do the following:<br><br>**+1** - Gain a [Statistic](../statistics/index.md) Card of your choice or Remove a [Statistic](../statistics/index.md) Card from your hand.<br><br>**0** - Draw 2 Cards from the [Ability](../abilities/index.md) Deck, gain one of them and discard the other.<br><br>**-1** - Draw 2 Cards from the [Spell](../spells/index.md) Deck, gain one of them and discard the other. |
| [Sea Barrel](sea_barrel.md) | [Visitable Field](index.md#visitable-field) | Roll and resolve 1 [:resource_die:](../keywords/dice.md#resource-die). |
| [Sea Chest](sea_chest.md) | [Visitable Field](index.md#visitable-field) | Roll 1 [Attack Die](../keywords/dice.md#attack-die). Depending on the result, do the following:<br><br>**+1** - [**Search(1)**](../keywords/search.md) [:artifact:](../artifacts/index.md).<br><br>**0** - Gain 5 :gold:.<br><br>**-1** - Gain nothing. |
| [Settlement](settlement.md) | [Flaggable Field](index.md#flaggable-field) | Works as a spawn point for Secondary [Heroes](../heroes/index.md) or Main [Heroes](../heroes/index.md) that have been defeated.<br><br>Works the same way as a mine, but the player can choose which resource income to increase. The settlement is then marked with a token of the chosen resource.<br><br>— OR —<br><br>Reinforce one of your :bronze_tier: or :silver_tier: [Units](../units/index.md) immediately for half the cost, rounded up. The first player to flag the settlement Reinforces that [Unit](../units/index.md) for free. |
| [Shipwreck](shipwreck.md) | [Visitable Field](index.md#visitable-field) | Roll and resolve 2 [:resource_die:](../keywords/dice.md#resource-die). |
| [Shipwreck (Creature Bank)](shipwreck_creature_bank.md) | [Visitable Field](index.md#visitable-field)<br>[Creature Bank (Ⅱ-Ⅲ)](../fields/creature_bank.md) | **Reward:**<br>[:positive_morale:](../keywords/morale.md#positive) and 5 :gold:.<br><br>**Extra:**<br>2 :gold: for every Stacked unit and [**Search(X)**](../keywords/search.md) the [Artifact](../artifacts/index.md) deck, where X is the number of Stacked units. |
| [Shipwreck Survivor](shipwreck_survivor.md) | [Visitable Field](index.md#visitable-field) | [**Search(2)**](../keywords/search.md) [:artifact:](../artifacts/index.md). |
| [Shrine of Magic Gesture](shrine_of_magic_gesture.md) | [Visitable Field](index.md#visitable-field) | Pay :pay: 3 :gold: to [**Search(2)**](../keywords/search.md) the [Spell](../spells/index.md) Deck. |
| [Shrine of Magic Incantation](shrine_of_magic_incantation.md) | [Visitable Field](index.md#visitable-field) | [**Search(2)**](../keywords/search.md) the [Spell](../spells/index.md) Deck. |
| [Spell Scroll](spell_scroll.md) | [Visitable Field](index.md#visitable-field) | When you enter this location, take 1 Spell Scroll card, place it near your [Hero](../heroes/index.md) card, and follow the instructions on the card. |
| [Stables](stables.md) | [Revisitable Field](index.md#revisitable-field) | Gain +1 :movement_points: for this turn. |
| [Star Axis](star_axis.md) | [Flaggable Field](index.md#flaggable-field) | You may Remove one of your [Statistic](../statistics/index.md) cards from your hand and replace it with an **Empowered** one of the same type. When you Flag this Field, do not remove any enemy Faction Cubes; multiple players may have a Faction Cube on this Field. |
| [Subterranean Gate](subterranean_gate.md) | [Revisitable Field](index.md#revisitable-field) | When you enter this location, move to the connected location on the adjacent [tile](../tiles/index.md). This location allows you to enter or exit [Subterranean tiles](../tiles/index.md#subterranean-tiles). |
| [Tavern](tavern.md) | [Revisitable Field](index.md#revisitable-field) | You can :pay: 7 :gold: to gain a Secondary [Hero](../heroes/index.md). Place their model on this Field. Then, choose one enemy player to discard 1 random card from their hand. |
| [Temple](temple.md) | [Visitable Field](index.md#visitable-field) | Gain [:positive_morale:](../keywords/morale.md#positive) token. |
| [Temple of the Sea](temple_of_the_sea.md) | [Visitable Field](index.md#visitable-field) | Gain 10 :gold: and [**Search(2)**](../keywords/search.md) [:artifact:](../artifacts/index.md) twice. |
| [Town](town.md) | [Flaggable Field](index.md#flaggable-field) | When flagged, the enemy Secondary [Heroes](../heroes/index.md) or Main [Heroes](../heroes/index.md) that have been defeated cannot spawn here.<br>Flagging an enemy town does prevent the enemy player from using it, nor does it grant any access to the [Town](../towns/index.md) board or [Faction Units](../units/index.md) to the player who flagged it.<br>Flagging a [Town](../towns/index.md) can cause Player Elimination win condition, and some scenarios may have extra rules and rewards attached to flagging [Towns](../towns/index.md). |
| [Trading Post](trading_post.md) | [Revisitable Field](index.md#revisitable-field) | Choose one:<br><br>[Trade](../trading.md) resources<br><br>— OR —<br><br>Remove a card<br><br>— OR —<br><br>Buy a [War Machine](../war_machines/index.md) |
| [Treasure Symbol](treasure_symbol.md) | [Visitable Field](index.md#visitable-field) | Roll a specified number of [Treasure dice](../keywords/dice.md#treasure-die), then select one to resolve its effect. |
| [Tree of Knowledge](tree_of_knowledge.md) | [Visitable Field](index.md#visitable-field) | You may :pay: 3 :valuables: or 10 :gold: to gain 2 :experience:. |
| [University](university.md) | [Visitable Field](index.md#visitable-field) | :pay: 6 :gold: to [**Search(4)**](../keywords/search.md) the [Ability](../abilities/index.md) Discard Pile |
| [War Machine Factory](war_machine_factory.md) | [Revisitable Field](index.md#revisitable-field) | Buy a [War Machine](../war_machines/index.md) |
| [Warrior's Tomb](warriors_tomb.md) | [Visitable Field](index.md#visitable-field) | [**Search(2)**](../keywords/search.md) [Artifacts](../artifacts/index.md) twice, then gain [:negative_morale:](../keywords/morale.md#negative) token twice. |
| [Water Wheel](water_wheel.md) | [Visitable Field](index.md#visitable-field) | Gain 3 :gold:. |
| [Windmill](windmill.md) | [Visitable Field](index.md#visitable-field) | Gain 1 :valuables:. |
| [Witch Hut](witch_hut.md) | [Visitable Field](index.md#visitable-field) | Choose one:<br><br>Remove an [Ability](../abilities/index.md) card from your hand<br><br>— OR —<br><br>look at the top card of the [Ability](../abilities/index.md) Deck and put that card into your hand or into the [Ability](../abilities/index.md) Deck Discard Pile. |


## See Also

- [List of Tiles](../tiles/index.md)
