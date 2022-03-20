//Manage package name according to your specific req.
package statpackage;

/**
 *
 * @author TR
 */
public class StatPackage {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println(ComputeMode.mode(new int[]{}));
        System.out.println(ComputeMode.mode(new int[]{1}));
        System.out.println(ComputeMode.mode(new int[]{1, 2, 3, 3}));
        System.out.println(ComputeMode.mode(new int[]{6, 3, 6, 6, 5, 9, 5}));
        System.out.println(ComputeMode.mode(new int[]{1, 1, 2, 3, 3, 9, 5}));
        System.out.println(ComputeMode.mode(new int[]{5, 4, 4, 3, 2, 2, 1}));
    }
    
}
