import java.nio.file.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String data0 = new String(Files.readAllBytes(Paths.get("Calc1.stk")));
        String data1 = new String(Files.readAllBytes(Paths.get("Calc2.stk")));

        args = new String[2];
        args[0] = data0;
        args[1] = data1;
        Postfix.main(args);
    }
}
