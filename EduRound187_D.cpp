#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        vector<int> a(n);
        vector<int> b(m);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        for (int i = 0; i < m; i++) {
            cin >> b[i];
        }

        int MAX = n + m;

        vector<int> divCount(MAX + 1, 0);
        vector<int> cnt(MAX + 1, 0);

        // a에 각 숫자가 몇 개 있는지
        for (int x : a) {
            cnt[x]++;
        }

        for (int x = 1; x <= MAX; x++) {
            if (cnt[x] == 0)
                continue;

            for (int y = x; y <= MAX; y += x) {
                divCount[y] += cnt[x];
            }
        }

        int AliceCount = 0;
        int BobCount = 0;
        int BothCount = 0;

        for (int y : b) {
            if (divCount[y] == n) {
                AliceCount++;
            }
            else if (divCount[y] == 0) {
                BobCount++;
            }
            else {
                BothCount++;
            }
        }

        if (BothCount % 2 == 0) {
            if (AliceCount > BobCount)
                cout << "Alice\n";
            else
                cout << "Bob\n";
        }
        else {
            if (AliceCount >= BobCount)
                cout << "Alice\n";
            else
                cout << "Bob\n";
        }
    }

    return 0;
}