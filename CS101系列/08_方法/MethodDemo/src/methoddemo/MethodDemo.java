package methoddemo;

public class MethodDemo {

    static int passByVal(int val) { //Pass by value
        val = 888;
        return val;
    }

    static int passByVal(int val1, int val2) {
        return val1 + val2;
    }

    static double passByVal(double val1, double val2) {
        return val1 * val2;
    }
    
    static void passByRef(Point p){
        p.setX(1.0);
        p.setY(1.0);
    }

    public static void main(String[] args) {
        int num = 123;
        passByVal(num);
        System.out.printf("num after pass by val is %d\n", num);
        System.out.println("Number added by 100 is: " + passByVal(num, 100));
        System.out.println("Number times 2.5 is: " + passByVal(num * 1.0, 2.5));
        
        Point pt = new Point(0, 0);
        passByRef(pt);
        System.out.println(pt);
    }

}
