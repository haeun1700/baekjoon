import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

/*
문제 전략 : 가중치가 있는 bfs, 현재 위치에서 +1 하는 삽질하는 문제
 */
public class Main{
    static int N, M;
    static int[][] box;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        box = new int[N][M];
        // 토마토 정보 담기
//        int startX = 0, startY= 0;
        Stack<int[]> start = new Stack<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
                // 출발 위치 구하기
                if (box[i][j] == 1) {
                    start.add(new int[]{i, j});
                }
            }
        }
        // bfs 호출하면서 삽질하기
        int minDay = bfs(start, 0);
        if (!check()){minDay = -1;}
        System.out.println(minDay);
    }

    static int bfs(Stack<int[]> stack, int depth) {
        //1. 방문할 큐와 방문 배열 생성
        Queue<Node> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];
        // 현재 위치 x,y값 큐에 삽입
        for (int i = 0; i < stack.size(); i++) {
            int[] adj = stack.get(i);
            queue.offer(new Node(adj[0], adj[1], depth));
            visited[adj[0]][adj[1]] = true;
        }
        int curDepth = 0;
        // 큐가 빌 때까지 삽질하기
        while (!queue.isEmpty()) {
            // 현재 위치값 꺼내기
            Node cur = queue.poll();
            curDepth = Math.max(cur.depth, curDepth);
            // 상하좌우 탐색
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + cur.x;
                int ny = dy[i] + cur.y;

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }// 범위가 벗어나면 continue
                if (visited[nx][ny]) {
                    continue;
                }
                if (box[nx][ny] != 0) {
                    continue;
                }
                box[nx][ny] = cur.depth+1;
                queue.offer(new Node(nx, ny, cur.depth + 1));
                visited[nx][ny] = true;
            }
        }
        return curDepth;
    }

    static class Node {
        int x, y, depth;

        public Node(int x, int y, int depth) {
            this.x = x;
            this.y = y;
            this.depth = depth;
        }
    }

    static boolean check(){
        for(int i = 0; i< N; i++){
            for(int j = 0; j<M; j++){
                if(box[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }
}