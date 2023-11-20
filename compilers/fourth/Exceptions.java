public class Exceptions {
    public static class UnexpectedCharacterException extends Exception{
        public UnexpectedCharacterException(String character){ super("Unexpected character: " + character);}
    }
    public static class UnexpectedOperatorException extends Exception {
        public UnexpectedOperatorException(String operator){ super("Unexpected operator: " + operator);}
    }
}
