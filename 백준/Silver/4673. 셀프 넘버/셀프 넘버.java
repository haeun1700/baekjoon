import java.io.IOException;

public class Main {
    static int[] arr = new int[10000];

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < 10000; i++) {
            int num = kaprekar(i);
            if(num < 10000){
                arr[num] = 1;
            }
        }
        for (int i = 1; i < 10000; i++) {
            if (arr[i] == 0) {
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
    }

    static int kaprekar(int num) {
        String value = String.valueOf(num);
        int result = num;
        for (int i = 0; i < value.length(); i++) {
            result += value.charAt(i) - '0';
        }

        return result;
    }
}