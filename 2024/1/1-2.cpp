#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<int> nums;
    unordered_map<int, int> counts;
    ifstream in("input.txt");
    string line;

    while (getline(in, line)) {
        int a, b;
        sscanf(line.c_str(), "%d %d", &a, &b);
        nums.push_back(a);
        if (counts.find(b) == counts.end()) {
            counts[b] = 1;
        } else {
            counts[b]++;
        }
    }

    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        int n = nums[i];
        if (counts.find(n) != counts.end()) {
            sum += n * counts[n];
        }
    }

    cout << sum << endl;
}