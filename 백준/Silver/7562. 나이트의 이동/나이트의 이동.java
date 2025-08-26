import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;
/*
1. 입력받기
    1-1. 테스트 케이스
    1-2. 체스판 길이 I
    1-3. 출발지 x,y
    1-4. 도착지 x,y
2. 정의하기
    2-1. 체스판 정의하기 i*i
    2-2. visited배열 정의하기 2차원 배열
    2-3. 이동할 수 있는 거리 정의하기
3. bfs함수
    3-1. 0,0부터 시작해서 호출하기
    3-2. 큐 생성
    3-3. 현재 값 큐에 삽입, 방문 처리
    3-4. 큐가 빌 때까지
        - for문 8번 돌면서
            - 방문하지 않았고
            - 범위 벗어나지 않았다면
            - 방문 처리
            - 큐에 넣기 (x,y,cnt+1)
 */
public class Main {
//   2-1. 체스판 정의하기 i*i
    static int[][] map;
    // 2-2. visited배열 정의하기 2차원 배열
    static boolean[][] visited;
    // 2-3. 이동할 수 있는 거리 정의하기
    static int[] dx = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dy = {-2, -1, 1, 2, -2, -1, 1, 2};
    static int startX, startY, endX, endY, cnt, I;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            // 1-2. 체스판 길이 I
            I = Integer.parseInt(br.readLine());
            map = new int[I][I];
            visited = new boolean[I][I];
//        1-3. 출발지 x,y
            st = new StringTokenizer(br.readLine());
            startX = Integer.parseInt(st.nextToken());
            startY = Integer.parseInt(st.nextToken());
//        1-4. 도착지 x,y
            st = new StringTokenizer(br.readLine());
            endX = Integer.parseInt(st.nextToken());
            endY = Integer.parseInt(st.nextToken());
//        3-1. 0,0부터 시작해서 호출하기
            cnt = 0;
            System.out.println(bfs(startX, startY, cnt));
        }
    }
    private static int bfs(int x, int y, int cnt){
        //3-2. 큐 생성
        Queue<int[]> queue = new ArrayDeque<>();
        //3-3. 현재 값 큐에 삽입, 방문 처리
        queue.offer(new int[]{x,y,cnt+1});
        visited[x][y] = true;
        //3-4. 큐가 빌 때까지
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            // for문 8번 돌면서
            for(int dir= 0; dir<8; dir++){
                int nx = dx[dir] + cur[0];
                int ny = dy[dir] + cur[1];
                cnt = cur[2];

                if(nx <0 || ny <0|| nx >= I || ny >= I) {continue;}
                if(visited[nx][ny]) {continue;}
                if(nx == endX && ny == endY) {
                    return cnt;
                }
                visited[nx][ny] = true;
                queue.offer(new int[]{nx,ny,cnt+1});
            }
        }
    return 0;
    }
}