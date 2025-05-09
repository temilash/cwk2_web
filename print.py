#printing the word and page wherre it occurs
def print_word(word, index):
    if word in index:
        pages = index[word]
        print(f"\nAll links are relative to https://quotes.toscrape.com")
        print(f"\nWord: '{word}'\n")
        print(f"Found in {len(pages)} page(s):")
        for i, (page, count) in enumerate(sorted(pages.items(), key=lambda item: item[1], reverse=True), 1):
            print(f"{i}. {page} → {count} occurrence(s)")
    else:
        print(f"\nWord: '{word}' not found in the index.")
