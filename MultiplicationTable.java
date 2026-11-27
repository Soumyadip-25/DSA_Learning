// Print the multiplication table of a number
// Print the multiplication table of a given number from 1 to 10.


import java.util.Scanner;

public class MultiplicationTable {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        for (int i = 1; i <= 10; i++) {

            int result = num * i;

            System.out.println(num + " x " + i + " = " + result);
        }

        sc.close();
    }
}
