import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 최댓값 골라서 점수 고치기
        int n = Integer.parseInt(br.readLine());
        int[] score = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            score[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, score[i]);
        }
        double total = 0;
        for (int i = 0; i < n; i++) {
            total += ((float) score[i] / max) * 100;
        }
        System.out.println(total / n);
    }
}