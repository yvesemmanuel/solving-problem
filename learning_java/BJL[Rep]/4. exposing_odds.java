import java.util.Scanner;

public class OddNumbersBetween {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a, b;

        System.out.println("Enter the value for A:");
        a = scanner.nextInt();

        System.out.println("Enter the value for B:");
        b = scanner.nextInt();

        for (int i = a; i <= b; i++) {
            if (i % 2 != 0) {
                System.out.println("It's odd: " + i);
            }
        }

        scanner.close();
    }
}
