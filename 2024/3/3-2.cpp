#include <iostream>
#include <fstream>
#include <regex>
using namespace std;

int main() {
    ifstream f("input.txt");
    string line;
    string l;
    while (getline(f, l)) {
        line += " " + l;
    }

    regex dont("don't\\(\\).*?do\\(\\)");
    line = regex_replace(line, dont, "");
    int first_dont = line.find("don't()");
    line = line.substr(0, first_dont == string::npos ? line.size() : first_dont);
    
    int sum = 0;
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