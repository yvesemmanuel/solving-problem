import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Stack;

public class Main {
    public static boolean isOperand(String str) {
        try {
            Double.parseDouble(str);
        } catch (NumberFormatException nfe) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        try {
            List<String> allLines = Files.readAllLines(Paths.get("Calc1.stk"));
            Stack<Float> RPNStacker = new Stack<>();
            for (int i = 0; i < allLines.size(); i++) {
                String it = allLines.get(i);
                
                if (isOperand(it)) {
                    RPNStacker.add(Float.parseFloat(it));
                }
                else {
		            Float y = RPNStacker.pop();
                    Float x = RPNStacker.pop();

                    if (it.equals("*")) {
                        RPNStacker.add(x * y);
                    }
                    else if (it.equals("+")) {
                        RPNStacker.add(x + y);
                    }
                    else if (it.equals("-")) {
                        RPNStacker.add(x - y);
                    }
                    else if (it.equals("/")) {
                        RPNStacker.add(x / y);
                    }
                }
                    
            }

            System.out.println("O resultado da operação posfixa " + "'" + String.join(" ", allLines) + "' é: " + RPNStacker.pop());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}