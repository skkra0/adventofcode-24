#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int count_xmas(int i, int j);
bool has_next_char(int i, int j, int dir, char c);

vector<string> lines;
int main() {
    ifstream in("input.txt");
    string line;
    while (getline(in, line)) {
        lines.push_back(line);
    }

    int total = 0;

    for (int i = 0; i < lines.size(); i++) {
        for (int j = 0; j < lines[i].size(); j++) {
            if (lines[i][j] == 'X') total += count_xmas(i, j);
        }
    }
    cout << total << endl;
}

int count_xmas(int i, int j) {
    int count = 0;
    for (int dir = 0; dir < 8; dir++) {
        if (has_next_char(i, j, dir, 'X')) count++;
    }
    return count;
}

bool has_next_char(int i, int j, int dir, char c) {
    if (lines[i][j] != c) {
        return false;
    }
    if (c == 'S') return true;
    int next_i = i;
    int next_j = j;
    switch (dir) {
        case 0:
            next_j++;
            break;
        case 1:
            next_i++;
            next_j++;
            break;
        case 2:
            next_i++;
            break;
        case 3:
            next_i++;
            next_j--;
            break;
        case 4:
            next_j--;
            break;
        case 5:
            next_i--;
            next_j--;
            break;
        case 6:
            next_i--;
            break;
        case 7:
            next_i--;
            next_j++;
            break;
    }

    if (next_i < 0 || next_i >= lines.size() || next_j < 0 || next_j >= lines[next_i].size()) return false;
    
    switch (c) {
        case 'X':
            return has_next_char(next_i, next_j, dir, 'M');
        case 'M':
            return has_next_char(next_i, next_j, dir, 'A');
        case 'A':
            return has_next_char(next_i, next_j, dir, 'S');
        default:
            return false;
    }
}