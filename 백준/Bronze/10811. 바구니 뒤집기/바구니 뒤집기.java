import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        for(int i = 0; i< n; i++){
            arr.add(i+1);
        }
        for(int i = 0; i<m; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            List<Integer> sub = arr.subList(a-1, b);
            Collections.reverse(sub);
        }
        for(int num : arr){
            System.out.print(num + " ");
        }
    }
}