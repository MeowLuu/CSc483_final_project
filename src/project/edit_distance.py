def damerau_levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    
    # Initialize a 2D array to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill in the rest of the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            
            # Consider swaps
            if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
    
    return dp[m][n]

# Example usage
word1 = "doctors"
word2 = "dcotros"
distance = damerau_levenshtein_distance(word1, word2)
print(f"Damerau-Levenshtein distance between '{word1}' and '{word2}' is: {distance}")
