class PrefixTree:
     def __init__(self):
          self.parent = {}
     def add(self, word):
          tokenized = list(word)
          parent = self.parent
          for char in tokenized:
               parent[char] = parent.get(char, {}) 
               parent = parent[char]
          parent["!"] = parent.get("!", {})

     def traverse_parent(self, parent, word = '', outlist = []):
          if parent.keys() != {}:
               for key in parent:
                    next_parent = parent[key]
                    if key.strip() != "!":
                        self.traverse_parent(next_parent, word + key.strip(), outlist=outlist)
                    else:
                        outlist.append(word)
          return outlist
     def search(self, prefix):
          parent = self.parent

          word = []
          found_words = []
          for char in prefix:
               if char in parent:
                    word.append(char)
                    parent = parent[char]
               else:
                    return []
          if parent:
               searched_prefix = ''.join(word)
          return [(searched_prefix + w) for w in self.traverse_parent(parent, outlist=[])]
