import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] ans = word.toCharArray();
        for(int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if('A'<= ch && ch <= 'Z'){
                ans[i] = (char)('a'+ ch - 'A');
            }else {
                ans[i] = (char) ('A' + ch - 'a');
            }
        }
        System.out.println(ans);
    }
}