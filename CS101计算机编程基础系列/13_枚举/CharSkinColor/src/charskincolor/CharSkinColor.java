package charskincolor;

/**
 *
 * @author TR
 */
public class CharSkinColor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Character police = new Character("Tom", "警察", SkinColor.BLACK);
        System.out.println(police);
        
        Character changqing = new Character("徐长卿", "大侠", SkinColor.WHITE);
        System.out.println(changqing);
    }
    
}
