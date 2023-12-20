import doctest
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

    total_low_count = 0
    total_high_count = 0
    for _ in range(1000):
        low_count, high_count = press_button()
        total_low_count += low_count
        total_high_count += high_count

    print(f'Part 1: {total_low_count * total_high_count}')





if __name__ == "__main__":
    doctest.testmod()
    main()
