#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool checkRepeated(string s, string t) {
	if (s.length() % t.length()) return false;
	for (int i = 0; i < s.length(); i += t.length()) {
		if (s.substr(i, t.length()) != t) return false;
	}
	return true;
}

int main() {
	string s;
	int m;
	cin >> s >> m;
	int l = s.length();
	for (int n = s.length() / 2; n; n--) {
		if (checkRepeated(s, s.substr(0, n))) l = n;
	}
	int mod = pow(10, 9) + 7;
	cout << m / l % mod;
	return 0;
}