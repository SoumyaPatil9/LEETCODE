class Spreadsheet {
private:
    vector<vector<int>> grid;
    int rows;

    // Helper to get value from either number or cell
    int getOperandValue(string s) {
        // If first char is letter → cell reference
        if (isalpha(s[0])) {
            int col = s[0] - 'A';
            int row = stoi(s.substr(1)) - 1;
            return grid[row][col];
        }
        // Otherwise it's a number
        return stoi(s);
    }

public:
    Spreadsheet(int rows) {
        this->rows = rows;
        grid = vector<vector<int>>(rows, vector<int>(26, 0));
    }

    void setCell(string cell, int value) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;
        grid[row][col] = value;
    }

    void resetCell(string cell) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;
        grid[row][col] = 0;
    }

    int getValue(string formula) {
        // Remove '='
        formula = formula.substr(1);

        int plusPos = formula.find('+');

        string left = formula.substr(0, plusPos);
        string right = formula.substr(plusPos + 1);

        return getOperandValue(left) + getOperandValue(right);
    }
};
