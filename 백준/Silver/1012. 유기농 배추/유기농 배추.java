import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
  static class Position {
    public int y, x;
    public Position(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  static final int []dy = {0,1,0,-1};
  static final int []dx = {1,0,-1,0};
  static boolean [][]field = new boolean[52][52];

  public static void check(int n, int m, int r, int c) {
    Queue<Position> q = new LinkedList<>();
    q.offer(new Position(r, c));
    field[r][c] = false;
    while(!q.isEmpty()) {
      Position cur = q.poll();
      for(int i = 0; i < 4; i++) {
        int ny = cur.y + dy[i];
        int nx = cur.x + dx[i];
        if(ny < 0 || ny >= n || nx < 0 || nx>= m || !field[ny][nx]) continue;
        field[ny][nx] = false;
        q.offer(new Position(ny, nx));
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int tc = Integer.parseInt(br.readLine());
    while(tc-- > 0) {
      StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
      int m = Integer.parseInt(stk.nextToken()), n = Integer.parseInt(stk.nextToken()), k = Integer.parseInt(stk.nextToken());
      for(int i = 0 ; i < k; i++) {
        stk = new StringTokenizer(br.readLine(), " ");
        int c = Integer.parseInt(stk.nextToken()), r = Integer.parseInt(stk.nextToken());
        field[r][c] = true;
      }
      int count = 0;
      for(int i = 0 ; i < n; i++) {
        for(int j = 0 ; j < m; j++) {
          if(field[i][j]){
            check(n, m, i, j);
            count++;
          }
        }
      }
      System.out.println(count);
    }
  }

}