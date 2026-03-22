# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”
I mostly stuck to the rule based model but tinkered a bit with the machine learning model to see the diffrence.

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.
classify sentinces as positive, negative or neutral based on the words in the text.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.
twenty four in total, i added ten.
**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.
I asked copilot for some examples but specified to add some that are very uncertian in wording

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages
examples that are mixed or ambigous i had added are:
"it ain't all bad" and "It could be worse"
**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.
It had trouble comperhending mixed sentinces and tended to flag them as negitave.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels
I had it take or give one point for negtive and positive words then had it give or take away two based on strong negtive words in the wordlist.

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?
It seemed to be more accurate the more words i added, it seemed to work best with strong words/

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.
it does not work well with unfamiler slang or subtlety/

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?
I did not see too much of a improvement after adding more data to the dataset it still only really got the specific examples correct/

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.
i think the main strengh would be depend on the amount of data you gave the model, with the amount i added it overfitted to the training data.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.
"It ain't bad" - this was correct due to me specficlly adding it to the dataset
"it is what it is" this was correct for the same reason


**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.
"today was nice"
"nice hat!"
both of these i tried with the rule based and then the ML model, the rule based was fixed after adding it to the dataset but the ML kept on getting any sentince with the word "nice" wrong.
## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled
the main limitations was the size of the dataset and its inability to detect sarcasm well, it also depended heavily on the words i used.
## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages
I think there is a potential for misclassfying sarscasm as distress.
for privicy i can see ML expanding its dataset with confidential information potentally being a problem.

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
I would add more data and include a real test set.
