#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
using namespace std;

unordered_map<int, unordered_set<int> > before;
bool is_before(int a, int b);

int main() {

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
            }
            update.push_back(y);
            x = y;
            iss.ignore();
        }
        if (success) continue;
        
        sort(update.begin(), update.end(), is_before);

        sum += update[update.size() / 2];
    }
    
    cout << sum << endl;
}

bool is_before(int a, int b) {
    auto it = before.find(a);
    return it != before.end() && it->second.find(b) != it->second.end();
}