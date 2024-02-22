import java.util.Scanner;

class Main {
    //연결요소가 몇개인가?
    //
    static int n, m;
    static int[][] graph;
    static boolean[] visited;
    static int cnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        //1. 정점 연결 처리
        for (int i = 0; i < m; i++) {
            int src = sc.nextInt();
            int dst = sc.nextInt();
            graph[src][dst] = graph[dst][src] = 1;

        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                dfs(i);
                cnt++; //새로운 연결 요소 찾는 것. 새로운 dfs호출의 개수를 출력하는 것 => 방문한 이력이 있다면 pass.
            }
        }
        System.out.println(cnt);
    }

    static void dfs(int node) {
        visited[node] = true;
        for (int i = 1; i <= n; i++) {
            if (graph[node][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }
}