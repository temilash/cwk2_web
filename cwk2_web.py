#!/usr/bin/env python3
# cwk2_web.py

from cwk2_crawler import crawl_all_pages, save_index
from load import load as load_index
from print import print_word
from find import find as find_pages

def build():
    """
    Crawl the entire site, build the inverted index in memory,
    save it to disk, and return it.
    """
    index = crawl_all_pages()
    save_index(index)
    return index

def load():
    """
    Load the inverted index from disk and return it.
    """
    return load_index()

def print_cmd(word, index):
    """
    Print occurrences of a single word.
    """
    print_word(word, index)

def find_cmd(phrase, index):
    """
    Find pages containing ALL words in the phrase.
    """
    find_pages(phrase, index)

def main():
    index = {}

    print("Starting Web crawler program...")
    while True:
        cmd = input("\nEnter command (build, load, print <word>, find <phrase>, quit): ").strip()

        if cmd == "build":
            index = build()

        elif cmd == "load":
            index = load()

        elif cmd.startswith("print "):
            if not index:
                print("Index is empty. Run 'build' or 'load' first.")
                continue
            word = cmd.split(" ", 1)[1]
            print_cmd(word, index)

        elif cmd.startswith("find "):
            if not index:
                print("Index is empty. Run 'build' or 'load' first.")
                continue
            phrase = cmd.split(" ", 1)[1]
            find_cmd(phrase, index)

        elif cmd in ("quit", "exit"):
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
