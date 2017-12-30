import collections
def findLongestSubSequence():
    S="abppplee"
    words=["pppppx", "ale", "applle", "bpleex", "kangaroo"]
    letter_pos=collections.defaultdict(list)
    
    for index, letter in enumerate(S):
        letter_pos[letter].append(index)
        #print(letter,"->",letter_pos[letter])
    #print(sorted(words,key= lambda word : len(word), reverse=True ))
    for word in sorted(words,key= lambda word : len(word), reverse=True ): #Important sorted in-built function using lambda and a parameter to sort with. In this case the len of string elements present
        pos=0
        possible_pos = []
        for letter in word:
            result=False
            #print(letter)
            #print(possible_pos)
            possible_pos = [p for p in letter_pos[letter] if p >= pos]
            #print(possible_pos)
            if letter not in letter_pos:
                break            
            else:
                if not possible_pos:
                    break
                pos = possible_pos[0]+1
                result=True
        if result:
            return word
                
if __name__=="__main__":
    print(findLongestSubSequence())
