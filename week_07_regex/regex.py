"""Read a text file and attempt to print all names found."""

# just mucking about, a couple of input patterns, and then a second pass
# to remove patterns that matched stopwords. would love to take time to
# find better algorithm. would be interesting to try matching against
# dictionaries or lists of common names, though what do you do for names
# that are common words? anyhow.

import argparse
import re
import sys

include_pattern = None
exclude_pattern = None

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help=('file to search for names'))
    return vars(parser.parse_args())

def build_patterns():
    build_include()
    build_exclude()

def build_include():
    """Initialize patterns."""
    global include_pattern
    patterns = []

    # building blocks
    name = r'[A-Z][a-z]+'
    honorific = r'\.|'.join(['Mr', 'Ms', 'Mrs', 'Dr', 'Mx'])

    # first name, last name
    patterns.append(r'(?:{} {})'.format(name, name))
    # honorific, last name
    patterns.append(r'(?:(?:{}) {})'.format(honorific, name))

    include_pattern = re.compile('|'.join(patterns))

def build_exclude():
    """Initialize stop words."""
    global exclude_pattern
    patterns = []

    # stop-words
    stopwords = ['the', 'a', 'on', 'in', 'under']
    stopwords = ['\b{}\b'.format(''.join('[{}{}]'.format(letter.upper(),
                                                         letter.lower())
                                         for letter in word)) for word
                 in stopwords]
    patterns.append('(?:{})'.format('|'.join(stopwords)))
    
    exclude_pattern = re.compile('|'.join(patterns))
    print(exclude_pattern)

def find_names(s):
    """Return a set of all names in a string."""
    found = set(m.group() for m in include_pattern.finditer(s))
    found = (name for name in found if not exclude_pattern.match(name))
    return found


def find_names_2(s):
    """Return a set of all names in a string."""

    # Replace stop-words with a special character
    # This keeps patterns from matching across removed stopwords
    s = re.sub(exclude_pattern, '%%%', s)
    print(s)

    # Run super-pattern!
    found = set(m.group() for m in include_pattern.finditer(s))
    return found

def main(input_file):
    """Read from infile, search from names, and print them."""
    build_patterns()
    names = set()
    with open(input_file) as fh:
        for line in fh:
            names.update(find_names_2(line))
    print('\n'.join(sorted(names)))


if __name__ == '__main__':
    main(**parse_args())
