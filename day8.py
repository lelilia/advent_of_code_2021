""" Advent of code 2021 day 8 """

INPUT_FILE = "input8.txt"

with open(INPUT_FILE) as f:
    input_txt = f.readlines()


class Decoder:
    def __init__(self, input_line):
        input_part, output_part = input_line.split(" | ")
        self.input = input_part.split()
        self.output = output_part.split()
        self.code = {}
        self.decode = {}
        self.result = None
        self.output_count = 0

        self.find_code()
        self.get_decode()
        self.decode_output()

    def get_output_count(self):
        return self.output_count

    def get_result(self):
        return self.result

    def get_decode(self):
        for key, value in self.code.items():
            value = self.get_sorted_string(value)
            self.decode[value] = key

    def decode_output(self):
        res = 0
        for o in self.output:
            o = self.get_sorted_string(o)
            number = self.decode[o]
            res = res * 10 + number
            if number in (1, 4, 7, 8):
                self.output_count += 1
        self.result = res

    def get_sorted_string(self, s):
        return "".join(sorted(s))

    def find_code(self):
        self.code[1] = [i for i in self.input if len(i) == 2][0]
        self.code[4] = [i for i in self.input if len(i) == 4][0]
        self.code[7] = [i for i in self.input if len(i) == 3][0]
        self.code[8] = [i for i in self.input if len(i) == 7][0]

        for i in self.input:
            if not 4 < len(i) < 7:
                continue
            set_i = set(i)
            if len(i) == 5:
                if len(set(self.code[1]) - set_i) == 0:
                    self.code[3] = i
                elif len((set(self.code[4]) - set(self.code[1])) - set_i) == 0:
                    self.code[5] = i
                else:
                    self.code[2] = i
            if len(i) == 6:
                if len(set(self.code[4]) - set_i) == 0:
                    self.code[9] = i
                elif len(set(self.code[1]) - set_i) == 0:
                    self.code[0] = i
                else:
                    self.code[6] = i


summe = 0
output_summe = 0
for line in input_txt:
    d = Decoder(line)

    summe += d.get_result()
    output_summe += d.get_output_count()

print("Part 1:\t", output_summe)
print("Part 2:\t", summe)

exit()
# messy first attempt

# exit()
input_list = output_list = []
for line in input_txt:
    i, o = line.split(" | ")
    output_list.append(o.split())


# count unique length
flat_output = [item for sublist in output_list for item in sublist]

length_output = [len(item) for item in flat_output]

summe = 0
for item in length_output:
    if item in (2, 4, 3, 7):
        summe += 1
print(summe)


# Part 2


class Decoder:
    def __init__(self, input, output):
        self.input = input.split()
        self.output = output.split()
        self.code = {}
        self.segments = {}
        self.find_numbers()
        # self.return_result()

    def find_numbers(self):
        self.code[1] = [i for i in self.input if len(i) == 2][0]
        self.code[4] = [i for i in self.input if len(i) == 4][0]
        self.code[7] = [i for i in self.input if len(i) == 3][0]
        self.code[8] = [i for i in self.input if len(i) == 7][0]

        for i in self.input:
            if len(i) != 6:
                continue
            if len(i) == 6:
                if (
                    len(set(i) - set(self.code[4])) == 2
                    and len(set(self.code[4]) - set(i)) == 0
                ):
                    self.code[9] = i
                elif (
                    len(set(i) - set(self.code[7])) == 3
                    and len(set(self.code[7]) - set(i)) == 0
                ):
                    self.code[0] = i
                else:
                    self.code[6] = i

        for i in self.input:
            if len(i) != 5:
                continue
            if len(set(self.code[9]) - set(i)) == 2:
                self.code[2] = i
            elif len(set(i) - set(self.code[6])) == 0:
                self.code[5] = i
            else:
                self.code[3] = i

        # self.code[6] = [i for i in self.input if len(i) == 6 and (self.code[1][0] not in i or self.code[1][1] not in i)][0]
        # self.code[9] = [i for i in self.input if len(i) == 6 and (self.code[4][j] in i for j in range(4))][0]
        # self.code[0] = [i for i in self.input if len(i) == 6 and i != self.code[6] and i != self.code[9]][0]

        # self.code[3] = [i for i in self.input if len(i) == 5 and (self.code[7][j] in i for j in range(3))][0]
        # self.code[5] = [i for i in self.input if len(i) == 5 and (i[j] in self.code[6] for j in range(5))][0]
        # self.code[2] = [i for i in self.input if len(i) == 5 and i != self.code[3] and i != self.code[5]][0]

    def return_result(self):
        res = ""
        for i in self.output:
            for key, value in self.code.items():
                if len(value) != len(i):
                    continue
                if len(set(value) - set(i)) == 0:
                    res += str(key)

        return res


print("------")

summe = 0
for line in input_txt:
    i, o = line.split(" | ")
    d = Decoder(i, o)
    summe += int(d.return_result())
    # print(d.input)
    # print(d.output)
    # print(d.code)
    # print( d.return_result())

print(summe)
