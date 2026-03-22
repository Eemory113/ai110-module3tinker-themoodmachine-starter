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
import string
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


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
        
        # Track cumulative session score
        self.session_score = 0

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Improvements implemented:
          - Removes punctuation
          - Handles simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalizes repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()
        
        # Handle simple emoticons and emojis by replacing with descriptive words
        emoticons = {
            ':)': ' happy ',
            ':(': ' sad ',
            ':-D': ' happy ',
            ':-d': ' happy ',
            ':D': ' happy ',
            ':d': ' happy ',
            ':-p': ' silly ',
            ':-P': ' silly ',
            ':P': ' silly ',
            ':-p': ' silly ',
            '😂': ' laughing ',
            '🥲': ' smiling ',
            '💀': ' dying ',
        }
        for emoticon, replacement in emoticons.items():
            cleaned = cleaned.replace(emoticon, replacement)
        
        # Remove punctuation
        cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
        
        # Normalize repeated characters (e.g., "soooo" -> "soo", "!!" -> "!")
        cleaned = re.sub(r'(.)\1{2,}', r'\1\1', cleaned)
        
        tokens = cleaned.split()
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.
        
        Modeling improvement: Negation handling and weighted word scoring
        Words like "not", "never", "no" flip the sentiment of the following word.
        For example: "not happy" is treated as negative, "not bad" is treated as positive.
        
        Strong positive words (love, amazing, excellent, etc.) contribute +2.
        Regular positive words contribute +1.
        Displays scoring breakdown for transparency.
        """
        tokens = self.preprocess(text)
        score = 0
        negation_words = {
            "not", "never", "no", "dont", "doesnt", "isnt", "arent", "wasnt", "werent",
            "cant", "cannot", "shouldnt", "wouldnt", "couldnt", "havent", "hasnt", "hadnt",
            "wont", "didnt", "neither", "nobody", "nowhere", "nothing",
        }
        
        # Strong positive words with extra weight
        strong_positive = {
            "love", "amazing", "excellent", "wonderful", "fantastic", "perfect", "awesome", 
            "great", "best", "brilliant", "superb", "terrific", "marvelous", "splendid",
            "delighted", "fabulous", "incredible", "outstanding", "exceptional", "magnificent",
            "beautiful", "lovely", "wonderful", "cheerful", "thrilled", "ecstatic", "delightful",
            "glad", "joyful", "excited", "inspiring", "uplifting", "fabulous"
        }
        
        print("\n--- Scoring Breakdown ---")
        print(f"Text: '{text}'")
        print(f"Tokens: {tokens}")
        print()
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            # Check if current token is a negation word and there's a next token
            if token in negation_words and i + 1 < len(tokens):
                next_token = tokens[i + 1]
                
                # Check if next token is positive (either in dataset or strong_positive)
                is_positive = next_token in self.positive_words or next_token in strong_positive
                is_strong = next_token in strong_positive
                
                # If next token is positive, negate it (make it negative)
                if is_positive:
                    if is_strong:
                        score -= 2
                        print(f"  '{token}' + '{next_token}' (strong positive negated) → -2 | Score: {score}")
                    else:
                        score -= 1
                        print(f"  '{token}' + '{next_token}' (positive negated) → -1 | Score: {score}")
                    i += 2
                    continue
                
                # If next token is negative, negate it (make it positive)
                is_negative = next_token in self.negative_words
                if is_negative:
                    score += 1
                    print(f"  '{token}' + '{next_token}' (negative negated) → +1 | Score: {score}")
                    i += 2
                    continue
            
            # Weighted scoring for positive words
            is_positive = token in self.positive_words or token in strong_positive
            is_strong = token in strong_positive
            
            if is_positive:
                if is_strong:
                    score += 2  # Strong positive words worth more
                    print(f"  '{token}' (strong positive) → +2 | Score: {score}")
                else:
                    score += 1
                    print(f"  '{token}' (positive) → +1 | Score: {score}")
            elif token in self.negative_words:
                score -= 1
                print(f"  '{token}' (negative) → -1 | Score: {score}")
            
            i += 1
        
        print(f"\n--- Total Score: {score} ---\n")
        
        # Add to session total
        self.session_score += score
        print(f">>> Session Total Score: {self.session_score} <<<\n")
        
        return score

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
        """
        score = self.score_text(text)
        
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
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
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )

    # ---------------------------------------------------------------------
    # Session tracking
    # ---------------------------------------------------------------------

    def get_session_score(self) -> int:
        """Return the cumulative mood score for the current session."""
        return self.session_score

    def reset_session_score(self) -> None:
        """Reset the session score to zero."""
        self.session_score = 0
        print("\n✓ Session score reset to 0\n")
