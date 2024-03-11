public class PointTest {
    public static void main(String[] args) {
        testConstructor();
        testSetX();
        testSetY();
        testMoveBy();
    }

    public static void testConstructor() {
        Point p = new Point(10, 10);
        assert p.getX() == 10;
        assert p.getY() == 10;
    }

    public static void testSetX() {
        Point p = new Point(0, 0);
        p.setX(100);
        assert p.getX() == 100;
        try {
            p.setX(-10);
            assert false;
        } catch (IllegalArgumentException e) { }
        try {
            p.setX(500);
            assert false;
        } catch (IllegalArgumentException e) {}
    }

    public static void testSetY() {
        Point p = new Point(0, 0);
        p.setY(200);
        assert p.getY() == 200;
        try {
            p.setY(-10);
            assert false;
        } catch (IllegalArgumentException e) {}
        try {
            p.setY(500);
            assert false;
        } catch (IllegalArgumentException e) {}
    }

    public static void testMoveBy() {
        Point p = new Point(100, 100);
        p.moveBy(50, -30);
        assert p.getX() == 150;
        assert p.getY() == 70;
        try {
            p.moveBy(-200, 0);
            assert false;
        } catch (IllegalArgumentException e) { }
        try {
            p.moveBy(0, 500);
            assert false;
        } catch (IllegalArgumentException e) { }
    }
}
