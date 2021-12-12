// vector<int> dp(100000, -1);

// class Solution {
// public:
//     int minNumberOfSemesters(int N, vector<vector<int>>& dependencies) {
//         vector<vector<int>> e(N+1);
//         vector<int> deg(N+1);  // in deg
//         for (vector<int> r: dependencies) {
//             e[r[0]].push_back(r[1]);
//             deg[r[1]]++;
//         }

//         queue<int> q;
//         for (int i = 1; i <= N; ++i) {
//             if (deg[i] == 0)q.push(i);
//         }

//         int ans = 0;
//         int num = 0;
//         while (q.size()) {
//             ans++;
//             num += q.size();
//             int size = q.size();
//             while (size--) {
//                 int x = q.front();
//                 q.pop();
//                 for (int y: e[x]) {
//                     if (--deg[y] == 0) q.push(y);
//                 }
//             }
//         }
//         if (num != N) return -1;
//         return ans;
//     }
// };

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int m = 10;
    int n = 3;
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    vector<vector<int>> lookup(m, vector<int>(n,1));
    vector<bool> ok(vector<bool>(n,false));

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}
