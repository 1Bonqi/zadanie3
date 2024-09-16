from typing import List


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for i in punctuation:
                        line = line.replace(i, '')
                    line = line.replace('-', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        _dict = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                _dict[key] = value.index(word.lower()) + 1
        return _dict

    def count(self, word):
        counts = {}
        for key, value in self.get_all_words().items():
            counts[key] = value.count(word.lower())

        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
