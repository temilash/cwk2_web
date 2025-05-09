def find(phrase, index):
    words = phrase.split()
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
        # Score each page by summing word frequencies
        scores = {}
        for page in common_pages:
            score = sum(index[word][page] for word in words)
            scores[page] = score

        # Sort pages by score descending
        ranked_pages = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        print(f"\nAll links are relative to https://quotes.toscrape.com")
        print(f"\nPages containing all words '{' '.join(words)}':")
        for i, (page, score) in enumerate(ranked_pages, 1):
            print(f"{i}. {page} → score: {score}")
    else:
        print("No page contains all the given words.")
