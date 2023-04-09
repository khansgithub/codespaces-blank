import requests

def count_words_at_url(url):
    resp = requests.get(url, timeout=20)
    return len(resp.text.split())