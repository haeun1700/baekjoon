import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
        static boolean[][] arr = new boolean[1001][1001];
        static boolean[] visited = new boolean[1001];

        public static void bfs(int n, int v){
            Queue<Integer> que = new LinkedList<>();
            que.offer(v);
            visited[v] = true;
            while(!que.isEmpty()){
                int cur = que.poll();
                System.out.print(cur + " " );

                for(int i = 1; i<=n; i++) {
                    if(!visited[i] && arr[cur][i]){
                        visited[i] = true;
                        que.offer(i);
                    }
                }
            }
        }
        public static void dfs(int n, int v){
            visited[v] = true;
            System.out.print( v + " ");
            for(int i = 1; i <= n; i++) {
                if(!visited[i] && arr[v][i]) {
                    dfs(n, i);
                }
            }
        }

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int m =Integer.parseInt(tokenizer.nextToken());
        int v = Integer.parseInt(tokenizer.nextToken());

        for(int i = 0; i< m; i++){
            tokenizer = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(tokenizer.nextToken());
            int y = Integer.parseInt(tokenizer.nextToken());
            arr[y][x] = arr[x][y] = true;

        }
//        깊이 우선 탐색
        dfs(n, v);
        Arrays.fill(visited, false);
        System.out.println();
        //너비 우선 탐색
        bfs(n, v);
    }
}