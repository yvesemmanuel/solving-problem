import java.util.Scanner;

public class CompareNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the first number:");
        double number1 = scanner.nextDouble();

        System.out.println("Enter the second number:");
        double number2 = scanner.nextDouble();

        if (number1 > number2) {
            System.out.println("The greater number is: " + number1);
        } else if (number2 > number1) {
            System.out.println("The greater number is: " + number2);
        } else {
            System.out.println("Both numbers are equal.");
        }

        scanner.close();
    }
}
