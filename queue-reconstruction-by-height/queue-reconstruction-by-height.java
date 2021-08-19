class Solution {
    public int[][] reconstructQueue(int[][] people) {
        PriorityQueue<int[]> q = new PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? -a[0]+b[0]:a[1]-b[1]);
        List<int[]> li = new LinkedList<>();
        
        for (int[] p: people) q.offer(p);
        
        while (!q.isEmpty()) {
            int[] a = q.poll();
            li.add(a[1], a);
        }
        
        return li.toArray(new int[people.length][]);
    }
}