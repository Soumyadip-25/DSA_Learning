// Check whether a number is a Perfect Number
// A perfect number is a number whose sum of proper divisors equals the number itself.


import java.util.Scanner;

public class PerfectNumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int sum = 0;

        for (int i = 1; i <= num / 2; i++) {

            if (num % i == 0) {
                sum = sum + i;
            }
        }

        if (num > 1 && sum == num) {
            System.out.println("Perfect Number");
        } else {
            System.out.println("Not a Perfect Number");
        }

        sc.close();
    }
}
