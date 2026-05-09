class Solution {
public:
    bool confusingNumber(int n) {
        map<int, int> invert_map = {{0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}};
        int rotated_num = 0;
        int n_copy = n;

        while (n_copy > 0) {
            int result = n_copy % 10;
            if (invert_map.find(result) == invert_map.end()) {
                return false;
            }

            rotated_num = rotated_num * 10 + invert_map[result];
            n_copy /= 10;
        }

        return rotated_num != n;
    }
};
