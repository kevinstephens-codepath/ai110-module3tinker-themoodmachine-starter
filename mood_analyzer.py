# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

# Words that flip the sentiment of a nearby positive/negative word.
NEGATORS = {
    "not", "no", "never", "cant", "cannot", "without",
    "don't", "doesn't", "didn't", "isn't", "wasn't", "aren't",
    "won't", "can't", "couldn't", "shouldn't", "wouldn't", "ain't",
}


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Steps:
          - Lowercase the text
          - Pull out text emoticons (":)", ":-(") and emojis as their own tokens
          - Drop punctuation, keeping apostrophes inside words ("don't")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()

        # Alternatives are tried in order at each position, so emoticons win
        # over the punctuation that would otherwise be thrown away.
        token_pattern = re.compile(
            r"(?::-?[()dp/]|;-?[)(]|<3)"            # :) :-( :d :p ;) <3
            r"|[\U0001F300-\U0001FAFF☀-➿]"  # single emoji characters
            r"|[a-z0-9]+(?:'[a-z]+)*"                # words, incl. contractions
        )

        tokens = []
        for token in token_pattern.findall(cleaned):
            if token[0].isalnum():
                # Collapse 3+ repeated letters down to 2: "soooo" -> "soo"
                token = re.sub(r"(.)\1{2,}", r"\1\1", token)
            tokens.append(token)

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        Improvements over a plain presence check:
          - Negation: a negator ("not", "never", "don't", ...) within the two
            tokens before a sentiment word flips its sign ("not happy" -> -1,
            "not bad" -> +1).
          - Counting: every occurrence counts, so "love love love" scores 3.
        """
        score, _, _ = self._score_tokens(self.preprocess(text))
        return score

    def _score_tokens(self, tokens: List[str]) -> Tuple[int, List[str], List[str]]:
        """
        Score a token list. Returns (score, positive_hits, negative_hits),
        where hits are listed as they were counted (negated hits are prefixed
        with "not ", e.g. "not happy" appears under negative_hits).
        """
        score = 0
        positive_hits: List[str] = []
        negative_hits: List[str] = []

        for i, token in enumerate(tokens):
            if token in self.positive_words:
                value = 1
            elif token in self.negative_words:
                value = -1
            else:
                continue

            negated = any(t in NEGATORS for t in tokens[max(0, i - 2):i])
            if negated:
                value = -value
                token = f"not {token}"

            score += value
            (positive_hits if value > 0 else negative_hits).append(token)

        return score, positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        Adjustment: "mixed" is returned when the text contains BOTH positive
        and negative signals ("excited ... but sad"), even if they happen to
        cancel out or one side outweighs the other. A net score alone can't
        tell "mixed" apart from "neutral", so this looks at the hits too.
        The labels match the ones used in TRUE_LABELS in dataset.py.
        """
        score, positive_hits, negative_hits = self._score_tokens(self.preprocess(text))

        if positive_hits and negative_hits:
            return "mixed"
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        score, positive_hits, negative_hits = self._score_tokens(self.preprocess(text))

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
