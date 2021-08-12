class Solution {
    public int[][] merge(int[][] it) {
        List<int[]> s = new ArrayList<>();
        for (int i=0;i<it.length;i++) {
            s.add(it[i]);
        }
        
        s.sort(Comparator.comparing(a -> a[0]));
        LinkedList<int[]> res = new LinkedList<>();
        for (int i=0;i<it.length;i++) {
            if (!res.isEmpty() && s.get(i)[0] <= res.getLast()[1]){
                int[] a = res.removeLast();
                System.out.println(a[0]+" "+a[1]);
                a[1] = Math.max(a[1], s.get(i)[1]);
                
                res.addLast(a);
            }else {
                res.addLast(s.get(i));
            }
        }
        int[][] r = new int[res.size()][2];
        for (int i=0;i<res.size(); i++) {
            r[i] = res.get(i);
        }
        return r;
        
    }
}