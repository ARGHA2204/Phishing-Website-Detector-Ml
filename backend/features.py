import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # 1. URL length
    features.append(len(url))

    # 2. Has HTTPS
    features.append(1 if "https" in url else 0)

    # 3. Count of dots
    features.append(url.count('.'))

    # 4. Presence of @
    features.append(1 if "@" in url else 0)

    # 5. Presence of -
    features.append(1 if "-" in url else 0)

    # 6. Count of digits
    features.append(sum(c.isdigit() for c in url))

    # 7. Suspicious words
    suspicious = ["login", "verify", "bank", "update"]
    features.append(1 if any(word in url for word in suspicious) else 0)

    return features