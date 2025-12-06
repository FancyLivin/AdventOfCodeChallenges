from fileReader import readFile

def findTotalMaxPower(file: str) -> None:
    power_banks = readFile(file)
    total_part_one, total_part_two = 0, 0
    for bank in power_banks:
        total_part_one += getMaxTwoDigitPowerOfBank(bank)
        total_part_two += getMaxTwelveDigitPowerOfBank(bank)
    print("Part One:", total_part_one, "Part Two:", total_part_two)

def getMaxTwoDigitPowerOfBank(power_bank: str) -> int:
    l = 0
    battery_max = 0
    for r in range(1, len(power_bank)):
        if battery_max == 99: # highest possible battery size of 2 digits
            break
        tens = int(power_bank[l]) * 10
        ones = int(power_bank[r])
        curr = tens + ones
        battery_max = max(battery_max, curr)

        if power_bank[r] > power_bank[l]:
            l = r
    return battery_max

def getMaxTwelveDigitPowerOfBank(power_bank: str) -> int:
    battery_max = 0
    ptr = 0
    stack = []
    # will always give the largest battery size after while loop finishes
    while ptr < len(power_bank):
        curr = power_bank[ptr]
        if stack:
            if len(stack) < 12:
                distance = len(power_bank) - ptr
                if distance > 12 - len(stack) and stack[-1] < curr:
                    stack.pop()
                else:
                    stack.append(curr)
                    ptr +=1
            else: # stack size of 12
                if stack[-1] < curr:
                    stack.pop()
                else:
                    ptr +=1
        else: # append to empty stack
            stack.append(curr)
            ptr +=1
    battery_max = int("".join(stack))
    return battery_max