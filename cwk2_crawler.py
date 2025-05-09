import requests
from bs4 import BeautifulSoup
import time
import re
import json
from collections import defaultdict
from urllib.parse import urljoin, urlparse

def crawl_all_pages(base_url="https://quotes.toscrape.com", delay=6):
    visited = set()
    to_visit = ["/"]
    index = defaultdict(lambda: defaultdict(int))
    session = requests.Session()
    page_count = 0

    while to_visit:
        relative_url = to_visit.pop(0)
        full_url = urljoin(base_url, relative_url)

        # Skip if already visited or external link
        #netloc is used to check if the domain is the same as the base_url
        if relative_url in visited or urlparse(full_url).netloc != urlparse(base_url).netloc:
            continue

        print(f"Crawling {full_url}")
        try:
            response = session.get(full_url)
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Failed to crawl {full_url}: {e}")
            continue

        visited.add(relative_url)
        page_id = relative_url or "/"  # Use '/' for homepage

        # Extract and tokenize all visible text
        text = soup.get_text()
        words = re.findall(r"\b[\w']+\b", text)
        for word in words:
            index[word][page_id] += 1

        # Find and queue new internal links 
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("/") and href not in visited and href not in to_visit:
                to_visit.append(href)

        time.sleep(delay)
        page_count += 1

    print(f"Crawling complete: {page_count} pages visited.")
    return index


# save the index to a json file
def save_index(index, filename="inverted_index.json"):
    with open(filename, "w") as f:
        json.dump(index, f)
    print(f"Inverted index saved to {filename}.")


if __name__ == "__main__":
    
    #main to verify the code is working
    index = crawl_all_pages()
    
    
    print(f"\nTotal words indexed: {len(index)}")
    print("Sample entries:")
    for word in list(index.keys())[:5]:  # Show first 5 words
        print(f"'{word}': {dict(index[word])}")

    save_index(index)
