import java.util.Scanner;

public class AverageCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double sum = 0;

        for (int i = 1; i <= 3; i++) {
            System.out.println("Enter grade " + i + ": ");
            double grade = scanner.nextDouble();
            sum += grade;
        }

        double average = sum / 3;
        System.out.println("The arithmetic average of the grades is: " + average);

        scanner.close();
    }
}