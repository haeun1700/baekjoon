import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();
        String searchWord = sc.nextLine();

        String replaced = text.replace(searchWord, "");
        int length = text.length() - replaced.length();
        int count = length / searchWord.length();
        System.out.println(count);
    }
}