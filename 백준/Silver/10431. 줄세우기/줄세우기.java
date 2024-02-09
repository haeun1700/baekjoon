import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token;
        int p = Integer.parseInt(br.readLine());

        while(p-- > 0){
            token = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(token.nextToken());
            int[] arr= new int[20];
            for(int i = 0; i< 20; i++){
                arr[i] = Integer.parseInt(token.nextToken());
            }

            int cnt = 0;
            int[] sorted = new int[20];
            for(int  i = 0; i< 20; i++){
                boolean find = false;
                for(int j = 0; j<i; j++){
                    if(sorted[j] > arr[i]){
                        find = true;
                        for(int k = i-1; k >= j; k--){
                            sorted[k+1] = sorted[k];
                            cnt++;
                        }
                        sorted[j] = arr[i];
                        break;
                    }
                }
                if(!find) sorted[i] = arr[i];
            }
            System.out.println(t + " " + cnt);
        }
    }
}