import re

# 18 units each with 729 hit points (weak to fire; immune to cold, slashing) with an attack that does 8 radiation damage at initiative 10
line_p = re.compile(r'(\d+) units each with (\d+) hit points (?:\((.*)\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)')


class Group(object):
    def __init__(self, team, n, units, hp, mods, damage, type, initiative):
        self.team = team
        self.n = n
        self.units = int(units)
        self.hp = int(hp)
        self.damage = int(damage)
        self.type = type
        self.initiative = int(initiative)
        self.weak = set()
        self.immune = set()

        if mods:
            for mod in mods.split('; '):
                mod_type, kinds = mod.split(' to ')
                if mod_type == 'weak':
                    for kind in kinds.split(', '):
                        self.weak.add(kind)
                elif mod_type == 'immune':
                    for kind in kinds.split(', '):
                        self.immune.add(kind)
                else:
                    raise Exception('what is ' + mod_type)

    def __str__(self):
        return 'Group[team={} {}, units={}, hp={}, weak={}, immune={}, damage={} {}, initiative={}]'.format(
            self.team, self.n, self.units, self.hp, self.weak, self.immune, self.damage, self.type, self.initiative)

    def effective_power(self):
        return self.units * self.damage

    def damage_vs(self, other):
        if self.type in other.immune:
            return 0
        if self.type in other.weak:
            return self.effective_power() * 2
        return self.effective_power()


def simulate(boost=0):
    with open('day24.txt') as f:
        groups = []

        for line in f:
            line = line.strip()
            if line == '':
                pass
            elif line == 'Immune System:':
                current = 'immune'
                n = 1
            elif line == 'Infection:':
                current = 'infection'
                n = 1
            else:
                m = line_p.match(line)
                groups.append(Group(current, n, *m.groups()))
                if current == 'immune':
                    groups[-1].damage += boost
                n += 1

    while True:
        killed = 0

        # groups.sort(key=lambda x: (x.team, x.n))
        # for group in groups:
        #     if group.units:
        #         print(group)
        # print()

        targets = dict()
        groups.sort(key=lambda x: (x.effective_power(), x.initiative))
        groups.reverse()
        for group in groups:
            if group.units:
                possible_targets = [x for x in groups if x.team != group.team and x.units and x not in targets.values()]
                if possible_targets:
                    target = max(possible_targets, key=lambda x: (group.damage_vs(x), x.effective_power(), x.initiative))
                    if group.damage_vs(target) > 0:
                        targets[group] = target

        groups.sort(key=lambda x: -x.initiative)
        for group in groups:
            if group in targets:
                target = targets[group]
                damage = group.damage_vs(target)
                kills = min(target.units, damage // target.hp)
                # print('{} {} deals {} damage to {} {}, killing {}'.format(group.team, group.n, damage, target.team, target.n, kills))
                target.units -= kills
                killed += kills

        immune_units = sum(x.units for x in groups if x.team == 'immune')
        infection_units = sum(x.units for x in groups if x.team == 'infection')
        if killed == 0:
            print('no kills, tie game')
            print('immune_units', immune_units)
            print('infection_units', infection_units)
            return False
        if immune_units == 0 or infection_units == 0:
            print('immune_units', immune_units)
            print('infection_units', infection_units)
            return immune_units > 0


if __name__ == '__main__':
    for i in range(0, 128):
        print('simulating with boost', i)
        if simulate(boost=i):
            print('found a winner!')
            break
