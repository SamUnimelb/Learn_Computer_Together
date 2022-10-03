package methoddemo;

/**
 *
 * @author Sam_Yan
 */
public class Point {
    private double x;
    private double y;
    
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }
    
    public void setX(double x){
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }
    
    @Override
    public String toString(){
        return "Point is: (" + this.x + ", " + this.y + "). ";
    }
}
