impl Solution {
    pub fn find_lonely_pixel(picture: Vec<Vec<char>>) -> i32 {
        let ROWS = picture.len();
        let COLS = picture[0].len();

        let mut row_count = vec![0; ROWS];
        let mut col_count = vec![0; COLS];

        for r in 0..ROWS {
            for c in 0..COLS {
                if picture[r][c] == 'B' {
                    row_count[r] += 1;
                    col_count[c] += 1;
                }
            }
        }

        // Find the lonely pixel
        let mut result = 0;
        for r in 0..ROWS {
            if row_count[r] == 1 {
                for c in 0..COLS {
                    if picture[r][c] == 'B' && col_count[c] == 1 {
                        result += 1;
                    }
                }
            }
        }

        result
    }
}
