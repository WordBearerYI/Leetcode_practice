public void dijkstra(int p) {
        int[] d = new int[n];
        Set<Integer> set = new HashSet<>(n);
        set.add(p);
        for (int i = 0; i < n; i++) {
            d[i] = a[p][i];
        }
        while (set.size() < n) {
            int le = Integer.MAX_VALUE;
            int num = 0;
            for (int i = 0; i < n; i++) {
                if (!set.contains(i) && le > d[i]) {
                    le = d[i];
                    num = i;
                }
            }
            for (int i = 0; i < n; i++) {
                if (!set.contains(i)) {
                    d[i] = Math.min(d[i], d[num] + a[num][i]);
                }
            }
            set.add(num);
        }
        for (int i = 0; i < n; i++) {
            System.out.println("点" + p + "到点" + i + "的距离为：" + d[i]);
        }
    }
