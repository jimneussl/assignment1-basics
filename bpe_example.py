# BPE training example

# ==========================================
# Vocabulary
# ==========================================

# create corpus
corpus = 'low low low low low lower lower widest widest widest newest newest newest newest newest newest'

token_to_idx = {bytes([i]):i for i in range(256)} # create vocab, byte:index
token_to_idx['<|endoftext|>'] = 256 # add special end token
idx_to_token = {v:k for k, v in token_to_idx.items()} # create vocab, but index:byte

# ==========================================
# Pre-tokenization
# ==========================================

word_freq = {}
for token in corpus.split(' '): # pre-tokenization based on whitespace
    key = tuple(token)
    word_freq[key] = word_freq.get(key, 0) + 1

# ==========================================
# Merges
# ==========================================

# ----- COUNT PAIRS -----
def get_pair_counts(vocab):
    counts = {}
    for word_tuple, freq in vocab.items():
        for i in range(len(word_tuple) - 1):
            pair = (word_tuple[i], word_tuple[i+1])
            counts[pair] = counts.get(pair, 0) + freq
    return counts

# ----- SELECT PAIR WITH HIGHEST COUNT -----
best_pair = max(pair_counts, key=lambda p: (pair_counts[p], p))

# ----- MERGE PRE-TOKENS -----
def apply_merge(word_tuple, pair):
    i = 0
    result = []
    while i < len(word_tuple):
        if i == len(word_tuple) - 1:
            result.append(word_tuple[i])
            i += 1
        elif word_tuple[i] == pair[0] and word_tuple[i+1] == pair[1]:
            result.append(pair[0] + pair[1])
            i += 2
        else:
            result.append(word_tuple[i])
            i += 1
    return tuple(result)

new_dict = {}
for word_tuple, count in word_freq.items():
    new_word = apply_merge(word_tuple, best_pair)
    new_dict[new_word] = count
word_freq = new_dict


print(f'new dict: {word_freq}')