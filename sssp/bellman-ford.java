public boolean bellmanFord(int s){
        int[] d = new int[n];
        for(int i=0;i<n;i++){
            d[i] = a[s][i];
        }
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(d[j]!=Integer.MAX_VALUE<<1&& a[j][k]!=Integer.MAX_VALUE<<1){
                        d[k] = Math.min(d[k],d[j]+a[j][k]);
                    }
                }
            }
        }
        for(int j=0;j<n;j++) {
            for (int k = 0; k < n; k++) {
                if (d[j]!=Integer.MAX_VALUE<<1&& a[j][k] != Integer.MAX_VALUE<<1) {
                    if(d[k]>d[j]+a[j][k]){
                        return false;
                    }
                }
            }
        }
