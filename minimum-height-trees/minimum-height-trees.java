class Solution {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (edges.length == 0) return new ArrayList<Integer>(){{add(0);}};
        for (int[] e: edges) {
            graph.putIfAbsent(e[0], new ArrayList<>());
            graph.putIfAbsent(e[1], new ArrayList<>());
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        ArrayList<Integer> q = new ArrayList<>();
        for (int i=0;i<n;i++) {
            if (graph.containsKey(i) && graph.get(i).size() == 1) q.add(i);
        }

        ArrayList<Integer> nq;
        while (n > 2) {
            n -= q.size();
            System.out.println(q.size());
            nq = new ArrayList<>();
            for (int v: q) {
                int u = graph.get(v).remove(0);
                graph.get(u).remove(new Integer(v));
                if (graph.get(u).size() == 1) nq.add(u);
            }
            q = nq;
            System.out.println(nq.size());
        }
        return q;
    }
}