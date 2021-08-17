class Solution {
    public int characterReplacement(String s, int k) {
        char[] ss = s.toCharArray();
        int[] map = new int[256];
        int max = -9, left=0, right;
        
        for (right=1;right<ss.length+1;right++) {
            map[ss[right - 1]]++;
            
            if (max < map[ss[right - 1]]) {
                max = map[ss[right - 1]];
            }
            
            if (right - left - max > k) {
                map[ss[left++]]--;
            }
        }
        return right - left - 1;
    }
}