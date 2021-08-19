class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c:tasks) {
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b) {
                return a[0]-b[0];
            }
        });
        for (char c: map.keySet()) {
            int a = map.get(c);
            q.offer(new int[]{-a, (int) c});
        }
        int res = 0;
        while (true) {
            int[] v = new int[256];
            int k = 0;
            while (!q.isEmpty() && k <= n) {
                int[] a = q.poll();
                if (a[0] < 0) {
                    v[a[1]] = a[0]+1;
                }
                res++;
                k++;
            }
            for (int i=0;i<256;i++) {
                if (v[i] < 0) {
                    q.offer(new int[] {v[i], i});
                    v[i]=0;
                        
               };
            }
            if (q.isEmpty()) {
                break;
            }
            res += n - k + 1;
        }
        return res;
        
    }
}