import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        String[] num = br.readLine().split(" ");
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(num[i]);
        }
        int maxValue = arr[0];
        int minValue = arr[0];

        for(int i = 0; i < num.length; i++){
            if(arr[i] > maxValue){
                maxValue = arr[i];
            } else if(arr[i] < minValue){
                minValue = arr[i];
            }
        }
        System.out.printf("%d %d", minValue, maxValue);
    }
}