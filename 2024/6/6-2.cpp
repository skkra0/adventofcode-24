#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

int main() {
    vector<string> lines;
    int start_x, start_y;
    int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int dir = 0;
    set<tuple<int, int> > path;

    ifstream in("input.txt");
    string line;
    int ct = 0;
    while (getline(in, line)) {
        if (line.find('^') != string::npos) {
            start_x = line.find('^');
            start_y = ct;
        }
        lines.push_back(line);
        ct++;
    }

    int x = start_x;
    int y = start_y;
    
    while (true) {
        int new_y = y + directions[dir][0];
        int new_x = x + directions[dir][1];
        if (new_y < 0 || new_y >= lines.size() || new_x < 0 || new_x >= lines[0].size()) {
            break;
        }

        if (lines[new_y][new_x] == '#') {
            dir = (dir + 1) % 4;
            continue;
        }
        
        path.insert(make_tuple(new_x, new_y));
        y = new_y;
        x = new_x;
    }
    
    int sum = 0;

    for (const auto& obs : path) {
        int x = start_x;
        int y = start_y;
        int dir = 0;
        lines[get<1>(obs)][get<0>(obs)] = '#';
        set<tuple<int, int, int> > visited;
        while (true) {
            int new_y = y + directions[dir][0];
            int new_x = x + directions[dir][1];
            if (new_y < 0 || new_y >= lines.size() || new_x < 0 || new_x >= lines[0].size()) {
                break;
            }

            if (lines[new_y][new_x] == '#') { //} || new_x == get<0>(obs) && new_y == get<1>(obs)) {
                dir = (dir + 1) % (sizeof(directions) / sizeof(directions[0]));
                continue;
            }
            
            if (visited.find(make_tuple(new_x, new_y, dir)) != visited.end()) {
                sum++;
                break;
            } else {
                visited.insert(make_tuple(new_x, new_y, dir));
            }
            y = new_y;
            x = new_x;
        }
        lines[get<1>(obs)][get<0>(obs)] = '.';
    }

    cout << sum << endl;
}
