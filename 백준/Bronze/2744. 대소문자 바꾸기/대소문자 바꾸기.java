import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();

        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);

            if((int)ch < 97){
                System.out.print(Character.toLowerCase(ch));
            }else{
                System.out.print(Character.toUpperCase(ch));
            }
        }
    }
}