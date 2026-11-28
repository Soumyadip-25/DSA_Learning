// Find the Nth Fibonacci Number using Recursion
// Find the Nth Fibonacci number using a recursive function.


import java.util.Scanner;

public class NthFibonacci {

    static int fibonacci(int n) {

        if (n == 0) {
            return 0;
        }

        if (n == 1) {
            return 1;
        }

        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter position: ");
        int n = sc.nextInt();

        if (n < 0) {
            System.out.println("Invalid position");
        } else {
            System.out.println(
                "Fibonacci number: " + fibonacci(n)
            );
        }

        sc.close();
    }
}
