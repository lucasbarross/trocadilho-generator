#!/usr/bin/env python
"""
Remove emoji from a text file and print it to stdout.
Usage
-----
    python remove-emoji.py input.txt > output.txt
"""
import re
import sys

# https://stackoverflow.com/a/49146722/330558
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def is_a_question(string):
    expression = r".+\?.+"
    return bool(re.match(expression, string))

if __name__ == '__main__':

    parsed_lines = []
    with open("jokes.txt") as file:
        for line in file:
            if(is_a_question(line)):
                parsed_lines.append(remove_emoji(line))
    
    cleaned_lines = set(parsed_lines)

    with open("cleaned_jokes.txt", 'r+') as file:
        for line in cleaned_lines:
            file.write(str(line))