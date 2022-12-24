# Contextual Embeddings for Scene Based Movie Search

Project associated with CSCI 544 Fall 2022, Group 44

A project based on retrieving movie titles based on 'tip of the tongue' scene descriptions. 

Poster link: https://drive.google.com/file/d/1yYU_hrMLA-3sxUc9pmmg6UrFvT7Pwoq-/view?usp=share_link


## Introduction
Movie search engines can handle many variations based on actor/director names, locations, time periods etc. However, not much support exists for looking up the semantic description of a scene without any of these details. In this project, we explore methods to create a semantic search engine that, given a natural-language 'tip of the tongue' user query describing a scene from a movie, returns the top-k movies that the query may be describing scenes from.

![image](https://user-images.githubusercontent.com/40300910/209452114-4fa830c4-4c77-4b78-a31a-fd7e5e042a03.png)

## Method

### Data

- Top-grossing data: Wikipedia plot sections scraped from Wikipedia list of highest grossing films]([https://en.wikipedia.org/wiki/List_of_highest-grossing_films)
Test queries: paraphrasing individual plot sentences and paragraphs

- TOMT data: Top 10 movies with the longest queries from 'I Remember This Movie' forum (source)[https://github.com/microsoft/Tip-of-the-Tongue-Known-Item-Retrieval-Dataset-for-Movie-Identification]

- Augmentation: (Parrot)[] and (Pegasus)[]

### Semantic Similarity
- Embedding methods
  - TF-IDF: unigram and 2208 dim embeddings
  - BERT+Cosine: 768-dim embeddings, summed last 4 layers
  - BERTScore: F-1 scores

- Similarity as Classification: RoBERTa
  - Similarity can be reframed as a binary classification problem (“Is sentence 1 similar to sentence 2?”)
  - Fine-tuned RoBERTa base for sentence pair classification
  - Created pairwise dataset through manual annotation and weak supervision
  - 80:20 train/test split over 280 pairs, 10 epochs, AdamW optimizer
  - 68.57% accuracy over test split 

## Results 
![image](https://user-images.githubusercontent.com/40300910/209452102-77a5b5a0-5643-4524-8485-84f2e392a508.png)

- Paraphrasing may not generate queries representative of typical end users, due to proper nouns in film media ('Bifrost', 'Odin' etc.)
- The classification approach is also biased towards movies with fewer scenes and multiple similar scenes as it returns movies with highest percentage of matched scenes. This emulates a higher recall scenario, hence it performs comparably to other approaches on top-3 accuracy as opposed to top-1.
