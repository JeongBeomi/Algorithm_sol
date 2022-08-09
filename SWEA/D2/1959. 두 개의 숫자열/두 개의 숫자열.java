import java.util.Scanner;

public class Solution{
    public static void main(String[] args){
        Scanner a = new Scanner(System.in);
        int case_num = a.nextInt();
        for(int i=0; i<case_num; i++) {
        	int N = a.nextInt();
        	int M = a.nextInt();
        	int[] arr1 = new int[N];
        	int[] arr2 = new int[M];
        	for(int j=0; j<N; j++) {
        		arr1[j] = a.nextInt();
        	}
        	for(int k=0; k<M; k++) {
        		arr2[k] = a.nextInt();
        	}
        	int sum=0;
        	int max =0;
        	if (N >= M){
        		for (int l = 0; l<N-M+1; l++) {
        			for(int o=0;o<M;o++) {
        				sum += arr1[o+l]*arr2[o];        				
        			}
        			if(max>sum) {
        				sum = 0;
        			}
        			else {
        				max = sum ;
        				sum = 0;
        			}
        		}
        	}
        	else {
        		for(int l= 0; l<M-N+1; l++) {
        			for(int o=0; o<N; o++) {
        				sum += arr1[o]*arr2[o+l];
        			}
        			if(max>sum) {
        				sum =0;
        			}
        			else {
        				max =sum;
        				sum = 0;
        			}
        		}
        	}
        	System.out.println("#"+(i+1)+" "+max);
        }
        a.close();      
    }
}