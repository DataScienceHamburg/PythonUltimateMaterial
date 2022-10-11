#%% packages
from collections import Counter
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#%% find unique words
# approach:
# 1. convert all to lower case
# 2. clean up special charaters
# 3. 
text_lwr = text.lower()
words = text_lwr.split()

words_cleaned = [word.strip('.,!;()[]') for word in words]
words_cleaned = [word.replace("'s", '') for word in words_cleaned]

# %%
Counter(words_cleaned).most_common(10)
# %%
