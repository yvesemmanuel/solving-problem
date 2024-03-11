public class Point {
    private int x = 0, y = 0;

    public Point(int x, int y) {
        setX(x);
        setY(y);
    }

    public int getX() { 
        return x; 
    }

    public int getY() { 
        return y; 
    }

    public void setX(int x) { 
        if (x >= 0 && x <= 400) {
            this.x = x;
        } else {
            throw new IllegalArgumentException("X coordinate must be between 0 and 400.");
        }
    }

    public void setY(int y) { 
        if (y >= 0 && y <= 400) {
            this.y = y;
        } else {
            throw new IllegalArgumentException("Y coordinate must be between 0 and 400.");
        }
    }

    public void moveBy(int dx, int dy) {
        int newX = x + dx;
        int newY = y + dy;

        if (newX >= 0 && newX <= 400 && newY >= 0 && newY <= 400) {
            x = newX;
            y = newY;
        } else {
            throw new IllegalArgumentException("New coordinates must be within the range [0, 400].");
        }
    }
}
