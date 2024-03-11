public class PointTest {
    public static void main(String[] args) {
        Point point1 = new Point();
        Point point2 = new Point();
        point1.setX(10);
        point1.setY(20);
        point2.setX(10);
        point2.setY(20);

        System.out.println("Point 1: " + point1);
        System.out.println("Point 2: " + point2);
        System.out.println("Are point1 and point2 equal? " + point1.equals(point2));

        ScreenPoint screenPoint1 = new ScreenPoint();
        ScreenPoint screenPoint2 = new ScreenPoint();
        screenPoint1.setX(100);
        screenPoint1.setY(200);
        screenPoint2.setX(100);
        screenPoint2.setY(200);

        System.out.println("\nScreenPoint 1: " + screenPoint1);
        System.out.println("ScreenPoint 2: " + screenPoint2);
        System.out.println("Are screenPoint1 and screenPoint2 equal? " + screenPoint1.equals(screenPoint2));
    }
}
