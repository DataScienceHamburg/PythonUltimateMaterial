#%%
from transformers import pipeline
# %%
gpt2_generator = pipeline('text-generation', model='gpt2')

#%%
sentences = gpt2_generator("bert and lea are ", do_sample=True, top_k=5, temperature=0.9, max_length=180, num_return_sequences=3)
# %%
sentences
# %%
