import java.util.Scanner;

public class PositiveNumberCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0, number;

        while (true) {
            System.out.println("Enter a number:");
            number = scanner.nextInt();

            if (number == 0) {
                break;
            } else if (number > 0) {
                count++;
            }
        }

        System.out.println("Number of positive numbers: " + count);
        scanner.close();
    }
}
