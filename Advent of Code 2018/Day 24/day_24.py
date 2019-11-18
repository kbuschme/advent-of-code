import re
from pprint import pprint
from copy import deepcopy

"""
Advent of Code 2018

https://adventofcode.com/2018/day/24

--- Day 24: Immune System Simulator 20XX ---

After a weird buzzing noise, you appear back at the man's cottage. He seems
relieved to see his friend, but quickly notices that the little reindeer
caught some kind of cold while out exploring.

The portly man explains that this reindeer's immune system isn't similar to
regular reindeer immune systems:

The immune system and the infection each have an army made up of several
groups; each group consists of one or more identical units. The armies
repeatedly fight until only one army has units remaining.

Units within a group all have the same hit points (amount of damage a unit
can take before it is destroyed), attack damage (the amount of damage each
unit deals), an attack type, an initiative (higher initiative units attack
first and win ties), and sometimes weaknesses or immunities. Here is
an example group:

18 units each with 729 hit points (weak to fire; immune to cold, slashing)
 with an attack that does 8 radiation damage at initiative 10

Each group also has an effective power: the number of units in that group
multiplied by their attack damage. The above group has an effective power
of 18 * 8 = 144. Groups never have zero or negative units; instead,
the group is removed from combat.

Each fight consists of two phases: target selection and attacking.

During the target selection phase, each group attempts to choose one target.
In decreasing order of effective power, groups choose their targets; in a tie,
the group with the higher initiative chooses first. The attacking group
chooses to target the group in the enemy army to which it would deal
the most damage (after accounting for weaknesses and immunities, but not
accounting for whether the defending group has enough units to actually
receive all of that damage).

If an attacking group is considering two defending groups to which it would
deal equal damage, it chooses to target the defending group with the largest
effective power; if there is still a tie, it chooses the defending group
with the highest initiative. If it cannot deal any defending groups damage,
it does not choose a target. Defending groups can only be chosen as a target
by one attacking group.

At the end of the target selection phase, each group has selected zero or
one groups to attack, and each group is being attacked by zero or one groups.

During the attacking phase, each group deals damage to the target it selected,
if any. Groups attack in decreasing order of initiative, regardless of whether
they are part of the infection or the immune system. (If a group contains no
units, it cannot attack.)

The damage an attacking group deals to a defending group depends on the
attacking group's attack type and the defending group's immunities and
weaknesses. By default, an attacking group would deal damage equal to its
effective power to the defending group. However, if the defending group is
immune to the attacking group's attack type, the defending group instead
takes no damage; if the defending group is weak to the attacking group's
attack type, the defending group instead takes double damage.

The defending group only loses whole units from damage; damage is always
dealt in such a way that it kills the most units possible, and any remaining
damage to a unit that does not immediately kill it is ignored. For example,
if a defending group contains 10 units with 10 hit points each and receives
75 damage, it loses exactly 7 units and is left with 3 units at full health.

After the fight is over, if both armies still contain units, a new fight
begins; combat only ends once one army has lost all of its units.

For example, consider the following armies:

Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with
 an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
 slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack
 that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire,
 cold) with an attack that does 12 slashing damage at initiative 4

If these armies were to enter combat, the following fights, including details
during the target selection and attacking phases, would take place:

Immune System:
Group 1 contains 17 units
Group 2 contains 989 units
Infection:
Group 1 contains 801 units
Group 2 contains 4485 units

Infection group 1 would deal defending group 1 185832 damage
Infection group 1 would deal defending group 2 185832 damage
Infection group 2 would deal defending group 2 107640 damage
Immune System group 1 would deal defending group 1 76619 damage
Immune System group 1 would deal defending group 2 153238 damage
Immune System group 2 would deal defending group 1 24725 damage

Infection group 2 attacks defending group 2, killing 84 units
Immune System group 2 attacks defending group 1, killing 4 units
Immune System group 1 attacks defending group 2, killing 51 units
Infection group 1 attacks defending group 1, killing 17 units


Immune System:
Group 2 contains 905 units
Infection:
Group 1 contains 797 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 184904 damage
Immune System group 2 would deal defending group 1 22625 damage
Immune System group 2 would deal defending group 2 22625 damage

Immune System group 2 attacks defending group 1, killing 4 units
Infection group 1 attacks defending group 2, killing 144 units


Immune System:
Group 2 contains 761 units
Infection:
Group 1 contains 793 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 183976 damage
Immune System group 2 would deal defending group 1 19025 damage
Immune System group 2 would deal defending group 2 19025 damage

Immune System group 2 attacks defending group 1, killing 4 units
Infection group 1 attacks defending group 2, killing 143 units


Immune System:
Group 2 contains 618 units
Infection:
Group 1 contains 789 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 183048 damage
Immune System group 2 would deal defending group 1 15450 damage
Immune System group 2 would deal defending group 2 15450 damage

Immune System group 2 attacks defending group 1, killing 3 units
Infection group 1 attacks defending group 2, killing 143 units


Immune System:
Group 2 contains 475 units
Infection:
Group 1 contains 786 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 182352 damage
Immune System group 2 would deal defending group 1 11875 damage
Immune System group 2 would deal defending group 2 11875 damage

Immune System group 2 attacks defending group 1, killing 2 units
Infection group 1 attacks defending group 2, killing 142 units


Immune System:
Group 2 contains 333 units
Infection:
Group 1 contains 784 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181888 damage
Immune System group 2 would deal defending group 1 8325 damage
Immune System group 2 would deal defending group 2 8325 damage

Immune System group 2 attacks defending group 1, killing 1 unit
Infection group 1 attacks defending group 2, killing 142 units


Immune System:
Group 2 contains 191 units
Infection:
Group 1 contains 783 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181656 damage
Immune System group 2 would deal defending group 1 4775 damage
Immune System group 2 would deal defending group 2 4775 damage

Immune System group 2 attacks defending group 1, killing 1 unit
Infection group 1 attacks defending group 2, killing 142 units


Immune System:
Group 2 contains 49 units
Infection:
Group 1 contains 782 units
Group 2 contains 4434 units

Infection group 1 would deal defending group 2 181424 damage
Immune System group 2 would deal defending group 1 1225 damage
Immune System group 2 would deal defending group 2 1225 damage

Immune System group 2 attacks defending group 1, killing 0 units
Infection group 1 attacks defending group 2, killing 49 units


Immune System:
No groups remain.
Infection:
Group 1 contains 782 units
Group 2 contains 4434 units

In the example above, the winning army ends up with 782 + 4434 = 5216 units.

You scan the reindeer's condition (your puzzle input); the white-bearded man
looks nervous. As it stands now, how many units would the winning army have?

Your puzzle answer was 10890.


--- Part Two ---

Things aren't looking good for the reindeer. The man asks whether more milk and cookies would help you think.

If only you could give the reindeer's immune system a boost, you might be able to change the outcome of the combat.

A boost is an integer increase in immune system units' attack damage. For example, if you were to boost the above example's immune system's units by 1570, the armies would instead look like this:

Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with
 an attack that does 6077 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
 slashing) with an attack that does 1595 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack
 that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire,
 cold) with an attack that does 12 slashing damage at initiative 4
With this boost, the combat proceeds differently:

Immune System:
Group 2 contains 989 units
Group 1 contains 17 units
Infection:
Group 1 contains 801 units
Group 2 contains 4485 units

Infection group 1 would deal defending group 2 185832 damage
Infection group 1 would deal defending group 1 185832 damage
Infection group 2 would deal defending group 1 53820 damage
Immune System group 2 would deal defending group 1 1577455 damage
Immune System group 2 would deal defending group 2 1577455 damage
Immune System group 1 would deal defending group 2 206618 damage

Infection group 2 attacks defending group 1, killing 9 units
Immune System group 2 attacks defending group 1, killing 335 units
Immune System group 1 attacks defending group 2, killing 32 units
Infection group 1 attacks defending group 2, killing 84 units
Immune System:
Group 2 contains 905 units
Group 1 contains 8 units
Infection:
Group 1 contains 466 units
Group 2 contains 4453 units

Infection group 1 would deal defending group 2 108112 damage
Infection group 1 would deal defending group 1 108112 damage
Infection group 2 would deal defending group 1 53436 damage
Immune System group 2 would deal defending group 1 1443475 damage
Immune System group 2 would deal defending group 2 1443475 damage
Immune System group 1 would deal defending group 2 97232 damage

Infection group 2 attacks defending group 1, killing 8 units
Immune System group 2 attacks defending group 1, killing 306 units
Infection group 1 attacks defending group 2, killing 29 units
Immune System:
Group 2 contains 876 units
Infection:
Group 2 contains 4453 units
Group 1 contains 160 units

Infection group 2 would deal defending group 2 106872 damage
Immune System group 2 would deal defending group 2 1397220 damage
Immune System group 2 would deal defending group 1 1397220 damage

Infection group 2 attacks defending group 2, killing 83 units
Immune System group 2 attacks defending group 2, killing 427 units
After a few fights...

Immune System:
Group 2 contains 64 units
Infection:
Group 2 contains 214 units
Group 1 contains 19 units

Infection group 2 would deal defending group 2 5136 damage
Immune System group 2 would deal defending group 2 102080 damage
Immune System group 2 would deal defending group 1 102080 damage

Infection group 2 attacks defending group 2, killing 4 units
Immune System group 2 attacks defending group 2, killing 32 units
Immune System:
Group 2 contains 60 units
Infection:
Group 1 contains 19 units
Group 2 contains 182 units

Infection group 1 would deal defending group 2 4408 damage
Immune System group 2 would deal defending group 1 95700 damage
Immune System group 2 would deal defending group 2 95700 damage

Immune System group 2 attacks defending group 1, killing 19 units
Immune System:
Group 2 contains 60 units
Infection:
Group 2 contains 182 units

Infection group 2 would deal defending group 2 4368 damage
Immune System group 2 would deal defending group 2 95700 damage

Infection group 2 attacks defending group 2, killing 3 units
Immune System group 2 attacks defending group 2, killing 30 units
After a few more fights...

Immune System:
Group 2 contains 51 units
Infection:
Group 2 contains 40 units

Infection group 2 would deal defending group 2 960 damage
Immune System group 2 would deal defending group 2 81345 damage

Infection group 2 attacks defending group 2, killing 0 units
Immune System group 2 attacks defending group 2, killing 27 units
Immune System:
Group 2 contains 51 units
Infection:
Group 2 contains 13 units

Infection group 2 would deal defending group 2 312 damage
Immune System group 2 would deal defending group 2 81345 damage

Infection group 2 attacks defending group 2, killing 0 units
Immune System group 2 attacks defending group 2, killing 13 units
Immune System:
Group 2 contains 51 units
Infection:
No groups remain.
This boost would allow the immune system's armies to win! It would be left with 51 units.

You don't even know how you could boost the reindeer's immune system or what effect it might have, so you need to be cautious and find the smallest boost that would allow the immune system to win.

How many units does the immune system have left after getting the smallest boost it needs to win?

Your puzzle answer was 7730.
"""
def parse_system_description(system_description, verbose=False):
    system = []
    for each in system_description.split("\n\n"):
        team, *group_descriptions = each.strip().split("\n")
        team = team.strip(":")
        for description in group_descriptions:
            units = int(re.search(r"^\d*(?= units)", description).group(0))
            hit_points = int(re.search(r"\d*(?= hit points)",
                description).group(0))
            attack = int(re.search(r"\d*(?= \w* damage)",
                description).group(0))
            attack_type = re.search(r"\w*(?= damage)", description).group(0)
            initiative = int(re.search(r"(?<=initiative )\d*",
                description).group(0))
            if re.search(r"(?<=weak to )(\w|\s|,)*(?=[;\)])", description):
                weaknesses = re.search(r"(?<=weak to )(\w|\s|,)*(?=[;\)])",
                    description).group(0).split(", ")
            else:
                weaknesses = []
            if re.search(r"(?<=immune to )(\w|\s|,)*(?=[;\)])", description):
                immunities = re.search(r"(?<=immune to )(\w|\s|,)*(?=[;\)])",
                    description).group(0).split(", ")
            else:
                immunities = []

            group = {
                'team': team,
                'units': units,
                'hit_points': hit_points,
                'weaknesses': weaknesses,
                'immunities': immunities,
                'attack': attack,
                'attack_type': attack_type,
                'initiative': initiative
            }
            system.append(group)

    if verbose:
        for group in system:
            for trait in group.items():
                print(trait)
            print()
    return system

