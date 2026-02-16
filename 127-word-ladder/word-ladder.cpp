class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        if (!wordSet.count(endWord)) return 0;
        
        queue<string> q;
        q.push(beginWord);
        
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                if (word == endWord) return level;
                
                for (int j = 0; j < word.length(); j++) {
                    char original = word[j];
                    
                    for (char c = 'a'; c <= 'z'; c++) {
                        word[j] = c;
                        
                        if (wordSet.count(word)) {
                            q.push(word);
                            wordSet.erase(word);  // mark visited
                        }
                    }
                    
                    word[j] = original; // restore
                }
            }
            
            level++;
        }
        
        return 0;
    }
};
