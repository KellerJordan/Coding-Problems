#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    long total = a + b + c + d + e;
    long min = 5 * pow(10, 9);
    long max;
    long sums[5] = {total - a, total - b, total - c, total - d, total - e};
    for(int i = 0; i < 5; i++) {
        long sum = sums[i];
        if(sum < min) min = sum;
        if(sum > max) max = sum;
    }
    cout << min << " " << max;
    return 0;
}
