# Bias in Natural Language Processing
## Morgan Wajda-Levie, December 2021

### results2html.py
#### About

In addition to a brief presentation, I've attached a visualization
script for an algorithm that attempts to measure _differential bias_ in
the training corpora of word embeddings.

Using the Word Association Embedding Test (Caliskan et al, 2016), the
algorithm attempts to estimate the amount that each document in a
training corpus will impact the final WEAT effect size. The theory is,
by identifying documents with the greatest impact on the final bias of a
word embedding, those documents can be witheld from training and the
overall bias reduced (Brunet et al, 2019.)

I have written this visualization script to look at these most impactful
documents so that we can analyze those documents and learn more about
what drives bias in word embeddings.

Parts of this script were written for a project in the Machine Learning
Seminar with Professor Anita Raja, but most of the output formatting was
written for CS Ethics. My partner in the Machine Learning Seminar is
Rebecca Kleinbart.

#### Usage

I have included a sample HTML output. To run the script yourself, you
will need results and a language corpus not included in this repo. For
the time being, I've made some available elsewhere.

1. Run **setup.sh** to download additional files.
2. Install pandas, using a virtual environment if you prefer.
3. Run the script: **python3 results2html simplewiki_results.csv
   simplewikiselects.txt**. Running the script without arguments will
   print additional usage.

The WEAT test for these results is comparing bias between men and women
with regards to science and the arts. The training corpus was taken from
Simple Wikipedia in 2017. This test is discussed at greater length in
Brunet et al's paper, "Understanding the Origins of Bias in
Word Embeddings."

#### What's Next?

Given more time, there are a few things I'd love to do with this code:

- Pull metadata formatting out into top-level corpus-hooks that are
  linked to the corpus text file. This way, new corpora with their own
  metadata formats can be easily added.
- Generally improve flow of information and organization of code,
  possibly reorganizing the way that selects are stored.
- See if it is possible to pull select articles from the original
  untokenized Wikimedia corpus and include access to those, possibly
  using a javascript window.
- Include links to the untokenized New York Times articles.
- Use a more standard HTML generation technique, possibly using
  templates.
- Calculate some overall statistics and possibly include plots.

#### References

- Understanding the Origins of Bias in Word Embeddings. Brunet,
  Alkalay-Houlihan, Anderson, Zemel.
- Semantics derived automatically from language corpora contain
  human-like biases. Caliskan, Bryson, Narayanan.

