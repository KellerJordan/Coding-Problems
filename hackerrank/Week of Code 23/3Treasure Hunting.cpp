#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main() {
	double x, y, a, b;
	cin >> x >> y >> a >> b;
	double k = (x * a + y * b) / (a * a + b * b);
	double n = (k * a - x) / b;
	cout << fixed << setprecision(12) << k << endl << n;
	return 0;
}