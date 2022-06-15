
int n,m;
int d[2001][2001];
char *s, *p;
bool f(int i, int j) {
    int *r = &d[i][j];
    if (*r != -1) return *r;
    *r = 0;
    if (j == m) return *r = i == n;
    if (i == n) return *r = p[j] == '*' && f(i, j + 1);
    if (p[j] == '*') *r = f(i + 1, j) | f(i, j + 1);
    if (s[i] == p[j] || p[j] == '?') *r = f(i + 1, j + 1);
    return *r;
}
bool isMatch(char * ss, char * pp){
    s = ss;
    p = pp;
    n = strlen(ss);
    m = strlen(pp);
    memset(d, -1, 2001 * 2001 * sizeof(int));
    return f(0, 0);
}