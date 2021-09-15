# Week 01
## Python practice

Since I'm pretty comfortable with lists and dictionaries and all the similar
goodnesses of vanilla python, I wanted to use this opportunity to practice with
some of the packages that I'll need for my Machine Learning class, which
relates to Ethics because I'm trying to take a focus on fairness and ethics in
machine learning.

These programs aren't much to speak of, mostly just practicing the syntax for
numpy and pandas.

### Requirements

matplotlib
numpy
pandas

#### covidfetch.py

Practice using urllib to fetch a file via HTTPS and perform a naive csv parse
to create a row of dictionaries. (Simply using a .split(',') approach, with no
support for quoted strings.)

#### covidpandas.py

Fetches the same dataset, put parses it using pandas, then uses some pandas
features to group and arrange the dataset, plot growth over time, and perform a
(meaningless) polynomial regression of new cases vs time.

#### irislearn.py

Fetches a classic machine learning dataset known as "the Iris dataset," that
categorizes three types of irises by 4 features. Uses a very naive 'K nearest
neigbors' algorithm to attempt to guess an iris based on similarity to data in
the training set. I didn't have time to fully implement the algorithm or error
analysis. Again, mostly in an exploration in how pandas and numpy are used to
work with datasets in the manner required for machine learning.
