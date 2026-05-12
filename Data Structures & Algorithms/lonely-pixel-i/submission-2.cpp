class Solution {
public:
    int findLonelyPixel(vector<vector<char>>& picture) {        
        int ROWS = picture.size();
        int COLS = picture[0].size();

        // Precalc 'B' pixel count in rows and cols
        vector<int> row_count(ROWS, 0);
        vector<int> col_count(COLS, 0);

        for (int r = 0; r < ROWS; ++r){
            for (int c = 0; c < COLS; ++c){
                if (picture[r][c] == 'B'){
                    row_count[r]++;
                    col_count[c]++;
                }
            }
        }

        // Find the lonely pixels
        int result = 0;
        for (int r = 0; r < ROWS; ++r) {
            if (row_count[r] != 1) {
                continue;
            }
            for (int c = 0; c < COLS; ++c) {
                if (picture[r][c] == 'B' && col_count[c] == 1) {
                    result++;
                }
            }
        }

        return result;
    }
};
