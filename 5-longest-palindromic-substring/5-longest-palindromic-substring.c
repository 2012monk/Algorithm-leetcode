

int dp[1001][1001];

int f(int i, int j, char *s) {
    if (dp[i][j] != -1) return dp[i][j];
    if (j - i == 1) return dp[i][j] = s[i] == s[j];
    return dp[i][j] = (s[i] == s[j]) & f(i + 1, j - 1, s);
}
char * longestPalindrome(char * s){
    int n = strlen(s);
    for (int i =0; i < n; i++) {
        for (int j = 0; j < n; j++) dp[i][j] = -1;
        dp[i][i] = 1;
    }

    int start = 0, len = 1;
    for (int i = 0; i < n - 1; i++) {
        for (int j = n - 1; j >= i; j--) {
            if (j - i + 1 < len) break;
            if (f(i, j, s)) {
                len = j - i + 1;
                start = i;
            }
        }
    }
    printf("%d %d\n", start, len);
    s = s + start;
    s[len] = 0;
    return s;
}
