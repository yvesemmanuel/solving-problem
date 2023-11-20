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

    /**
    * Return tokens' list after reading all file lines
    * or throw and exception if invalid character identified
    * @param allLines list contaning all the file's lines
    * @return a list containing Token elements
    */
    public static List<Token> tokenization(List<String> allLines) throws Exception {
        List<Token> tokens = new ArrayList<Token>();

        for (int i = 0; i < allLines.size(); i++) {
            String it = allLines.get(i);
            
            if (isOperand(it)) {
                tokens.add(new Token(TokenType.NUM, it));
            }
            else if (it.equals("*")) {
                tokens.add(new Token(TokenType.STAR, it));
            }
            else if (it.equals("+")) {
                tokens.add(new Token(TokenType.PLUS, it));
            }
            else if (it.equals("-")) {
                tokens.add(new Token(TokenType.MINUS, it));
            }
            else if (it.equals("/")) {
                tokens.add(new Token(TokenType.SLASH, it));
            }
            else {
                throw new Exception("Invalid character: " + it);
            }
        }

        return tokens;
    }

    /**
    * Return the result of applying the operation between 'x' and 'y'
    * @param x first operand (real number)
    * @param y second operand (real number)
    * @return operation result (real number)
    */
    public static Float applyOperation(Float x, Float y, String OP) {
        if (OP.equals("*")) {
            return x * y;
        }
        else if (OP.equals("+")) {
            return x + y;
        }
        else if (OP.equals("-")) {
            return x - y;
        }
        else {
            return x / y;
        }
    }

    /**
    * Return the result after scanning all the tokens
    * @param tokens list of tokens
    * @return scanning result (real number)
    */
    public static Float scanning(List<Token> tokens) {
        Regex validator = new Regex();
        Stack<Float> RPNStacker = new Stack<>();
        while (!tokens.isEmpty()) {
            Token curr = tokens.remove(0);
            String it = curr.lexeme;
            TokenType tp = curr.type;

            if (tp == TokenType.NUM) {
                RPNStacker.add(Float.parseFloat(it));
            }
            else if (validator.isOP(it)) {
                Float y = RPNStacker.pop();
                Float x = RPNStacker.pop();

                RPNStacker.add(applyOperation(x, y, it));
            }
        }

        return RPNStacker.pop();
    }

    /**
    * Return the result after tokenization and scanning steps
    * @param filepath path of the file to read
    * @return postfix operations result (real number)
    */
    public static Float postfix(String filepath) throws Exception {
        List<Token> tokens = tokenization(Files.readAllLines(Paths.get(filepath)));
        Float result = scanning(tokens);
        
        return result;
    }

    public static void main(String[] args) throws Exception {
        Float valid_result = postfix("Calc3.stk");
        System.out.println(valid_result);

        Float invalid_result = postfix("Calc3-exception.stk");
        System.out.println(invalid_result);
    }
}