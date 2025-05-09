#printing the word and page wherre it occurs
def print_word(word, index):
    word = word.lower()
    if word in index:
        pages = index[word]
        print(f"\nAll links are relative to https://quotes.toscrape.com")
        print(f"\nWord: '{word}'\n")
        print(f"Found in {len(pages)} page(s):")
        for page, count in pages.items():
            print(f"- {page} → {count} occurrence(s)")
    else:
        print(f"\nWord: '{word}' not found in the index.")
