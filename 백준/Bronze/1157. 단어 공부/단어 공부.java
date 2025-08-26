import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/*
1. 단어를 입력받는다. -> 대문자로 처리한다.
2. HashMap을 선언한다.
    2-1. 해당 문자열의 문자를 key,value로 저장한다.
3. Map의 키와 밸류값이 무엇인지 순회한다.
    3-1. 만약 밸류가 현재 max보다 높으면 갱신
    3-2. 만약 max와 value가 동일하면 ?로 저장
4. 최종 res값 출력
 */
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //1. 단어를 입력받는다. -> 대문자로 처리한다.
        String word = br.readLine().toUpperCase();
        //2. HashMap을 선언한다.
        HashMap<Character, Integer> map = new HashMap<>();
        //2-1. 해당 문자열의 문자를 key,value로 저장한다.
        for(int i = 0; i< word.length(); i++){
            char c = word.charAt(i);
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        // 3. Map의 키와 밸류값이 무엇인지 순회한다.
        int maxValue = Integer.MIN_VALUE;
        char res = ' ';

        for(Map.Entry<Character, Integer> entry : map.entrySet()){

            if(maxValue <= entry.getValue()){
                // 3-2. 만약 max와 value가 동일하면 ?로 저장
                res = maxValue == entry.getValue() ? '?' : entry.getKey();
                // 3-1. 만약 밸류가 현재 max보다 높으면 갱신
                maxValue = entry.getValue();
            }
        }
        System.out.println(res);
    }
}