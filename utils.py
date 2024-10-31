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
        return None  # If score is out of range
    
def generate_stopwords():
    STOP_WORDS = set(
        """
    a about above across after afterwards again against all almost alone along
    already also although always am among amongst amount an and another any anyhow
    anyone anything anyway anywhere are around as at

    back be became because become becomes becoming been before beforehand behind
    being below beside besides between beyond both bottom but by

    call can cannot ca could

    did do does doing done down due during

    each eight either eleven else elsewhere empty enough even ever every
    everyone everything everywhere except

    few fifteen fifty first five for former formerly forty four from front full
    further

    get give go

    had has have he hence her here hereafter hereby herein hereupon hers herself
    him himself his how however hundred

    i if in indeed into is it its itself

    keep

    last latter latterly least less

    just

    made make many may me meanwhile might mine more moreover most mostly move much
    must my myself

    name namely neither never nevertheless next nine no nobody none noone nor not
    nothing now nowhere

    of off often on once one only onto or other others otherwise our ours ourselves
    out over own

    part per perhaps please put

    quite

    rather re really regarding

    same say see seem seemed seeming seems serious several she should show side
    since six sixty so some somehow someone something sometime sometimes somewhere
    still such

    take ten than that the their them themselves then thence there thereafter
    thereby therefore therein thereupon these they third this those though three
    through throughout thru thus to together too top toward towards twelve twenty
    two

    under until up unless upon us used using

    various very very via was we well were what whatever when whence whenever where
    whereafter whereas whereby wherein whereupon wherever whether which while
    whither who whoever whole whom whose why will with within without would

    yet you your yours yourself yourselves
    """.split()
    )
    print("length of Stop Words",len(STOP_WORDS))
    contractions = ["n't", "'d", "'ll", "'m", "'re", "'s", "'ve"]
    STOP_WORDS.update(contractions)

    for apostrophe in ["‘", "’"]:
        for stopword in contractions:
            STOP_WORDS.add(stopword.replace("'", apostrophe))
    return STOP_WORDS          

# Function to tokenize and preprocess text
def tokenize(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters, and exclude numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces

    # Handle multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space

    text = re.sub(r'[^\w\s]', '', text)

    # Split into tokens
    tokens = text.split()

    # Remove any empty tokens (in case of leading/trailing spaces)
    tokens = [token for token in tokens if token]

    return tokens
# Function to generate vocabulary
def apply_stopwords(vocab, stopwords):
    return vocab - stopwords
def generate_vocab(train_df):
    tokens = set()
    for _, row in train_df.iterrows():
        row_tokens = tokenize(row['sentence'])
        tokens.update(row_tokens)  # Use set to avoid duplicates
    return np.array(sorted(tokens))
    



