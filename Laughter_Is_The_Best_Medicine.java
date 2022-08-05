/*Jade Tan, Jarrett Singian, Martin Tierro*/



import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Laughter_Is_The_Best_Medicine {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] parts = br.readLine().split("\\s+");
		long n = Long.parseLong(parts[0]);
		long k = Long.parseLong(parts[1]);
        long a=0;
        long length = getLength(a)[1];
        for (a = 0;  length < (long)1e18 && a <= (long)10e5; a++) {
            length = getLength(a)[1];
        }
        if (n > a) {
            n = a;
        }
		System.out.println(solve(n,k));
	}
  
    public static char solve(long n, long k) {
    	// solve answer here. Return correct answer
        if (n==0) {
            return 'H';
        } else if (n==1) {
            return 'A';
        } else {
            long[] halves = getLength(n-1);
            long halfLeft = halves[1], halfRight = halves[0];
            if (k+1 > halfLeft) {
                return solve(n-1, k-halfLeft); // go to right
            } else {
                return solve(n-2, k); // go to left
            }
        }
        
    }
               
    static long[] getLength(long n) { 
        long F[][] = new long[][]{{1,1},{1,0}}; 
        n+=1;
        if (n == 0) 
            return new long[]{0,0}; 
        power(F, n-1); 
           return F[0]; 
    } 
    
    static void multiply(long F[][], long M[][]) { 
        long x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]; 
        long y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]; 
        long z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]; 
        long w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]; 

        F[0][0] = x; 
        F[0][1] = y; 
        F[1][0] = z; 
        F[1][1] = w; 
    } 
  
    static void power(long F[][], long n) { 
        long i; 
        long M[][] = new long[][]{{1,1},{1,0}}; 
      
        for (i = 2; i <= n; i++) 
            multiply(F, M); 
    } 
}