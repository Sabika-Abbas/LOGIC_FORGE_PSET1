# Input:  log = "ADOBECODEBANC", pattern = "ABC"
# Output: "BANC"

from collections import Counter
def pattern_detection(log, pattern):
    window_freq=Counter()
    pattern_freq=Counter(pattern)
    left=0
    count=0
    window=""
    required_len=len(pattern)
    min_length=float("inf")

    for right in range(len(log)):
        char=log[right]
        window_freq[char]+=1

        if char in pattern_freq and window_freq[char]==pattern_freq[char]:
            count+=1
        
        while left<=right and count==required_len:
            current_length=right-left+1
            if current_length<min_length:
                min_length=current_length
                window=log[left:right+1]

            left_char=log[left]
            window_freq[left_char]-=1
            if left_char in pattern_freq and window_freq[left_char]<pattern_freq[left_char]:
                count-=1
            left+=1
    return window
        
   

print(pattern_detection("abdehn", "deh"))

