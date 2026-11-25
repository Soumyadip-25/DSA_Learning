// Find the missing number in an array using XOR
// An array contains numbers from 1 to N, but one number is missing. Find the missing number.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter N: ");
        int n = sc.nextInt();

        int xor = 0;

        System.out.println("Enter " + (n - 1) + " elements:");

        for (int i = 0; i < n - 1; i++) {
            int num = sc.nextInt();
            xor = xor ^ num;
        }

        for (int i = 1; i <= n; i++) {
            xor = xor ^ i;
        }

        System.out.println("Missing number: " + xor);

        sc.close();
    }
}