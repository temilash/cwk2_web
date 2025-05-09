import json

#loading the inverted index from the json file
def load(filename="inverted_index.json"):
    try:
        with open(filename, "r") as f:
            index = json.load(f)
        print(f"Inverted index loaded from {filename}.")
        return index
    except FileNotFoundError:
        print(f"Error: {filename} not found. Run 'build' first.")
        return {}