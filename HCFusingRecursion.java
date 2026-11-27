// Find HCF using Recursion
// HCF (Highest Common Factor), also called GCD, is the largest number that divides two numbers exactly.


import java.util.Scanner;

public class HCFUsingRecursion {

    static int findHCF(int a, int b) {

        if (b == 0) {
            return a;
        }

        return findHCF(b, a % b);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = sc.nextInt();

        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        int result = findHCF(Math.abs(a), Math.abs(b));

        System.out.println("HCF: " + result);

        sc.close();
    }
}
