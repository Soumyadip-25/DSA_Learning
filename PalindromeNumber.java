// Check whether a number is a palindrome
// A number is a palindrome if it remains the same when its digits are reversed.

import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int original = num;
        int reverse = 0;

        if (num < 0) {
            System.out.println("Not a Palindrome Number");
        } else {

            while (num > 0) {

                int digit = num % 10;

                reverse = reverse * 10 + digit;

                num = num / 10;
            }

            if (original == reverse) {
                System.out.println("Palindrome Number");
            } else {
                System.out.println("Not a Palindrome Number");
            }
        }

        sc.close();
    }
}