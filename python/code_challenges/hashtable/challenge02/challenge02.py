class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value=True):
        index = self._hash(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                return
        self.table[index].append((key, value))

    def exists(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return True
        return False

def first_repeated_word(s):
    hashtable = Hashtable()
    words = s.split()
    
    for word in words:
        word = word.strip('.,!?').lower()
        if hashtable.exists(word):
            return word
        hashtable.insert(word)
    
    return "No Repetition"

# Example usage
print(first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC."))
# Output: ASAC

print(first_repeated_word("I am learning programming at ASAC."))
# Output: No Repetition
