import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    """
    Process the text using spaCy for tokenization, POS tagging, etc.
    """
    doc = nlp(text)
    
    # Extract tokens and their part of speech
    token_info = [(token.text, token.pos_) for token in doc]
    
    return token_info

def extract_entities(text):
    """
    Extract named entities (NER) from the text using spaCy.
    """
    doc = nlp(text)
    
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities
