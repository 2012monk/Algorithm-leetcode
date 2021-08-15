class Solution {
    public int find(int[] a, int lo, int hi, int t) {
        int l=lo, r=hi;
        while (l <= r && l < hi) {
            int mid = (l + r) / 2;
            if (a[mid] == t){
                return mid;
            }
            if (a[mid] < t) {
                l = mid + 1;
            }
            else{
                r = mid - 1 ;
            }
            
        }
        return l;
    }
    public int search(int[] nums, int target) {
        int l = find(nums, 0, nums.length-1, target);
        if (nums[l] == target) return l;
        return -1;
    }
}