import java.util.Scanner;
public class mayor {
static Scanner scanner = new Scanner(System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
int num1;
		System.out.println("type a number");
		num1=scanner.nextInt();
		
		if(num1>0)
			System.out.println("is higher than 0");
		else
			if(num1==0)
				System.out.println("is equal to 0");
		
		
		
	}

}
