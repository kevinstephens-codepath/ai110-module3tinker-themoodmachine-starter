# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”  
I used the rule based model for all parts other than Part 4 where I used the ML one.

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.  
The rule-based model is trying to classify a short post or text message into positive, negative or neutral through analyzing the individual words in the text.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
The scoring is just +1 on positive, -1 on negative, and if there is both negative and positive it is neutral.
For the ML version, describe how training works at a high level (no math needed).  
First it turns the words into numbers, learns which words point to which moods, then uses vector prediction to add up the weights and give a final verdict.


## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.  
There are 14 Sample posts, and I came up with a mix of different moods and slang to add to help cast a wider net.

**Labeling process:**  
Explain how you chose labels for your new examples. 
I went with what I know the meanings to be.
Mention any posts that were hard to label or could have multiple valid labels.  
"Lowkey stressed but kind of proud of myself 🥲" It's labeled mixed, and it is, but could be weighted as negative.

**Important characteristics of your dataset:**  
- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.  
- Basically sarcasm and oddities with human language

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made. 
- How positive and negative words affect score  
positive adds one, negative subtracts one, and a mix makes it neutral
- Negation rules you added  
I did not add any negation rules other than some words in the list.
- Emoji handling 
I did add some emoji handling in processing but no actual positive/negative weights. 

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?  
When the mood is obvious, it usually gets it right.

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.  
Sarcasm, mixed moods(no weight, just neutral), and unmapped words.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only