def effective_power(group):
    return group['units'] * group['attack']

def select_target(groups, verbose=False):
    sorted_attackers = sorted(
        [(i, effective_power(g), g['initiative'])
         for i, g in enumerate(groups)],
        key=lambda g: (g[1], g[2]), reverse=True)
    if verbose:
        print("Groups attack order (index, effective power, initiative):")
        for i, power, initiative in sorted_attackers:
            print(i, power, initiative)

    selected_targets = {}
    for attacker_index, _, _ in sorted_attackers:
        attacker = groups[attacker_index]
        if verbose:
            print(f"\nAttacker: {attacker_index}")
        enemy_indices = [i for i, other in enumerate(groups)
                           if other['team'] != attacker['team']
                           and i not in selected_targets.values()]

        possible_targets = []
        for enemy_index in enemy_indices:
            enemy = groups[enemy_index]
            if verbose:
                print(f"Enemy: {enemy_index}")
            estimated_damage = estimate_damage(attacker, enemy)
            if estimated_damage > 0:
                possible_targets.append((
                    enemy_index, estimated_damage,
                    effective_power(enemy), enemy['initiative']
                ))

        if len(possible_targets) > 0:
            target_index = sorted(possible_targets,
                key=lambda t: (t[1], t[2], t[3]), reverse=True)[0][0]
            if verbose:
                print(f"Target: {target_index}")
            selected_targets[attacker_index] = target_index
    return selected_targets

