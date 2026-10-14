#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        string removeStars(string s) {
            stack<char> st;
            stack<char> ans;
            for (char c : s) st.push(c);
            int starcount = 0;
            while(!st.empty()){
                if(st.top() == '*') {
                    st.pop();
                    starcount++;
                } else {
                    if(starcount > 0) {
                        st.pop();
                        starcount--;
                    } else { 
                        ans.push(st.top());
                        st.pop();
                    }
                }
            }
            string result = "";
            while(!ans.empty()){
                result += ans.top();
                ans.pop();
            }
            return result;
        }
};

// int main() {
//     // string s = "leet**cod*e";
//     string s = "erase*****";
//     cout <<Solution().removeStars(s) << '\n';
//     return 0;
// }