"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "lit",
    "goated",
    "slay",
    "dope",
    "vibing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "mid",
    "cringe",
    "trash",
    "ugh",
    "sucks",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Highkey love hanging out with my friends, no cap 😂",
    "Lowkey stressed but kind of proud of myself 🥲",
    "I absolutely love getting stuck in traffic",
    "Finally finished my project! Feeling amazing :)",
    "My phone died right before the interview :(",
    "Just picked up groceries and headed home",
    "That movie was so bad it was actually fun 💀",
    "Excited for my new job, but sad to leave my team",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "Highkey love hanging out with my friends, no cap 😂"
    "mixed",     # "Lowkey stressed but kind of proud of myself 🥲"
    "negative",  # "I absolutely love getting stuck in traffic" (sarcasm)
    "positive",  # "Finally finished my project! Feeling amazing :)"
    "negative",  # "My phone died right before the interview :("
    "neutral",   # "Just picked up groceries and headed home"
    "mixed",     # "That movie was so bad it was actually fun 💀" (could be positive)
    "mixed",     # "Excited for my new job, but sad to leave my team"
]
