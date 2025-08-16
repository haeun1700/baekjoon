import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/*
문제 프로세스
    - n명, 키 비교 횟수가 주어진다
    - m개 줄에 a와 b의 키를 비교한다. a < b
    - 학생은 1~n번까지 있다.
문제 해결전략 : 위상정렬
    - 3의 선수과목 1 -> 1: 3
    - 3의 선수과목 2 -> 2: 3
    - indegree [0 0 2] => 1삽입 2삽입 3삽입
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // 1. 입력받기 -> 학생이 담긴 indree와 인접리스트
        List<Integer>[] student = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            student[i] = new ArrayList<>();
        }
        int[] indegree = new int[n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            student[a].add(b);
            indegree[b]++;
        }
        Queue<Integer> q = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                q.add(i);
                sb.append(i).append(" ");
            }
        }
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int next : student[node]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.add(next);
                    sb.append(next).append(" ");
                }
            }
        }
        System.out.println(sb);
    }
}