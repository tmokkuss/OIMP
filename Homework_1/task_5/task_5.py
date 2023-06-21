anagrams = {}
result = []


def sorted_words(data):
    return ''.join(sorted(data))


def check_anagrams(data):
    for word in data:
        sorted_word = sorted_words(word)
        anagrams.setdefault(sorted_word, [])
        anagrams[sorted_word].append(word)
    for w, a in anagrams.items():
        result.append(sorted(set(a)))
    return result[::-1]


if __name__ == '__main__':
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(check_anagrams(data=words))

