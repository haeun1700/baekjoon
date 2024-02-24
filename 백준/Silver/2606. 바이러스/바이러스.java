import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
    static boolean[][] arr = new boolean[101][101];
    static boolean[] visited = new boolean[102];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        StringTokenizer token;
        for (int i = 0; i < m; i++) {
            token = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            arr[a][b] = arr[b][a] = true; //서로 연결
        }
        Queue queue = new LinkedList();

        queue.offer(1);
        visited[1] = true;
        int count = 0;
        while (!queue.isEmpty()) {
            int cur = (int) queue.poll(); //앞에있는거

            for (int i = 1; i <= n; i++) {
                if (!visited[i] && arr[cur][i]) {
                    queue.offer(i);
                    visited[i] = true;
                    count++;
                }
            }
        }
        System.out.println(count);

    }
}