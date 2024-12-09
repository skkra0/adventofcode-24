#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream in("input.txt");

    int sum = 0;

    string line;
    string l;
    while (getline(in, l)) {
        line += " " + l;
    }

    int start = 0;
    while (true) {
        int num_start = line.find("mul(", start);
        if (num_start == string::npos) break;
        num_start += 4;

        int num_end = line.find(",", num_start);
        int a;
        int b;
        size_t pos;
        try {
            a = stoi(line.substr(num_start, num_end - num_start), &pos);
            if (pos != num_end - num_start) {
                start = num_start;
                continue;
            }
        } catch (invalid_argument e) {
            start = num_start;
            continue;
        }

        num_start = num_end + 1;
        num_end = line.find(")", num_start);

        try {
            b = stoi(line.substr(num_start, num_end - num_start), &pos);
            if (pos != num_end - num_start) {
                start = num_start;
                continue;
            }
        } catch (invalid_argument e) {
            start = num_start;
            continue;
        }

        sum += a * b;
        start = num_end + 1;
    }
    cout << sum << endl;
}