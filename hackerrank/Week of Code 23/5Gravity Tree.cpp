#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

map<int, int> tree;
map<int, vector<int>> pathList;

int getDist(int vertexA, int vertexB) {
    vector<int> A = pathList[vertexA];
    vector<int> B = pathList[vertexB];
    for(int i = 0; i < A.size(); i++) {
        auto it = find(B.begin(), B.end(), A[i]);
        if(it != B.end()) {
            return i + distance(B.begin(), it);
        }
    }
    return 0;
}

map<int, vector<int>> getPathList(int vertex, vector<int> path) {
    map<int, vector<int>> vertexList;
    path.insert(path.begin(), vertex);
    vertexList[vertex] = path;
    for(int i = 1; i <= tree.size(); i++) {
        if(tree[i] == vertex) {
            map<int, vector<int>> childList = getPathList(i, path);
            vertexList.insert(childList.begin(), childList.end());
        }
    }
    return vertexList;
}

int main() {
    int n;
    cin >> n;
    tree[1] = 0;
    for(int i = 2; i <= n; i++){
        int t;
        cin >> t;
        tree[i] = t;
    }
    
    vector<int> tempPath;
    tempPath.push_back(0);
    pathList = getPathList(1, tempPath);
    
    int q;
    cin >> q;
    for(int i = 0; i < q; i++){
        int u, v;
        cin >> u >> v;
        int netForce = 0;
        for(int i = 1; i <= pathList.size(); i++) {
            if(find(pathList[i].begin(), pathList[i].end(), v) != pathList[i].end()) {
                netForce += pow(getDist(i, u), 2);
            }
        }
        cout << netForce << endl;
    }
    
    return 0;
}