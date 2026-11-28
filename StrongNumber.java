// Check whether a number is a Strong Number
// A Strong Number is a number whose sum of the factorials of its digits equals the original number.


import java.util.Scanner;

public class StrongNumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int original = num;
        int sum = 0;

        if (num < 0) {
            System.out.println("Not a Strong Number");
        } else {

            while (num > 0) {

                int digit = num % 10;

                int fact = 1;

                for (int i = 1; i <= digit; i++) {
                    fact = fact * i;
                }

                sum = sum + fact;

                num = num / 10;
            }

            if (sum == original) {
                System.out.println("Strong Number");
            } else {
                System.out.println("Not a Strong Number");
            }
        }

        sc.close();
    }
}
