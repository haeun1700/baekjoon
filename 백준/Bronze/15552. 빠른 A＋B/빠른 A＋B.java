import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();//출력 대신 사용
        String T = br.readLine(); //한 줄 그대로 입력받기

        int a = Integer.parseInt(T); //int값으로 변형
        for(int i = 0; i < a; i++){
            String str = br.readLine();//숫자 입력
            //공백을 기준으로 나누겠다는 뜻
            int target = str.indexOf(" "); //" "와 같은 공백으로 구분하여 하나씩 문자를 가져옴
            //0번째와 1번째를 가져와 int 형으로 변환하겠다는 뜻
            int result = Integer.parseInt(str.substring(0,target))+Integer.parseInt(str.substring(target+ 1)); //substring은 문자열 0번째부터 공백까지와 그 다음 공백부터 다음 문자까지 더하기
            sb.append(result+"\n");//출력할 것을 가져옴. 출력이 이뤄지는 않음.
        }
        br.close();
        System.out.print(sb); //출력
    }
}