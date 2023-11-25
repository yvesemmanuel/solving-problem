import java.util.Scanner;
import java.lang.Math;

public class PowerCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the first number (greater than zero): ");
        double number1 = scanner.nextDouble();

        System.out.println("Enter the second number (greater than zero): ");
        double number2 = scanner.nextDouble();

        if (number1 > 0 && number2 > 0) {
            double result = Math.pow(number1, number2);
            System.out.printf("%.2f raised to the power of %.2f is %.2f\n", number1, number2, result);
        } else {
            System.out.println("Both numbers must be greater than zero.");
        }

        scanner.close();
    }
}
