#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main() {
    ifstream in("input.txt");
    string line;
    int safe = 0;
    while (getline(in, line)) {
        stringstream ss(line);
        int dir;
        int x, y;
        bool isSafe = true;
        ss >> x >> y;
        if (y > x) {
            dir = 1;
        } else if (y < x) {
            dir = -1;
        } else {
            continue;
        }
        while (true) {
            int diff = dir * (y - x);
            if (diff < 1 || diff > 3) {
                isSafe = false;
                break;
            }
            x = y;
            if (!(ss >> y)) {
                break;
            }
        }

        if (isSafe) {
            cout << line << endl;
            safe++;
        }
    }

    cout << safe << endl;
}