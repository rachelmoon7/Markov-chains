"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_string = ''
    open_file = open(file_path)
    for line in open_file:
        file_string += line 
    
    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    list_of_words = text_string.split()

    for i in range(len(list_of_words)):
        starting_point = (list_of_words[i], list_of_words[i+1])
        dict_values = []
        
        if i == len(list_of_words) - 2:
            break
        elif list_of_words[i+2] == starting_point[0] and list_of_words[i+1] == starting_point[1]: 
            dict_values.append(list_of_words[i+2])

        for i in range(len(list_of_words)):
            if list_of_words[i] == starting_point[0] and list_of_words[i+1] == starting_point[1]:
                dict_values.append(list_of_words[i + 2])

        chains[starting_point] = dict_values

    return chains
# print(make_chains("would you could you in a house? would you couldx you in a farm? would you hello"))



def make_text(chains):
    """Return text from chains."""

    # words.append(random.choice(list(chains.keys())))
    # for key in chains.keys():
    #     words.extend(random.choice(chains[key]))
    # print(words)

    lookup_key = choice(list(chains.keys()))
    result_list = [lookup_key[0], lookup_key[1]]
    next_word = choice(chains[lookup_key])
        
    for pairs in chains:
        try: 
            result_list.append(next_word)
            lookup_key = (lookup_key[1], next_word)
            next_random_word = choice(chains[lookup_key])
            next_word = next_random_word
        except: 
            # lookup_key = choice(list(chains.keys())) 
            # result_list.extend(list([lookup_key]))
            break

    return ' '.join(result_list)
# print(make_text(make_chains("would you could you in a house? would you couldx you in a farm? would you hello")))


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
