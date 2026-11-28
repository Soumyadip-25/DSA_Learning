// Count the frequency of each character in a string
// Count how many times each character appears in a string using HashMap.


import java.util.Scanner;
import java.util.HashMap;

public class CharacterFrequency {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        HashMap<Character, Integer> frequency = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {

            char ch = str.charAt(i);

            if (frequency.containsKey(ch)) {

                frequency.put(ch, frequency.get(ch) + 1);

            } else {

                frequency.put(ch, 1);
            }
        }

        for (char ch : frequency.keySet()) {

            System.out.println(
                ch + " : " + frequency.get(ch)
            );
        }

        sc.close();
    }
}
