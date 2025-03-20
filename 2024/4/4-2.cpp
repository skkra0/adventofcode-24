#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool has_x_mas(int i, int j);

vector<string> lines;
int main() {
    ifstream in("input.txt");
    string line;
    while (getline(in, line)) {
        lines.push_back(line);
    }

    int total = 0;
    for (int i = 1; i < lines.size() - 1; i++) {
        for (int j = 1; j < lines[i].size() - 1; j++) {
            if (lines[i][j] == 'A' && has_x_mas(i, j)) {
                total++;
            }
        }
    }
    cout << total << endl;
}

bool has_x_mas(int i, int j) {
    char ms[] = {'M', 'S'};
    bool mas_1 = false;
    bool mas_2 = false;
    for (int k = 0; k < 2; k++) {
        if (lines[i - 1][j - 1] == ms[k] && lines[i + 1][j + 1] == ms[(k + 1) % 2]) mas_1 = true;
    }
    for (int k = 0; k < 2; k++) {
        if (lines[i - 1][j + 1] == ms[k] && lines[i + 1][j - 1] == ms[(k + 1) % 2]) mas_2 = true;
    }

    return mas_1 && mas_2;
}