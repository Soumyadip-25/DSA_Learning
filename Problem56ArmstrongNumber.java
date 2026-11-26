// Check Armstrong Number
// An Armstrong number is a number whose sum of each digit raised to the power of the total number of digits equals the original number.


import java.util.Scanner;

public class Problem56ArmstrongNumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int original = num;
        int temp = num;
        int digits = 0;
        int sum = 0;

        if (num < 0) {
            System.out.println("Not an Armstrong Number");
        } else {

            if (num == 0) {
                digits = 1;
            }

            while (temp > 0) {
                digits++;
                temp = temp / 10;
            }

            temp = num;

            while (temp > 0) {
                int digit = temp % 10;
                sum += (int) Math.pow(digit, digits);
                temp = temp / 10;
            }

            if (sum == original) {
                System.out.println("Armstrong Number");
            } else {
                System.out.println("Not an Armstrong Number");
            }
        }

        sc.close();
    }
}
