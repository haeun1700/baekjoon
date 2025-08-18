import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static boolean[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static char[][] arr;
    static int N, cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new char[N][];
        visited = new boolean[N][N];
        for(int i = 0; i<N; i++){
            arr[i] = br.readLine().toCharArray();
        }
        int depth = 0;
        List<Integer> res = new ArrayList<>();

        // 모든 행렬을 돌면서 방문하지 않았고 연결되어 있다면 호출하기
        for(int i = 0; i < N; i++){
            for(int j = 0; j <N; j++){
                if(!visited[i][j] && arr[i][j] == '1'){
                    // 한번 호출되면 계속 연결된 것들을 찾을 것이기 때문에 다시 돌아왔을 때가 이제 다음 단지번호가 된다.
//                    System.out.println("방문한다. ");
                    depth++;
                    cnt = 0; // 다음 단지에 세대수를 세기위해 0으로 초기화한다.
                    res.add(dfs(i,j));
                }
            }
        }
        // 오름차순 정렬
        Collections.sort(res);
        sb.append(depth).append("\n");
        for(int i : res){
            sb.append(i).append("\n");
        }
        System.out.println(sb);
    }

    // 현재 좌표값과 세대수
    private static int dfs(int i, int j){
        visited[i][j] =true;
        cnt++;
        // 상하좌우 탐색
        for(int idx = 0; idx<4; idx++){
            int nx = dx[idx] + i;
            int ny = dy[idx]+j;
            // 새로운 좌표가 범위를 벗어나면 continue
            if(nx < 0 || ny < 0 || nx >=N ||  ny >= N){
                continue;
            }
            if(!visited[nx][ny] && arr[nx][ny] == '1'){
                dfs(nx, ny);
            }
        }
        return cnt;
    }
}