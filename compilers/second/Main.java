import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Stack;
import java.util.ArrayList;

public class Main {
    public static boolean isOperand(String str) {
        try {
            Double.parseDouble(str);
        } catch (NumberFormatException nfe) {
            return false;
        }
        return true;
    }

    public static Token Tokenization(String it) throws Exception {
        if (isOperand(it)) {
            return new Token(TokenType.NUM, it);
        }
        else if (it.equals("*")) {
            return new Token(TokenType.STAR, it);
        }
        else if (it.equals("+")) {
            return new Token(TokenType.PLUS, it);
        }
        else if (it.equals("-")) {
            return new Token(TokenType.MINUS, it);
        }
        else if (it.equals("/")) {
            return new Token(TokenType.SLASH, it);
        }
        else {
            throw new Exception("Invalid character: " + it);
        }
    }

    public static Float ApplyOperation(Float x, Float y, String OP) throws Exception {
        if (OP.equals("*")) {
            return x * y;
        }
        else if (OP.equals("+")) {
            return x + y;
        }
        else if (OP.equals("-")) {
            return x - y;
        }
        else if (OP.equals("/")) {
            return x / y;
        }
        else {
            throw new Exception("Invalid operation: " + OP);
        }
    }

    public static void main(String[] args) throws Exception {
        List<String> allLines = Files.readAllLines(Paths.get("Calc2.stk"));
        Stack<Float> RPNStacker = new Stack<>();
        List<Token> tokens = new ArrayList<Token>();

        for (int i = 0; i < allLines.size(); i++) {
            String it = allLines.get(i);
            tokens.add(Tokenization(it));
        }

        
        while (!tokens.isEmpty()) {
            String it = tokens.remove(0).lexeme;
            
            if (isOperand(it)) {
                RPNStacker.add(Float.parseFloat(it));
            }
            else {
                Float y = RPNStacker.pop();
                Float x = RPNStacker.pop();

                RPNStacker.add(ApplyOperation(x, y, it));
            }
        }

        System.out.println("O resultado da operação posfixa " + "'" + String.join(" ", allLines) + "' é: " + RPNStacker.pop());

    }
}