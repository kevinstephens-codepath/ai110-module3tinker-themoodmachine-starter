# The Mood Machine
## Part 1 - Build the Dataset
### Noting which labels feel easy to label vs ambiguous.
Easy:
- I love this class so much
- Today was a terrible day
- So excited for the weekend

Ambiguous:  
- Feeling tired but kind of hopeful
- This is fine
- I am not happy about this

### Added 8 new sample posts and true labels:
- "positive",  # "Highkey love hanging out with my friends, no cap 😂"
- "mixed",     # "Lowkey stressed but kind of proud of myself 🥲"
- "negative",  # "I absolutely love getting stuck in traffic" (sarcasm)
- "positive",  # "Finally finished my project! Feeling amazing :)"
- "negative",  # "My phone died right before the interview :("
- "neutral",   # "Just picked up groceries and headed home"
- "mixed",     # "That movie was so bad it was actually fun 💀" (could be positive)
- "mixed",     # "Excited for my new job, but sad to leave my team"

### Ran and saw change in CLI.

> Q. What did adding your new labeled posts change in the output, and what would break if the lists were mismatched?  
> A. It added the new labels within the CLI output within the Rule-based evaluation, and batch demo. If the lists were mismatched the wrong "feeling" would be tied to the wrong post.

## Part 2 - Engineer the rule-based brain
### Implemented preprocess, score_text, predict_label
### Obvious Test Sentences:
- Positive: I am happy - Result: Positive
- Negative: I am sad - Result: Negative
- Neutral: I am ok - Result: Neutral

> Q. Which token or rule had the biggest effect on one prediction you checked?  
> A. The neutral rule has the biggest effect to me, making so any combo is neutral may change later, as if there are 100 love but only one not love in the text it would be neutral even though I would expect a positive sesult.

## Part 3 - Break It on Purpose
### My 3 Breaker posts
You: I'm fine 🙂
Model: neutral
You: I love getting stuck in traffic
Model: positive
You: This party is fire
Model: neutral

All neutral from our model.
### Failure patern
- For this level of model, I'd say something realistic we could fix is some slang not being in the word lists.
- I would say that modern slang is the biggest missing piece.
### Applying a fix:
Positive slang words added:
- lit
- goated
- slay
- dope
- vibing
Negative slang words added:
- mid
- cringe
- trash
- ugh
- sucks

The change let more modern slang be used in the model, but the sarcasm is still going over the models head.

> Q. What failure pattern did you see, and what specific change made it less wrong?  
> A. The failure was in modern slang, and adding more slang terms helped make it a bit less wrong for modern posts.

## Part 4 - Evaluate and Compare to ML
### Studying mismatches:
I chose:  
"My phone died right before the interview :(" -> predicted=neutral, true=negative  
As the focus. I will document this as a limitation for now.
### ML_Experiments
- It failed to see lit as positive, otherwise it is an improvment over my model.
> Q. Which example did the ML model handle differently from the rule-based one, and what does that tell you about the data?  
> A. "Today was lit!" was handled as negative in ML, but I made sure my model could handle it as positive. That means the ML data has lit as a negative word.

## Part 5 - The Model Card
> Q. What is one limitation or bias note that belongs in the model card, and what evidence supports it?
> A. "I locked myself out of the office :)" is taken as a positive, but is obviously a negative post. The fact that it is labeled as positive when running it through the mood analyzer.