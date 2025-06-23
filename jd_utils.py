import spacy
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")

def extract_keywords(jd_text):
    doc = nlp(jd_text)
    return list(set([chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 3]))

def match_keywords(resume_text, keywords):
    matches = {kw: fuzz.partial_ratio(kw.lower(), resume_text.lower()) for kw in keywords}
    matched = {k: v for k, v in matches.items() if v > 70}
    return matched, len(matched) / len(keywords) * 100
