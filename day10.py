INPUT_FILE = "input10.txt"


with open(INPUT_FILE) as f:
    input_lines = f.readlines()

points_broken = {")": 3, "]": 57, "}": 1197, ">": 25137}

points_complete = {")": 1, "]": 2, "}": 3, ">": 4}

partner_bracket = {"(": ")", "[": "]", "{": "}", "<": ">"}

score_broken = 0
score_complete = []


for line in input_lines:
    stack = []
    for char in line.strip():
        if char in partner_bracket.keys():
            stack.append(char)
        else:
            if char == partner_bracket[stack[-1]]:
                stack.pop()
            else:
                score_broken += points_broken[char]
                break
    else:
        this_score = 0
        while stack:
            curr = stack.pop()
            char = partner_bracket[curr]
            this_score = this_score * 5 + points_complete[char]
        score_complete.append(this_score)

print("Part 1:\t", score_broken)
print("Part 2:\t", sorted(score_complete)[len(score_complete) // 2])


# first messy attempt
exit()
penalties = {")": 3, "]": 57, "}": 1197, ">": 25137}

auto_completion_score = {")": 1, "]": 2, "}": 3, ">": 4}

total_score = 0
total_score2 = []
for line in input_lines:
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        if char in ")]}>":
            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    total_score += penalties[char]
                    break
            if char == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    total_score += penalties[char]
                    break
            if char == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    total_score += penalties[char]
                    break
            if char == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    total_score += penalties[char]
                    break
    else:
        this_score = 0
        while stack:
            curr = stack.pop()
            if curr == "(":
                char = ")"
            elif curr == "[":
                char = "]"
            elif curr == "{":
                char = "}"
            elif curr == "<":
                char = ">"

            this_score *= 5
            this_score += auto_completion_score[char]
        total_score2.append(this_score)


print(total_score)
print(total_score2)
total_score2 = sorted(total_score2)

print(total_score2[(len(total_score2)) // 2])
