# Advent Of Code 2025 Challenges
Will be writing my thought process for each solution in this README file, along with runtime & space complexities.
Technically since I am reading the file into each of my solutions, lowest space complexity will be O(n), but I'm pretending that it's an external input going forward for all problems. Will be linking to each day below.

[Day One](#day-one---secret-entrance)
[Day Two](#day-two---gift-shop)
[Day Three](#day-three---lobby)
[Day Four](#day-four---printing-department)
[Day Five](#day-five---cafeteria)

## Day One - Secret Entrance
### Part One
My initial idea is to iterate through and solve in O(n) runtime.
Space complexity should realistically be O(1).
I'll only be incrementing/decrementing the dial value, and a count value of every instance the dial reaches 0.

Gave up on modulo solution, found out I could just use a while loop, and although it makes the solution O(k*n) -- k being the number of iterations in the while loop -- at greatest, it still is significantly easier to understand what I'm doing.
### Part Two
Initially tried to solve by incrementing a count value every time while loop iterated in part one, but that answer was actually very slightly too low. Three under to be exact

Implemented a method within the initial for loop to solve the total number of times I pass and hit 0. This solution is actually a little faster than part one. It's runtime is O(n) and space complexity is also O(1).

The logic for looping through from the left is a little messy, but I thankfully understand what I'm doing, and runtime/space complexity are both as fast as I can get.
## Day Two - Gift Shop
### Part One
Will be brute forcing it for now. Just going to iterate through every value in the given ranges, and just check if all numbers utilizing a two-pointer solution results in an invalid ID.

Ended up with a runtime of O(n * k * l) -- n being the total number of ranges, k being the amount of nums in each range, and l being the length of each digit. Not great, definitely need to improve upon this.
Space complexity was a lot simpler being O(1) since all I'm doing is storing the summation of all invalid IDs.
### Part Two
Did a very similar solution to part one. However, instead of splitting the list and using a two-pointer solution, I swapped that single for loop out for a double for loop to iterate through every valid splice combination for a number, and then split that number and check if all values from the split are equal.

It is significantly slower, with a runtime of O(n * m * k * l). Iterating through each range in n time, iterating through each number in range m times, iterating through each valid num split k times, and finally iterating through each num utilizing the current k split in l time. It's pretty messy, but the whole thing ran in less than 30 seconds so I don't think I'll try to learn a more optimal solution.

Space complexity pretty sure its still O(1), I think you can argue that the ```split_num``` variable in the method ```checkRangeForAllInvalidIDs``` makes it O(l) -- l being the total number of splits for the current split value k.
## Day Three - Lobby
### Part One
My first instinct is to iterate through each line, and grab the highest two digits using a heap data structure. Nevermind am reading through again, will need to come up with a different solution.

With my current method, the line ```818181911112111``` should output ```92```, however with my heap logic I would get ```89```. Ended up doing a greedy sliding window solution, updating the tens digit of the battery if the ones digit was ever larger than the tens, and keeping track of the maximum battery power after each iteration.

Runtime is O(n*m), n being total number of power banks, and m being the length of individual power banks.

Space complexity is O(1).
### Part Two
This is looking a lot rougher, have to get the largest 12 digit battery from each power bank instead of largest 2 digit battery. I feel like you can get away with a sliding window solution, the only issue being you will have to keep track of 11 other variables instead of 1.

Saw a visualization utilizing a stack to find the solution, so will be doing the exact same. The link to that stack visualizer is [here](https://www.reddit.com/r/adventofcode/comments/1pdc396/2025_day_3_part_2_python_terminal_visualization/). I regret making over 22 variables to store every place for my initial implementation... Will show the monstrosity that I previously had to show how absurd this was:
```
def getMaxTwelveDigitPowerOfBank(power_bank: str) -> int:
    battery_max = 0
    l = 0
    m_one = 1
    m_two = 2
    m_three = 3
    m_four = 4
    m_five = 5
    m_six = 6
    m_seven = 7
    m_eight = 8
    m_nine = 9
    m_ten = 10
    for r in range(11, len(power_bank)):
        hunds_bill = int(power_bank[l]) * pow(10, 11)
        tens_bill = int(power_bank[m_one]) * pow(10, 10)
        bill = int(power_bank[m_two]) * pow(10, 9)
        hunds_mill = int(power_bank[m_three]) * pow(10, 8)
        tens_mill = int(power_bank[m_four]) * pow(10, 7)
        mill = int(power_bank[m_five]) * pow(10, 6)
        hunds_th = int(power_bank[m_six]) * pow(10, 5)
        tens_th = int(power_bank[m_seven]) * pow(10, 4)
        th = int(power_bank[m_eight]) * pow(10, 3)
        hunds = int(power_bank[m_nine]) * pow(10, 2)
        tens = int(power_bank[m_ten]) * pow(10, 1)
        ones = int(power_bank[r])
        curr = hunds_bill + tens_bill + bill + hunds_mill + tens_mill + mill + hunds_th + tens_th + th + hunds + tens + ones
        battery_max = max(battery_max, curr)
    print(battery_max)
    return battery_max
```

Average runtime complexity of O(n*m), going through n power banks again, and technically iterating through each power bank in m time.

Space complexity of O(12) since stack's max size will reach at max size 12. I don't know if that is possible, if not then it's just O(1).
## Day Four - Printing Department
### Part One
Will be iterating through at most O(n*m) runtime to get through the entire matrix. Did not want to write out every single check manually, saw online that you could do it in a very simple for loop for each paper roll using:
```
# m being column, n being row
nearby_rolls = 0
for dy in range(-1, 2):
    for dx in range(-1, 2):
        if dy == dx == 0:
            continue
        nearby_rolls += isRoll(paper_matrix, m + dy, n + dx)
```

Runtime complexity is O(n * m), n and m being the rows and columns you have to iterate through respectively.

Space complexity is a little larger, I also saw online to make this method work I would need to add a border around the entire matrix, so its technically O((n+2) * (m+2)), since the border adds two more rows and columns.
### Part Two
Doesn't look too bad, it looks like I'll just have to add a while loop to my part one and break out once I can no longer remove any further rolls of paper. Put the output into a list for each loop, so that I can keep track of when there is no longer anymore movable rolls. I also did this so that I can use the first index of the list as the output to part one.

Runtime complexity is O(k * n * m), n and m being the rows and columns and k being total number of iterations needed. Since part one and two are the same code, I've actually increased part one's runtime complexity.

Space complexity is the exact same as part one.
## Day Five - Cafeteria
### Part One
Runtime complexity is a little confusing. I think realistically it's O(nlogn) because of the mergeRanges method utilizing the built-in sort() method. If not, it's more likely to just be O(k * m), k being the total number of ranges remaining and m being the total number of ingredient IDs.

Space complexity is O(n), storing the entire file as two separate entities, one for the fresh food ranges and all the fresh food ids as separate lists.

### Part Two
Same runtime and space complexities as part one. Just added extra logic to sum all the differences of each fresh food interval.
## Day Six - Trash Compactor
### Part One
I want to implement a way where the space complexity is the size of an individual math problem, but I'm not sure how to properly iterate through that without hardcoding individual rows.

Solved in O(n * m) runtime and space complexity, both in relation to a 2D matrix. A little dissapointed in this solution, was hoping to figure out a way to reduce space complexity, but can't think of a way to do that while also utilizing a 2D array solution.
### Part Two
Took me a while to figure out how the problems were meant to be read, but now I get it thankfully. Although I'm not sure how I'll efficiently read through each problem with the new format.
I can put the logic for both into the same for loop, but that will just cause so much confusion when reading so I'm just going to create a separate function and pass each parsed dataset into that.

Both ended up having the same runtime and space complexities, I feel like I can significantly reduce the space complexity of both problems while maintaining same runtime, but can't think of a solution currently.