import java.util.Scanner;

public class NumberOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numbers = new double[2];

        for (int i = 0; i < 2; i++) {
            System.out.println("Enter number " + (i + 1) + ":");
            numbers[i] = scanner.nextDouble();
        }

        double number1 = numbers[0];
        double number2 = numbers[1];

        if (number1 == number2) {
            double product = number1 * number2;
            System.out.println("The multiplication of the numbers is: " + product);
        } else if (number1 > number2) {
            double difference = number1 - number2;
            System.out.println("The subtraction of the first number by the second is: " + difference);
        } else {
            double sum = number1 + number2;
            System.out.println("The sum of the numbers is: " + sum);
        }

        scanner.close();
    }
}
