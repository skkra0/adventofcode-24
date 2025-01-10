#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    vector<string> lines;
    int x, y;
    int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int dir = 0;

    ifstream in("input.txt");
    string line;
    int ct = 0;
    while (getline(in, line)) {
        if (line.find('^') != string::npos) {
            x = line.find('^');
            y = ct;
            line[x] = 'X';
        }
        lines.push_back(line);
        ct++;
    }
    
    int steps = 1;
    while (true) {
        int new_y = y + directions[dir][0];
        int new_x = x + directions[dir][1];
        if (new_y < 0 || new_y >= lines.size() || new_x < 0 || new_x >= lines[0].size()) {
            break;
        }

        if (lines[new_y][new_x] == '#') {
            dir = (dir + 1) % (sizeof(directions) / sizeof(directions[0]));
            continue;
        }

        if (lines[new_y][new_x] != 'X') {
            lines[new_y][new_x] = 'X';
            steps++;
        }
        
        y = new_y;
        x = new_x;
    }

    cout << steps << endl;
}