class Solution {
public:
    vector<vector<int>> result;
    vector<int> current;
    
    void backtrack(vector<int>& candidates, int target, int start) {
        if (target == 0) {
            result.push_back(current);
            return;
        }
        
        if (target < 0) return;
        
        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] > target) break;  // pruning
            
            current.push_back(candidates[i]);
            
            // i (not i+1) because we can reuse same number
            backtrack(candidates, target - candidates[i], i);
            
            current.pop_back();  // backtrack
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, target, 0);
        return result;
    }
};
