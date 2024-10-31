import numpy as np
import re


def map_classes(score):
    if 0 <= score <= 0.2:
        return 0  # Very negative
    elif 0.2 < score <= 0.4:
        return 1  # Negative
    elif 0.4 < score <= 0.6:
        return 2  # Neutral
    elif 0.6 < score <= 0.8:
        return 3  # Positive
    elif 0.8 < score <= 1.0:
        return 4  # Very positive
    else:
        return None


def tokenize(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters, and exclude numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep only letters and spaces

    # Handle multiple spaces
    text = re.sub(
        r"\s+", " ", text
    ).strip()  # Replace multiple spaces with a single space

    text = re.sub(r"[^\w\s]", "", text)

    # Split into tokens
    tokens = text.split()

    # Remove any empty tokens (in case of leading/trailing spaces)
    tokens = [token for token in tokens if token]
    
    return tokens


def generate_vocab(train_df):
    tokens = set()
    for _, row in train_df.iterrows():
        row_tokens = tokenize(row["sentence"])
        tokens.update(row_tokens)
    return np.array(sorted(tokens))
