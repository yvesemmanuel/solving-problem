public class Regex {
    private static final String NUM_REGEX = "(\\d)+";
    private static final String OP_REGEX = "(\\+|-|\\*|/)";
    private static final String PLUS_REGEX = "(\\+)";
    private static final String MINUX_REGEX = "(\\-)";
    private static final String STAR_REGEX = "(\\*)";
    private static final String SLASH_REGEX = "(/)";
    private static final String ID_REGEX = "[a-z]"; // for id recognition


    public static boolean isNum(String token) {
        return token.matches(NUM_REGEX);
    }

    public static boolean isOP(String token) {
        return token.matches(OP_REGEX);
    }

    public static boolean isPlus(String token) {
        return token.matches(PLUS_REGEX);
    }

    public static boolean isMinus(String token) {
        return token.matches(MINUX_REGEX);
    }

    public static boolean isStar(String token) {
        return token.matches(STAR_REGEX);
    }

    public static boolean isSlash(String token) {
        return token.matches(SLASH_REGEX);
    }

    public static boolean isId(String token) {return token.matches(ID_REGEX);}

    public static TokenType getTokenType(String token) {
        TokenType tokenType = null;
        if(isPlus(token))
            tokenType = TokenType.PLUS;
        else if(isMinus(token))
            tokenType = TokenType.MINUS;
        else if(isStar(token))
            tokenType = TokenType.STAR;
        else if(isSlash(token))
            tokenType = TokenType.SLASH;
        else
            tokenType = TokenType.NUM;

        return tokenType;
    }
}