// Find the single non-repeating element
// An array contains elements where every number appears twice except one. Find that single element.

import java.util.Scanner;

public class NonRepeatingElement {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int xor = 0;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            xor = xor ^ num;
        }

        System.out.println("Non-repeating element: " + xor);

        sc.close();
    }
}