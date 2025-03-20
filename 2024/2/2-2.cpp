#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int is_safe(vector<int> report, int start, int end, int skip);
int is_safe_dampened(vector<int> report);
int main() {
    ifstream in("input.txt");
    vector<vector<int> > nums;
    int safe = 0;

    string line;
    while (getline(in, line)) {
        stringstream ss(line);
        vector<int> report;
        int n;
        while (ss >> n) report.push_back(n);
        nums.push_back(report);
    }

    for (int i = 0; i < nums.size(); i++) {
        if (is_safe_dampened(nums[i])) {
            safe++;
        }
    }

    cout << safe << endl;
}

int is_safe(vector<int> report, int start, int end, int skip) {
    int x = report[start];
    if (skip == start + 1) {
        start++;
    }
    int y = report[start + 1];
    int dir;
    if (y > x) {
        dir = 1;
    } else if (y < x) {
        dir = -1;
    } else {
        return 0;
    }

    int diff;
    for (int i = start + 2; i < end; i++) {
        if (i == skip) continue;
        diff = dir * (y - x);
        if (diff < 1 || diff > 3) {
            return 0;
        }
        x = y;
        y = report[i];
    }

    diff = dir * (y - x);
    if (diff < 1 || diff > 3) {
        return 0;
    }
    return 1;
}

int is_safe_dampened(vector<int> report) {
    if (is_safe(report, 0, report.size(), -1) ||
        is_safe(report, 1, report.size(), -1) ||
        is_safe(report, 0, report.size() - 1, -1)) {
        return 1;
    }

    for (int i = 1; i < report.size(); i++) {
        if (is_safe(report, 0, report.size(), i)) {
            return 1;
        }
    }

    return 0;
}