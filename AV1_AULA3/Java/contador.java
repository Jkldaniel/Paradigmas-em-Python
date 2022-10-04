package Av1_Aula3;

public class contador {

	public static void main(String[] args) {
		   long start = System.currentTimeMillis();

	       for(int i=1; i<=100; i++)

	           System.out.print(i+" ");
	       	   long elapsed = System.currentTimeMillis() - start;
	       	   System.out.print("o metodo foi executado em " + elapsed + "ms");
	       	   
	}
}
	