// Find the sum of first N natural numbers using Recursion
// Calculate the sum of all natural numbers from 1 to N using recursion.


import java.util.Scanner;

public class SumOfNaturalNumbers {

    static int calculateSum(int n) {

        if (n == 0) {
            return 0;
        }

        return n + calculateSum(n - 1);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        if (n < 0) {
            System.out.println("Enter a non-negative number");
        } else {
            int result = calculateSum(n);

            System.out.println("Sum: " + result);
        }

        sc.close();
    }
}
