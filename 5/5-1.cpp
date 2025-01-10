#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int main() {
    unordered_map<int, unordered_set<int> > before;

    ifstream in("input.txt");
    string line;
    while (getline(in, line)) {
        if (line.empty()) break;

        int a, b;
        sscanf(line.c_str(), "%d|%d", &a, &b);
        if (before.find(a) == before.end()) {
            before[a] = unordered_set<int>();
            before[a].insert(b);
        } else {
            before[a].insert(b);
        }
    }

    int sum = 0;
    while (getline(in, line)) {
        bool success = true;
        vector<int> update;
        int x, y;
        istringstream iss(line);
        iss >> x;
        update.push_back(x);
        iss.ignore();
        while (iss >> y) {
            if (before.find(y) != before.end() && before[y].find(x) != before[y].end()) {
                success = false;
                break;
            }
            update.push_back(y);
            x = y;
            iss.ignore();
        }
        if (!success) continue;
        sum += update[update.size() / 2];
    }
    
    cout << sum << endl;
}