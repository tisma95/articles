# Get started Sentence Similarities

1. Install the conda
2. Create the env with `conda create -n similarity python=3.10`
3. Activate the env with `conda activate similarity`
4. Install the milvus package with `pip install -r requirements.txt`
5. Install spacy languages: `python -m spacy download en_core_web_lg` and `python -m spacy download fr_core_news_lg`

> After install new package update the requirements with `conda list -e > conda-requirements.txt`
> After install new package with pip command update the requirement with `pip install -r pip-requirements.txt`

> Charger le modèle relatif au français avec `python -m spacy download fr_core_news_lg` pour des modèles moins large prendre **fr_core_news_md** ou **fr_core_news_sm** <br>
> Pour l'anglais prendre **en_core_web_sm**, **en_core_web_md** et **en_core_web_lg**.

# Code explanation

The main goal is to ask two sentences to the user and display the percent of similarity between both sentences.

For two sentences $A$ and $B$ use the formula:

$cos(\alpha) = \frac{\sum_{i=1}^{n}A_{i}B{i}}{\sqrt{\sum_{i=1}^{n}A_{i}^{2}} * \sqrt{\sum_{i=1}^{n}B_{i}^{2}}}$

- `native_similarity.py`: Analyse of similarity with Python native code
- `spacy_similarity.py`: Analyse of similarity with Spacy
- `nltk_similarity.py`: Analyse of similarity with NLTK
- `spacy_internal_similarity.py`: Use the internal similarity of spacy by using **similarity** of spacy
