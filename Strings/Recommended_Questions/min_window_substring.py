#Minimum Window Substring
#Leet Code Link: https://leetcode.com/problems/minimum-window-substring/description/

'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

def minWindow(s: str, t: str) -> str:
        #Getting Length of the given inputs
        m,n = len(s),len(t)

        # Count of the character in t which should be present in s substring
        counter = n

        # start and end for sliding window and head to get hold of the latest start pointer which satisfy the criteria of counter == 0
        start,end,head = 0,0,0
        
        # To Track the Minimum Length of the SubString which satify the criteria
        minLength = m+1

        # hash map to track the occurances of the characters in t which need to be further used while iterating s
        charMap = {}
        
        # if t length is more than s it is invalid
        if n>m: return ""

        # Creating hashmap which stores frequences of each character in t 
        for i in t:
            charMap[i] = charMap.get(i,0)+1

        # using end pointer to iterate over s here window start increasing
        while(end<m):

            # if a character from t is found in s we need to track it
            if s[end] in charMap:
                # Decrease the counter as we found the character in s and counter cannot be negative 
                # because our problem is to find "every character in t (including duplicates) should be in substring s" 
                if charMap[s[end]] > 0:
                    counter-=1
                # updating the hash map since we are using this in the window
                charMap[s[end]]-=1
            
            # increment the end to move the window
            end+=1

            #MAIN CRITERIA: When counter becomes 0 we found all the characters(including duplicates) of t in this window(end-start) substring
            while(counter == 0):
                # Deducing the length of the window
                currLen = end-start
                # If the Current Window size is less the previous window update minLength
                if currLen < minLength:
                    # Updating the minLength
                    minLength = currLen
                    # we need to store the start of last valid window since we have to return contents in the window
                    # we can't directly use 'start' because we will be updating it later to reduce the size of the window
                    head = start
                
                # While reducing the size of window there might be cases where character of t would be present in the window
                # As we are planning to move out of the start we need to add the used characters in Hash map and counter
                if s[start] in charMap:
                    # Add the characters used previously as we are moving out the window and can be used again
                    charMap[s[start]]+=1
                    # Increasing the counter as it can be used again further and counter cannot be negative 
                    # because our problem is to find "every character in t (including duplicates) should be in substring s"
                    if charMap[s[start]] > 0:
                        counter+=1
                # Increasing start pointer as we are reducing the window size
                start+=1

        # if all the characters are not found in substring of s return ""
        if minLength == m+1:
            return ""
        #return the valid substring using head and minLength
        return s[head:head+minLength]