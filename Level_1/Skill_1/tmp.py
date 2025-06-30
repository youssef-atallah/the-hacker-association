# 10. Extract all vowels from a string.
def extract_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char in vowels])

print(extract_vowels("Hello World"))  # Output: eoO
print(extract_vowels("Hello super H"))   # eoue
