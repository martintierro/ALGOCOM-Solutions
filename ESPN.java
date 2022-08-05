import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.Math.*;
import java.util.Arrays;

//Jarrett Singian, Jade Tan, Martin Tierro
public class ESPN {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        String[] parts = br.readLine().trim().split(" ");
        int n = Integer.parseInt(parts[0]);
        long kx = Long.parseLong(parts[1]);
        long ky = Long.parseLong(parts[2]);
        long[][] people = new long[n][2];
        long distances[]= new long[n];
        for(int i = 0; i < n; i++) {
            parts = br.readLine().trim().split(" ");
            people[i][0] = Long.parseLong(parts[0]);
            people[i][1] = Long.parseLong(parts[1]);
            distances[i]=(Math.abs(kx-people[i][0])+Math.abs(ky-people[i][1]));
            
        }
        Arrays.sort(distances);
    
        int q = Integer.parseInt(br.readLine().trim());
        for(int i = 0; i < q; i++) {
            long e = Long.parseLong(br.readLine().trim());
            int ans = 0;
            ans = getAns(distances, 0, distances.length, e);
            sb.append(ans).append("\n");
        }
        System.out.print(sb);
    }
    

    
    
    
    
    public static int getAns (long[] distances, int left, int right, long e){
        if (right>left){
           final int mid = left + (right - left) / 2;
            if (distances[mid] <= e)
             return getAns(distances, mid+1, right, e); 
            else    
                return getAns(distances, left, mid, e);
        }
       else{
         return left; 
       }
    }
    
}
    