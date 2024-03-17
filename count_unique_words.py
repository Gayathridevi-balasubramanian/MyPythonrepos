import re
import collections

def count_words(path):
    with open(path,'r',encoding='utf-8') as file:
        all_words = re.findall(r"[1-9a-zA-Z-']+",file.read())
        all_words = [words.upper() for words in all_words]
        print(f'\n Total words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\n Top 20 words')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t\t{word[1]}')

count_words('gayathri.txt')