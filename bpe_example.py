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
    for word, freq in vocab.items():
        for i in range(len(word) - 1):
            pair = (word[i], word[i+1])
            counts[pair] = counts.get(pair, 0) + freq
    return counts

# ----- MERGE PRE-TOKENS -----
def apply_merge(word, pair):
    i = 0
    result = []
    while i < len(word):
        if i == len(word) - 1:
            result.append(word[i])
            i += 1
        elif word[i] == pair[0] and word[i+1] == pair[1]:
            result.append(pair[0] + pair[1])
            i += 2
        else:
            result.append(word[i])
            i += 1
    return tuple(result)

# ----- LOOP THOUGH ALL STEPS NUM_MERGES TIMES -----
num_merges = 10

for i in range(num_merges):
    # step 1: count pairs
    pair_counts = get_pair_counts(word_freq)

    # step 2: select best pair
    best_pair = max(pair_counts, key=lambda p: (pair_counts[p], p))

    # step 3: merge
    new_dict = {}
    for word, count in word_freq.items():
        new_word = apply_merge(word, best_pair)
        new_dict[new_word] = count
    word_freq = new_dict
    
    print(f'vocab after round {i+1} of merges: {word_freq}')