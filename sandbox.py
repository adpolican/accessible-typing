import pygtrie

#t = pygtrie.StringTrie()

class NonUniqueError(Exception):
    pass

L_PINKY = 1
L_RING = 2
L_MID = 3
L_INDEX = 4
L_THUMB = 5
R_THUMB = 5
R_INDEX = 6
R_MID = 7
R_RING = 8
R_PINKY = 9

LETTERMAP = {
    'a': L_PINKY,
    'b': L_INDEX,
    'c': L_MID,
    'd': L_MID,
    'e': L_MID,
    'f': L_INDEX,
    'g': L_INDEX,
    'h': R_INDEX,
    'i': R_INDEX,
    'j': R_INDEX,
    'k': R_MID,
    'l': R_RING,
    'm': R_INDEX,
    'n': R_INDEX,
    'o': R_RING,
    'p': R_PINKY,
    'q': L_PINKY,
    'r': L_INDEX,
    's': L_RING,
    't': L_INDEX,
    'u': R_INDEX,
    'v': L_INDEX,
    'w': L_RING,
    'x': L_RING,
    'y': R_RING,
    'z': L_PINKY,
    ';': R_PINKY,
    }

def only_letters(word):
    word = word.strip().lower()
    abt = 'abcdefghijklmonpqrstuvwxyz'
    word = ''.join(filter(lambda l: l in abt, word))
    return word

def is_word(line):
    return '#' not in line and '!' not in line

def get_words(fname='wordlist.txt'):
    with open(fname) as wordfile:
        word_list = list(filter(is_word, wordfile.readlines()))
    word_list = [only_letters(word) for word in word_list]
    return word_list

def encode_word(word):
    return tuple([LETTERMAP[letter] for letter in word])

def decode_word(coded_word):
    key = encode_word(coded_word)
    word_list = encoding_map[key]
    return word_list

word_list = get_words()
encoding_map = {}
for word in word_list:
    try:
        encoding_map[encode_word(word)] += [word]
    except KeyError:
        encoding_map[encode_word(word)] = [word]
    except:
        print('Skipping {}'.format(word))

print('Calculating collisions')
all_collisions = 0
most_collisions = 0
collisions = []
total_words = 100000
for encoding, words in encoding_map.items():
    if len(words) > most_collisions:
        collisions = words
        most_collisions = len(words)
    all_collisions += len(words)
print('average colisions: {}'.format(all_collisions/total_words))
print('most collisions: {}'.format(most_collisions))
print(collisions)


while True:
    encoded_word = input('Input a word: ')
    print('Decoded: {}'.format(decode_word(encoded_word)[0]))
