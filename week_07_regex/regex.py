"""Read a text file and attempt to print all names found."""

# just mucking about, a couple of input patterns, and then a second pass
# to remove patterns that matched stopwords. would love to take time to
# find better algorithm. would be interesting to try matching against
# dictionaries or lists of common names, though what do you do for names
# that are common words? anyhow.

import re
import sys

include_pattern = None
exclude_pattern = None

def build_patterns():
    build_include()
    build_exclude()

def build_include():
    """Initialize patterns."""
    global include_pattern
    patterns = []

    # building blocks
    name = r'[A-Z][a-z]+'
    honorific = r'\.|'.join(['Mr', 'Ms', 'Mrs', 'Dr'])

    # first name, last name
    patterns.append(f'(?:{name} {name})')
    # honorific, last name
    patterns.append(f'(?:(?:{honorific}) {name})')

    include_pattern = re.compile('|'.join(patterns))

def build_exclude():
    """Initialize stop words."""
    global exclude_pattern
    patterns = []

    #building blocks
    articles = r'|'.join([r'\bThe\b', '\bA\b'])
    
    patterns.append(f'(?:{articles})')
    
    exclude_pattern = re.compile('|'.join(patterns))

def find_names(s):
    """Return a set of all names in a string."""
    found = set(m.group() for m in include_pattern.finditer(s))
    found = (name for name in found if not exclude_pattern.match(name))
    return found

def main(infile):
    """Read from infile, search from names, and print them."""
    build_patterns()
    names = set()
    with open(infile) as fh:
        for line in fh:
            names.update(find_names(line))
    print('\n'.join(sorted(names)))


if __name__ == '__main__':
    main(sys.argv[1])