def estimate_damage(attacker, defender, weakness_multiplier=2):
    if attacker['attack_type'] in defender['immunities']:
        return 0
    elif attacker['attack_type'] in defender['weaknesses']:
        return effective_power(attacker) * weakness_multiplier
    else:
        return effective_power(attacker)

def attack(attacker, defender, verbose=False):
    if attacker['units'] > 0 and defender['units'] > 0:
        damage = estimate_damage(attacker, defender)
        hitpounts_per_unit = defender['hit_points']
        defeated_units =  damage // hitpounts_per_unit
        defender['units'] -= defeated_units

        if verbose:
            print("\nAttacker:")
            pprint(attacker)
            print("Defender:")
            pprint(defender)
            print(f"Damage dealt: {damage}")
            print(f"Units defeated: {defeated_units}")
    else:
        defeated_units = 0

    return defender, defeated_units

def immune_response(groups, verbose=False):
    rounds = 0
    stalemate = False
    while len(set(group['team'] for group in groups)) > 1 and not stalemate:
        stalemate = True
        rounds += 1
        if verbose:
            print(f'\n\nRound: {rounds}')
            print('Groups:')
            pprint(groups)

        targets = select_target(groups)

        defeated_groups = []
        attackers = sorted([(i, groups[i]['initiative']) for i in targets],
            key=lambda a: a[1], reverse=True)
        for attacker_index, _ in attackers:
            defender_index = targets[attacker_index]
            attacker = groups[attacker_index]
            defender = groups[defender_index]
            defender, defeated_units = attack(attacker, defender)
            if defeated_units > 0:
                stalemate = False
            if defender['units'] > 0:
                groups[defender_index] = defender
            else:
                defeated_groups.append(defender_index)

        groups = [group for i, group in enumerate(groups)
                        if i not in defeated_groups]
    if stalemate:
        victorious_team = None
    else:
        victorious_team = set([group['team'] for group in groups]).pop()
    remaining_units = sum([group['units'] for group in groups])
    return victorious_team, remaining_units

def boost_immune_system(groups, boost):
    for i, group in enumerate(groups):
        if group['team'] == 'Immune System':
            groups[i]['attack'] += boost
    return groups

def find_smallest_immune_system_boost(groups):
    boost = 0
    victorious_team = None
    while victorious_team != 'Immune System':
        boost += 1
        boosted_groups = boost_immune_system(deepcopy(groups), boost)
        victorious_team, remaining_units = immune_response(boosted_groups)
    return boost, remaining_units

def main():
    with open('day_24_system.txt', 'r') as system_file:
        groups = parse_system_description(system_file.read())

    _, units_winning_army = immune_response(deepcopy(groups))
    print(f"Units of the winning army: {units_winning_army}")

    boost, units_winning_army = find_smallest_immune_system_boost(
        deepcopy(groups))
    print(f"Immune system units after smallest boost ({boost}):",
        f"{units_winning_army}")

if __name__ == '__main__':
    main()
