// Calculate power without using Math.pow()
// Calculate the power of a number using a loop.


import java.util.Scanner;

public class Problem58PowerCalculation {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter base: ");
        int base = sc.nextInt();

        System.out.print("Enter exponent: ");
        int exponent = sc.nextInt();

        if (exponent < 0) {
            System.out.println("Please enter a non-negative exponent.");
        } else {

            long result = 1;

            for (int i = 1; i <= exponent; i++) {
                result = result * base;
            }

            System.out.println("Result: " + result);
        }

        sc.close();
    }
}
