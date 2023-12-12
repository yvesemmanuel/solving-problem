import java.util.Scanner;

public class PrintIntegers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a, b;

        System.out.println("Enter the value for A:");
        a = scanner.nextInt();

        while (true) {
            System.out.println("Enter the value for B (must be greater than A):");
            b = scanner.nextInt();

            if (b <= a) {
                System.out.println("Error: B must be greater than A. Please re-enter.");
            } else {
                break;
            }
        }

        System.out.println("Number series:");
        for (int i = a + 1; i < b; i++) {
            System.out.print(i + " ");
        }

        scanner.close();
    }
}
