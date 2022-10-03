package charskincolor;

/**
 *
 * @author TR
 */
public enum SkinColor {
    RED(255, 0, 0),
    GREEN(0, 255, 0),
    BLUE(0, 0, 255),
    BLACK(0, 0, 15),
    WHITE(255, 255, 255);
    
    
    private final int r, g, b;
    SkinColor(int r, int g, int b){
        this.r = r;
        this.g = g;
        this.b = b;
    }

    public SkinColor getColor(){
        return this;
    }
    
}
