import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int count = 0;
        int startIdx = 0;

        while(true){
            int findIndex = a.indexOf(b, startIdx); // 찾으면 해당 인덱스 반환
            if(findIndex < 0){
                break;
            }
            count++;
            startIdx = findIndex + b.length();
        }
        System.out.println(count);
    }
}