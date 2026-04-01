class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # defaultdict with key as the set(): list of words

        count_words = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            
            for c in word:
                char_count[ord(c) - ord('a')] += 1
            
            count_words[tuple(char_count)].append(word)

        return list(count_words.values())