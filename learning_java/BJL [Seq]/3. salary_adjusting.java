import java.util.Scanner;

public class SalaryIncrease {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the current salary:");
        double currentSalary = scanner.nextDouble();

        double increaseRate = 0.25;  // 25% increase
        double newSalary = currentSalary * (1 + increaseRate);

        System.out.printf("The new salary after a 25%% increase is: %.2f\n", newSalary);

        scanner.close();
    }
}
