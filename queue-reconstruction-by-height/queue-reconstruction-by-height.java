class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b) {
                return a[0] == b[0] ? a[1]-b[1]: -a[0]+b[0];
            }
        });
        LinkedList<int[]> li = new LinkedList<>();
        for (int[] p:people) {
            li.add(p[1], p);
        }
        return li.toArray(new int[people.length][]);
    }
}