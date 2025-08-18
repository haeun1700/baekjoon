import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};
    static int w, h;
    static boolean[][] visited;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        do {
            map = new int[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int cnt = 0;
            visited = new boolean[h][w];
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (!visited[i][j] && map[i][j] == 1) {
                        cnt++;
                        bfs(i, j);
                    }
                }
            }
            System.out.println(cnt);
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
        } while (w != 0 || h != 0);

    }

    private static void bfs(int i, int j) {
        visited[i][j] = true;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{i, j});

        while (!queue.isEmpty()) {
            int[] res = queue.poll();
            for (int n = 0; n < 8; n++) {
                int nx = dx[n] + res[0];
                int ny = dy[n] + res[1];
                if (nx < 0 || ny < 0 || nx >= h || ny >= w) {continue;}
                if (!visited[nx][ny] && map[nx][ny] == 1) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
    }
}
