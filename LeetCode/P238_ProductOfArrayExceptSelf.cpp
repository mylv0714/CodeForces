#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
        // left product x right product
        // time complexity: O(n), space complexity: O(1)
        vector<int> productExceptSelf(vector<int>& nums) {
            int n = nums.size();
            vector<int> ans(n,1);
            int left = 1;
            for (int i=0;i<n;i++) {
                ans[i] = left;
                left *= nums[i];

            }
            int right = 1;
            for (int i=n-1;i>=0;i--) {
                ans[i] *= right;
                right *= nums[i];
            }
            return ans;
        }
    };

// int main() {
//     vector<int> nums = {1, 2, 3, 4};
//     vector<int> result = Solution().productExceptSelf(nums);
//     for (int i = 0; i < result.size(); i++) {
//         cout << result[i] << " ";
//     }
//     cout << '\n';
// }