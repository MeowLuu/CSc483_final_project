package project;

public class edit_distance {
	public static void main(String[] args) {
		int distance = calc_edit_dist("doctors", "dcotros");
		System.out.println(distance);
	}
	
	public static int calc_edit_dist(String word1, String word2) {
		int m = word1.length();
        int n = word2.length();
        
        // Create a 2D array to store the distances
        int[][] dp = new int[m + 1][n + 1];
        
        // Initialize the first row and column
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill in the rest of the array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                }
                
                // Consider swaps
                if (i > 1 && j > 1 && word1.charAt(i - 1) == word2.charAt(j - 2) && word1.charAt(i - 2) == word2.charAt(j - 1)) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 2][j - 2] + 1);
                }
            }
        }
        
        return dp[m][n];
	}
}
