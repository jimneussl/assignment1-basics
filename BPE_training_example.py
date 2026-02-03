# BPE training example

# ==========================================
# Vocabulary
# ==========================================

# create corpus
corpus = 'low low low low low lower lower widest widest widest newest newest newest newest newest newest'

vocab_b = {bytes([i]):i for i in range(256)} # create vocab, byte:index
vocab_b['<|endoftext|>'] = 256 # add special end token
vocab_idx = {v:k for k, v in vocab_b.items()} # create vocab, but index:byte

# ==========================================
# Pre-tokenization
# ==========================================

pre_tok = corpus.split(' ') # pre-tokenization based on whitespace
print(pre_tok)

tok_word = dict() 
for s in pre_tok: # counting tokens and saving in dict
    tok_word[s] = tok_word.get(s,0) + 1
print(f'token count: {tok_word}')

tok_tuple = tok_word.copy()
for k in list(tok_tuple.keys()): # turning tokens into tuples to separate letters
    tok_tuple[tuple(k)] = tok_tuple.pop(k)

print(f'token count after turning tokens into tuples: {tok_tuple}')


# ==========================================
# Merges
# ==========================================


"""
we loop through list of keys
go into i key, for range length of i - 1
within key, we go into k letter
pair it with k + 1 letter
count occurence

then we go into k+1 letter and compare with k+2
--> there is a nice "sliding window" trick here, can't remember

save the count in a new dict --> NO, WE DON'T RECOUNT, WE CHECK IF THE PAIR OCCURS IN PRE-TUPLED TOKEN LIST
--> saves compute
--> e.g., we find pair 'lo'
- then ckech in which tokens lo occurs and add the counts
- e.g., lo occurs in low: 5 and lower: 2
- so we add 5 and 2 and get count of 7 for 'lo'
grab the merge with highest count
include max() to grab lexicographically greatest pair if there's a tie for highest count

update old dict to replace old bytes with byte pairs
e.g., instead of 'l', 'o', 'w' --> 'l', 'ow'

do this several rounds --> n loops
gradually merge more and introduce new tokens

need to keep track of the new tokens so they can be added to the vocab in the end
"""
pair_set = set()
pair_list = list()
for i in list(tok_tuple.keys()): # pair up the letters in each word
    for k in range(len(i)-1):
        pair = i[k] + i[k+1]
        if pair not in pair_set:
            pair_set.add(pair)
            pair_list.append(pair)

print(f'pair list: {pair_list}')

pair_count = {pair:0 for pair in pair_list}

for pair in pair_count.keys():
    for tok in tok_word.keys():
        if pair in tok:
            pair_count[pair] += tok_word[tok]
print('=============================')
print('=============================')
print(f'>>>> PAIR COUNT: {pair_count}')


"""
next up, need to implement:
'We would then merge the pre-tokens so that we end up with {(l,o,w): 5, (l,o,w,e,r): 2, (w,i,d,e,st): 3, (n,e,w,e,st): 6}'
"""