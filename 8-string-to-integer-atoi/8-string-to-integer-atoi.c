
typedef long long ll;
#define MAX __INT_MAX__
#define MIN -MAX - 1

int myAtoi(char * s){

    int sign = 1;
    ll ret = 0;
    while (*s == ' ') s++;
    if (*s == '-' || *s == '+') sign *= -(*(s++) - 44);
    while (*s >= '0' && *s <= '9') {
        ret = ret * 10;
        ret += *(s++) - '0';
        if (ret * sign > MAX) return MAX;
        if (ret * sign < MIN) return MIN;
    }
    return ret * sign;
}