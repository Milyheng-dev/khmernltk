from khmernltk import word_tokenize

raw_text = "សមាជិកសមាជិកាបានបន្តចុះផ្សាយព័ត៌មានឃោសនាជាបន្តបន្ទាប់ទៀតនៅក្នុងស្រុកបាធាយខេត្តកំពង់ចាម?"

# Tokenize into a list of words
words = word_tokenize(raw_text)

# Remove empty/whitespace tokens
cleaned_words = [word.strip() for word in words if word.strip()]

print("Tokens:", cleaned_words)
print("Number of tokens:", len(cleaned_words))
print("Number of characters:", len(raw_text))