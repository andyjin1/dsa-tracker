class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash table with key of array frequency: list of word 
        # iterate through the words in strs and then count the occurences
        # if we find the same occurence in the hash table, we append the currrent word to the list
        # we can return a list object of dictionary values in the end

        freq_words = defaultdict(list)

        for word in strs:
            count_word = [0] * 26
            for c in word:
                count_word[ord(c) - ord('a')] += 1 
            freq_words[tuple(count_word)].append(word)

        return list(freq_words.values())