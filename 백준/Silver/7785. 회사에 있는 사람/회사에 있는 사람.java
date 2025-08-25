
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        // 2번 전략으로 실행
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb =new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        List<Person> list = new ArrayList<>();
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String state = st.nextToken();

            Person person = new Person(name, state);
            list.add(person);
        }
        Collections.sort(list, (o1, o2) -> {
            return o2.name.compareTo(o1.name);
        });

        for(int i = 0; i<list.size()-1; i++){
            if(!list.get(i).name.equals(list.get(i+1).name) && list.get(i).state.equals("enter")) {
                sb.append(list.get(i).name).append("\n");
            }
        }
        if(list.get(list.size()-1).state.equals("enter")){sb.append(list.get(list.size()-1).name).append("\n");}
        System.out.println(sb);
    }
    static class Person{
        String name, state;
        public Person(String name, String state){
            this.name = name;
            this.state = state;
        }
    }
}
