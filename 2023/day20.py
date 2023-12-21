import doctest
import math
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Any


@dataclass
class Module:
    kind: str
    inputs: List[str]
    outputs: List[str]
    state: Any


def main():
    module_pattern = re.compile(r"([%&])?(\w+) -> (.*)")

    modules = defaultdict(lambda: Module(None, [], [], None))

    with open('day20_input.txt') as f:
        for line in f:
            kind, name, outputs = module_pattern.match(line.strip()).groups()
            outputs = outputs.split(', ')

            modules[name].kind = kind
            modules[name].outputs = outputs
            for output in outputs:
                modules[output].inputs.append(name)

    for module in modules.values():
        if module.kind == '%':
            module.state = False
        if module.kind == '&':
            module.state = {k: False for k in module.inputs}

    def press_button():
        low_count = 0
        high_count = 0
        pending = []

        def send(target, signal, source):
            # print(f"{source} -> {signal} -> {target}")
            pending.append((target, signal, source))

        send('broadcaster', False, 'button')

        while pending:
            target, signal, source = pending.pop()
            if signal:
                high_count += 1
            else:
                low_count += 1

            module = modules[target]
            if module.kind == '%':
                if not signal:
                    module.state = not module.state
                    for output in module.outputs:
                        send(output, module.state, target)
            elif module.kind == '&':
                module.state[source] = signal
                signal = not all(v for v in module.state.values())
                for output in module.outputs:
                    send(output, signal, target)
            else:
                for output in module.outputs:
                    send(output, signal, target)
        return low_count, high_count

    def part1():
        total_low_count = 0
        total_high_count = 0
        for _ in range(1000):
            low_count, high_count = press_button()
            total_low_count += low_count
            total_high_count += high_count
        return total_low_count * total_high_count

    print(f'Part 1: {part1()}')

    def part2():
        def preceding(module_name):
            return [k for k, v in modules.items() if module_name in v.outputs]

        def bits_to_int(bits):
            value = 0
            for bit in reversed(bits):
                value *= 2
                if bit:
                    value |= 1
            return value

        def counter_period(counter):
            bits = []
            bit = next(m for m in preceding(counter) if m in modules['broadcaster'].outputs)
            while bit:
                bits.append(counter in modules[bit].outputs)
                bit = next((m for m in modules[bit].outputs if m != counter), None)
            return bits_to_int(bits)

        counters = [preceding(x)[0] for x in preceding(preceding('rx')[0])]
        periods = [counter_period(c) for c in counters]
        return math.lcm(*periods)

    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    doctest.testmod()
    main()
