import java.io.IOException;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 1; i < 10; i++){
            System.out.printf("%d * %d = %d\n", n, i, n*i);
        }
    }
}