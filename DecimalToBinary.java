// Convert Decimal to Binary
// Convert a decimal number into its binary representation.


import java.util.Scanner;

public class DecimalToBinary {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a decimal number: ");
        int num = sc.nextInt();

        int temp = num;
        String binary = "";

        if (num == 0) {
            binary = "0";
        }

        while (num > 0) {

            int remainder = num % 2;

            binary = remainder + binary;

            num = num / 2;
        }

        System.out.println("Binary of " + temp + ": " + binary);

        sc.close();
    }
}
