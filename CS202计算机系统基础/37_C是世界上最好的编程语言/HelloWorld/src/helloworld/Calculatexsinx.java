package helloworld;

public class Calculatexsinx {
    public static void main(String[] args) {
        double x = 0.0, fx = 0.0;
        long start = System.currentTimeMillis();
        
        while(x < 10000.0){
            fx = x * Math.sin(x);
            x += Math.pow(2, -8);
        }
        
        long duration = System.currentTimeMillis() - start;
        System.out.println("Time duration: " + duration + " msecs.");
    }
}
