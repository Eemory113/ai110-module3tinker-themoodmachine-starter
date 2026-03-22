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
    "nice",
    "wonderful",
    "excellent",
    "beautiful",
    "cool",
    "fantastic",
    "lovely",
    "perfect",
    "awesome",
    "brilliant",
    "delightful",
    "fabulous",
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
    "lowkey stressed but kind of proud of myself",
    "no cap this is fire 🔥",
    "I'm literally dying 💀 this is so funny",
    "not the traffic again :(",
    "feeling blessed but also kinda tired",
    "this food hits different fr fr",
    "I'm so done with everything 😩",
    "Actually this isn't that bad? pleasantly surprised :)",
    "highkey obsessed with this song ngl",
    "same energy as stepping on a lego tbh 😬",
    "It ain't bad",
    "I guess it's okay",
    "whatever 🙃",
    "could be worse",
    "I'm not mad just disappointed",
    "it is what it is",
    "The vibe is off ngl",
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
    "mixed",     # "lowkey stressed but kind of proud of myself"
    "positive",  # "no cap this is fire 🔥"
    "positive",  # "I'm literally dying 💀 this is so funny"
    "negative",  # "not the traffic again :("
    "mixed",     # "feeling blessed but also kinda tired"
    "positive",  # "this food hits different fr fr"
    "negative",  # "I'm so done with everything 😩"
    "mixed",     # "Actually this isn't that bad? pleasantly surprised :)"
    "positive",  # "highkey obsessed with this song ngl"
    "negative",  # "same energy as stepping on a lego tbh 😬"
    "positive",  # "It ain't bad" (double negative = positive, despite containing "bad")
    "neutral",   # "I guess it's okay" (lukewarm, minimal enthusiasm)
    "negative",  # "whatever 🙃" (dismissive tone masked by emoji)
    "mixed",     # "could be worse" (backhanded positivity)
    "negative",  # "I'm not mad just disappointed" (denying anger but expressing disappointment)
    "neutral",   # "it is what it is" (resignation/acceptance)
    "negative",  # "The vibe is off ngl" (subtle negativity)
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
