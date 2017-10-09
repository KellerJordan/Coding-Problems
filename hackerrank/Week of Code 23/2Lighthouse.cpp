#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
vector<vector<bool>> arr;

float dist(int x, int y) {
	return sqrt(pow(x, 2) + pow(y, 2));
}

int testPoint(int x, int y) {
	int maxDistance = min(min(x, y), min(n - 1 - x, n - 1 - y));
	float distance;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			distance = dist(x - i, y - j);
			if (arr[i][j] && distance <= maxDistance) maxDistance = floor(distance - .000001);
		}
	}
	return maxDistance;
}

int main() {
	cin >> n;
	arr.resize(n, vector<bool>(n, false));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char b;
			cin >> b;
			if (b == '*') arr[i][j] = true;
		}
	}

	int max = 0;
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			int size;
			size = testPoint(x, y);
			if (size > max) max = size;
		}
	}

	cout << max;

	return 0;
}