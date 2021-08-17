class Solution {
    public int characterReplacement(String s, int k) {
        char[] ss = s.toCharArray();
        int[] map = new int[256];
        int max = -9, left=0, right;
        
        for (right=1;right<ss.length+1;right++) {
            char ch = ss[right - 1];
            
            map[ch]++;
            max = max < map[ch] ? map[ch] : max;
            
            
            if (right - left - max > k) map[ss[left++]]--;
        }
        
        return right - left - 1;
    }
}