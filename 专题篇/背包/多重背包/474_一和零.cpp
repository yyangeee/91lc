#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include<numeric>
using namespace std;

class Solution {
public:
    vector<int> getZerosOnes(string& str) {
        vector<int> zerosOnes(2);
        int length = str.length();
        for (int i = 0; i < length; i++) {
            zerosOnes[str[i] - '0']++;
        }
        return zerosOnes;
    }

    int findMaxForm(vector<string>& strs, int m, int n) {
        int length = strs.size();
        vector< vector< vector<int> > > dp (length+1, vector< vector<int> >(m+1, vector<int>(n+1 ,0)));
        for (int i = 1; i <= length ; i++ ) {
            vector<int> zerosOnes = getZerosOnes(strs[i-1]);
            int zero = zerosOnes[0];
            int one = zerosOnes[1];
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    if (j >= zero && k >= one) {
                        dp[i][j][k]= max(dp[i-1][j][k], dp[i-1][j-zero][k-one] + 1);
                    } else {
                        dp[i][j][k] = dp[i-1][j][k];
                    }
                }
            }
        }
        return dp[length][m][n] ;
    }

        int findMaxForm2(vector<string>& strs, int m, int n) {
        int length = strs.size();
        vector< vector< int > > dp (m+1, vector<int>(n+1 ,0));
        for (int i = 1; i <= length ; i++ ) {
            vector<int> zerosOnes = getZerosOnes(strs[i-1]);
            int zero = zerosOnes[0];
            int one = zerosOnes[1];
            for (int j = m; j > 0; j--) {
                for (int k = n; k > 0 ; k--) {
                    if (j >= zero && k >= one) {
                        dp[j][k]= max(dp[j][k], dp[j-zero][k-one] + 1);
                    } else {
                        dp[j][k] = dp[j][k];
                    }
                }
            }
        }
        return dp[m][n] ;
    }
};

int main() {
    string a[5] = {"10", "0001", "111001", "1", "0"};
    std::vector<string> strs(a,a+5);
    int result;
    result = Solution().findMaxForm2(strs, 5, 3);    
    cout << result << endl;
    return 0;
}