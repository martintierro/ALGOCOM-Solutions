    //JARRETT ETHAN SINGIAN    JADE NICOLE TAN    MARTIN ANGELO TIERRO
    
    import java.io.BufferedReader;
    import java.io.InputStreamReader;
    import java.util.Stack;
    import java.util.LinkedList;
    import java.util.Deque;

    public class CheatingDebt {

        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();
            int m = Integer.parseInt(br.readLine().trim().split(" ")[1]);
            String num = br.readLine().trim();
            sb = new StringBuilder ();
        
        System.out.println (removeDebt(num, m, sb).toString());
        
        
        }


        public static boolean isZeroNotAt2ndDigit (int a, int m, boolean potential){

           // System.out.println ("ISZERO "+(a=='0')+" "+a);

            if (a=='0' && m>0&&potential)
                return false;
            else
                return true;
        }

        



        public static StringBuilder removeDebt (String num, int m, StringBuilder sb){

            Deque<Character> deque = new LinkedList<>();
            Stack<Character> stack = new Stack<>();
            int zeroes=0;

            if(m==num.length())
                return new StringBuilder("0");


            for (int i = 0; i<num.length(); i++){

                 while (m > 0 && !deque.isEmpty() && check(deque, stack ,num.charAt(i), zeroes, m) && ( num.length() - m == 1 || deque.size() != 1 || num.charAt(i) != '0')){
                    char temp = deque.pollLast();
                    if(temp != '0')
                        stack.pop();
                    else
                        zeroes--;
                    m--;
                }
                
                deque.addLast(num.charAt(i));
                if(num.charAt(i) != '0'){
                    stack.add(num.charAt(i));
                }
                else
                    zeroes++;
            }

            while(m > 0 && deque.size() > 0){
                deque.pollLast();
                m--;
            }
            if(deque.size() == 0){
                sb.append('0');
            }
            while(deque.size() > 0){
                sb.append(deque.poll());
            }
              
            return sb;
        }


    
        static boolean check(Deque<Character> deque, Stack<Character> stack, char currentChar, long count, int m){
            if(deque.peekLast() != '0' || (deque.peekLast() == '0' && currentChar == '0'))
                return deque.peekLast() > currentChar;
            else {
                if(count >= m)
                    return false;
                else
                    return stack.peek() > currentChar;
                
            }
        }

        
           
    }