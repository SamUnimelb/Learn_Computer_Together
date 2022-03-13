package charskincolor;

/**
 *
 * @author TR
 */
public class Character {
    private String name;
    private String role;
    private SkinColor sc;
    
    public Character(String name, String role, SkinColor sc){
        this.name = name;
        this.role = role;
        this.sc = sc;
    }
    
    @Override
    public String toString(){
        return name + ", role: " + this.role + " , skin: " + sc.getColor();
    }
    
}
