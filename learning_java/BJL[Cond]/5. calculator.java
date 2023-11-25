import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[2];

        for (int i = 0; i < 2; i++) {
            System.out.println("Enter integer " + (i + 1) + ":");
            numbers[i] = scanner.nextInt();
        }

        System.out.println("Choose an operation:");
        System.out.println("1 - Add");
        System.out.println("2 - Subtract");
        System.out.println("3 - Multiply");
        System.out.println("4 - Divide");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.println("Result: " + (numbers[0] + numbers[1]));
                break;
            case 2:
                System.out.println("Result: " + (numbers[0] - numbers[1]));
                break;
            case 3:
                System.out.println("Result: " + (numbers[0] * numbers[1]));
                break;
            case 4:
                if (numbers[1] != 0) {
                    System.out.println("Result: " + ((double) numbers[0] / numbers[1]));
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Invalid choice. Please select a valid operation.");
                break;
        }

        scanner.close();
    }
}
