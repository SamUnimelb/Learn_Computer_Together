package pkg11_gottenbankproject;

/**
 *
 * @author TR
 */
public class BankAccount {
    private String accountID;
    private double amount;
    
    public BankAccount(String accountID, double amount){
        this.accountID = accountID;
        this.amount = amount;
    }
    
    public double getAmount(){
        return amount;
    }
    
    public void deposit(double howMuch){
        amount += howMuch;
    }
    
    public void takeMoney(double howMuch){
        if(howMuch > 1000)
            System.out.println("Too much! Please go to counter to take this!");
        else{
            amount -= howMuch;
            System.out.println(howMuch + " took from your account!");
        }
            
      
    }
    
}
