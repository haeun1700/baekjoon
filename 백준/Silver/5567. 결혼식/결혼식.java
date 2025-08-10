import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int n;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
        System.out.println(bfs(1));

    }

    static int bfs(int start) {
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        visited[start] = true;
        int cnt = 0;
        int depth = 0;
        int result = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            cnt++;
            for (int i : graph[cur]) {
                if (!visited[i] && cnt <= depth+1) {
                    q.add(i);
                    visited[i] = true;
                    result++;
                    if(cur == 1) {depth++;}

                }
            }
        }
        return result;
    }
}