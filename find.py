def find(phrase, index):
    words = phrase.lower().split()
    if not words:
        print("Please enter at least one word.")
        return

    # Collect sets of pages for each word
    page_sets = []
    for word in words:
        if word in index:
            page_sets.append(set(index[word].keys()))
        else:
            print(f"Word '{word}' not found in the index.")
            return

    # Intersect all sets to find common pages
    common_pages = set.intersection(*page_sets)

    if common_pages:
        print(f"\nAll links are relative to https://quotes.toscrape.com")
        print(f"\nPages containing all words '{' '.join(words)}':")
        for page in sorted(common_pages):
            print(f"- {page}")
    else:
        print("No page contains all the given words.")
