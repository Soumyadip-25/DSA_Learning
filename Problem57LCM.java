// Find LCM of two numbers
// LCM (Least Common Multiple) is the smallest positive number that is divisible by both given numbers.


import java.util.Scanner;

public class Problem57LCM {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        int x = Math.abs(a);
        int y = Math.abs(b);

        int num1 = x;
        int num2 = y;

        while (num2 != 0) {
            int temp = num2;
            num2 = num1 % num2;
            num1 = temp;
        }

        int gcd = num1;

        if (x == 0 || y == 0) {
            System.out.println("LCM: 0");
        } else {
            int lcm = (x / gcd) * y;
            System.out.println("LCM: " + lcm);
        }

        sc.close();
    }
}
