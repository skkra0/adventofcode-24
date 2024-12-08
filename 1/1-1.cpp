#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream in("input.txt");

    vector<int> list1;
    vector<int> list2;
    string line;
    string word;
    while (getline(in, line)) {
        int a, b;
        sscanf(line.c_str(), "%d %d", &a, &b);
        list1.push_back(a);
        list2.push_back(b);
    }

    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    int sum = 0;
    for (int i = 0; i < list1.size(); i++) {
        sum += abs(list1[i] - list2[i]);
    }
    cout << sum << endl;
}