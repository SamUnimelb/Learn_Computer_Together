package pkg11_gottenbankproject;

/**
 *
 * @author TR
 */
public class BankAccount {
    private String accountID;
    private double amount;
    private Logger logger;
    
    public BankAccount(String accountID, double amount){
        this.accountID = accountID;
        this.amount = amount;
    }
    
    public String getAccountID(){
        return accountID;
    }
    
    public double getAmount(){
        logger = new Logger(this.accountID + " checked balance!");
        return amount;
    }
    
    public void deposit(double howMuch){
        amount += howMuch;
        logger = new Logger(this.accountID + " deposited " + howMuch + ".");
    }
    
    public void takeMoney(double howMuch){
        if(howMuch > 1000){
            System.out.println("Too much! Please go to counter to take this!");
            logger = new Logger(this.accountID + 
                    " tried to take money but failed. ");
        } else{
            amount -= howMuch;
            System.out.println(howMuch + " took from your account!");
            logger = new Logger(howMuch + " took from " + this.accountID + "!");
        }
            
      
    }
    
}
