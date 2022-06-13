

int myAtoi(char * s){

    int sign = 1;
    long long ret = 0;
    int max = __INT_MAX__;
    int min = -max - 1;
    while (*s == ' ') s++;
    if (*s == '-' || *s == '+') sign *= -(*(s++) - 44);
    printf("%d",sign);
    while (*s >= '0' && *s <= '9') {
        ret = ret * 10;
        ret += *(s++) - '0';
        if (ret * sign > max) return max;
        if (ret * sign < min) return min;
    }
    ret *= sign;
    return ret;
}