
class Solution {
public:

    int numDecodings(string s) {
        /// 11106 
        // 1110 6 --> 11 10 6 --> 1 1 10 6 --> 11 10 6
        // 111 06 -> X

        int x = 0; 
        int y = 0;
        if(s[0] != '0') {
            x = 1;
        }

        for(int i = 1; i < s.size(); i++) {
            int newX = 0; 
            int newY = 0; 
            string newAdd = s.substr(i - 1, 2); 
            if (s[i] != '0') newX = x + y; 
            if (newAdd <= "26") newY = x; 
            x = newX; 
            y = newY;
        }


        return x + y; 
        
    }
};