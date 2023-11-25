import java.util.Scanner;

public class NumberComparison {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numbers = new double[3];

        for (int i = 0; i < 3; i++) {
            System.out.println("Enter number " + (i + 1) + ":");
            numbers[i] = scanner.nextDouble();
        }

        if (numbers[0] > numbers[1] && numbers[0] > numbers[2] && numbers[0] != numbers[1] && numbers[0] != numbers[2]) {
            System.out.println("Condition satisfied.");
        } else {
            System.out.println("Error!!");
        }

        scanner.close();
    }
}
