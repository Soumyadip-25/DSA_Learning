// Convert Binary to Decimal
// Convert a binary number into its decimal representation.


import java.util.Scanner;

public class BinaryToDecimal {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a binary number: ");
        String binary = sc.next();

        int decimal = 0;
        int power = 1;

        for (int i = binary.length() - 1; i >= 0; i--) {

            char digit = binary.charAt(i);

            if (digit != '0' && digit != '1') {
                System.out.println("Invalid binary number");
                sc.close();
                return;
            }

            if (digit == '1') {
                decimal = decimal + power;
            }

            power = power * 2;
        }

        System.out.println("Decimal: " + decimal);

        sc.close();
    }
}
