# Problem (unicode 1): Understanding Unicode

(a) What Unicode character does chr(0) return?
ANS: It returns the space (' ') character. --> NO, it actually returns the "Null" character. It represents "nothingness", not a space. chr(32) returns the actual space character.
---
(b) How does this character’s string representation (__repr__()) differ from its printed representa-
tion?
ANS: Printing str returns just the nothing ( ) while printing repr returns "nothing" in quotation marks (' ').
---
(c) What happens when this character occurs in text? It may be helpful to play around with the
following in your Python interpreter and see if it matches your expectations:
ANS: Concatenating ch(0) in text doesn't actually create a space. --> print("this is a test" + chr(0) + "string") returns: this is a teststring
--> because it's not a space, it's "nothing"

# Problem (unicode2): Unicode Encodings

(a) What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than
UTF-16 or UTF-32? It may be helpful to compare the output of these encodings for various
input strings.
ANS: UTF-32 is too long because of it's fixed-width 4-byte encoding. UTF-16 is either 2 or 4 bytes and better for multi-language, but since the majority of the internet is in English, UTF-8 is more efficient. It allows for common symbold to take less space while UTF-16 would still waste 2 bytes on very common characters.
---
(b)Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string into
a Unicode string. Why is this function incorrect? Provide an example of an input byte string
that yields incorrect results.

def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])
>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
ANS: An example input string & byte string that produces an incorrect output is 'こんにちは' (string) with its corresponding bytestring '\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf' (bytestring). It triggers the following error [UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe3 in position 0: unexpected end of data] because the function is trying to decode each byte individually. For more complex symbols like the Japanese ones, which are encoded with multiple bytes for a single character, the function would have to decode all bytes belonging to a single symbols. together
---
(c) Give a two byte sequence that does not decode to any Unicode character(s).
ANS: [227, 129] don't decode into unicode characters. To test, use: print(bytes([227, 129]).decode('utf-8'))



---

## LEARNING:

**Bytes objects: representation vs. iteration**

- `bytes` objects store integers (0–255).
- Printing shows a readable form (e.g., `b'hello'`) when bytes are printable ASCII.
- Iterating yields integers: `for b in b'hello'` gives `104, 101, 108, 108, 111`.
- Use `list(bytes_object)` to see the integer values directly.

**Key takeaway:** The display is a convenience; the underlying data is integers.

**Code example:**
```python
my_bytes = b'hello'
print(my_bytes)              # b'hello' (representation)
print(list(my_bytes))      # [104, 101, 108, 108, 111] (actual values)
for b in my_bytes:
    print(b)               # 104, 101, 108, 108, 111 (integers)
```

**List analogy:**
```python
my_list = [1, 2, 3]
print(my_list)             # [1, 2, 3] (representation)
for item in my_list:
    print(item)            # 1, 2, 3 (actual values)
```
Same concept: representation vs. actual elements.