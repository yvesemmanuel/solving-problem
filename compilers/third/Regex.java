public class Regex {
	
	
	public static boolean isNum(String token) {
		if (token != null) {
			return token.matches("[0-9]+");
		}

		return false;
	}
	
	public static boolean isOP(String token) {
		if (token != null) {
			return token.matches("\\*|\\-|\\+|\\/]");
		}

		return false;
	}

}
