class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            # Anagrams have the same letters when sorted
            key = "".join(sorted(word))

            # If this is a new group, create its list
            if key not in groups:
                groups[key] = []

            # Add the word to the group with the matching sorted letters
            groups[key].append(word)

        # Return the groups without their keys
        return list(groups.values())