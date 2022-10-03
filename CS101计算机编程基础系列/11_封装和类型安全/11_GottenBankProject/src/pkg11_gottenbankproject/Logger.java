package pkg11_gottenbankproject;

import java.io.*;

/**
 *
 * @author TR
 */
public class Logger {
    private FileWriter writer;
    
    public Logger(String transactionMessage){
        /*
        * For business type, 1 - depoit, 2 - check amount, 3 - take money
        */
        try {
            writer = new FileWriter(new File("logger.txt"), true);
            writer.write(transactionMessage + "\n");
            writer.close();            
        } catch (IOException ex) {
            System.out.println(ex);
        }
    }
    
    
}
