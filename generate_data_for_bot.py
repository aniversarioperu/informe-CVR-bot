import json
import re
import sys

import nltk.data


if len(sys.argv) < 2:
    print("\nError, enter txt file to extract sentences for twitter.")
    sys.exit(1)

input_file = sys.argv[1].strip()
with open(input_file, "r") as handle:
    text = handle.readlines()

cleaned_text = []
for i in text:
    line = i.strip()
    stripped_line = ' '.join(line.splitlines())
    stripped_line_without_extra_spaces = re.sub('\s+', ' ', stripped_line.strip())
    if not re.search('^[0-9]+$', stripped_line_without_extra_spaces):
        if len(stripped_line_without_extra_spaces) > 0:
            cleaned_text.append(stripped_line_without_extra_spaces)

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
sentences = tokenizer.tokenize(' '.join(cleaned_text))

sentences_for_twitter = [i for i in sentences if 23 < len(i) < 106]

sentences_for_twitter_with_index = []
for idx, i in enumerate(sentences_for_twitter):
    sentences_for_twitter_with_index.append({'index': idx,
                                             'sentence': 'InformeCVR: {0} http://bit.ly/1VOf0hs'.format(i)})

print(json.dumps(sentences_for_twitter_with_index))

