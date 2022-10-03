//package maindemo;

/**
 *
 * @author TR
 */
import java.io.*;
import java.util.Scanner;

public class MainDemo {

    public static void main(String[] params) {
        Scanner input;
        try {
            input = new Scanner(new File(params[1]));
            while(input.hasNextLine())
                System.out.println(input.nextLine());
        } catch (FileNotFoundException ex) {
            System.out.println(ex);
        }

    }
    
}
