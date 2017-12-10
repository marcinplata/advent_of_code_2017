"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a
password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""


def read_file(path):
    rows = []
    with open(path) as file:
        for line in file:
            line = line[:-1] if line[-1] == '\n' else line
            rows.append(line.split(" "))
    return rows


def valid_passphrase(rows):
    valid = 0
    for row in rows:
        if len(set(row)) == len(row):
            valid += 1
    return valid


rows = read_file("tests/day_04_test")
print(valid_passphrase(rows))


"""
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two 
words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to 
form any other word in the passphrase. 

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
"""


def valid_passphrase(rows):
    valid = 0
    for row in rows:
        d = set()
        for w in row:
            w = "".join(sorted(w))
            if w in d:
                continue
            else:
                d.add(w)
        if len(row) == len(d):
            valid += 1
            # print(row)
    return valid


rows = read_file("tests/day_04_test")
print(valid_passphrase(rows))

