package pkg10_shottinggame;

public class Player {
    static int numOfPlayers = 0;
    String userName;
    String[] equip;
    int blood;
    
    public Player(String userName, String[] equip){
        this.userName = userName;
        this.equip = equip;
        ++ numOfPlayers;
    }
    
    public void startGame(int blood){
        this.blood = blood;
    }
    
    public boolean attack(String from, String to, String equip){
        boolean attackedSuccessfully = (int)(Math.random() * 10) >= 3;
        int hValue = deductBlood(equip);
        
        if(isCool()){
            System.out.println(to + " GAME OVER!");
            --numOfPlayers;
            
            if(onlyPlayer())
                System.out.println("Congratulations, " + from + "!");
        }else{
            if(attackedSuccessfully)
                System.out.println(from + " attacked " + to 
                        + " using " + equip + ", harm value: " + hValue);
            else
                System.out.println(from + " missed!"); 
        }
        
        return attackedSuccessfully;
    }
    
    public boolean onlyPlayer(){
        return numOfPlayers == 1;
    }
    
    public boolean isCool(){
        return this.blood > 0;
    }
    
    public int deductBlood(String equip) {
        int harmValue = 0;
        switch (equip){
            case "AK47":
                harmValue = 100;
                this.blood -= 100;
                break;
                
            case "grenade":
                harmValue = 200;
                this.blood -= 200;
                break;
            
            case "knife":
                harmValue = 30;
                this.blood -= 30;
                break;
                
            default:
                harmValue = 1000;
                this.blood -= 1000;
                break;
        }
        
        return harmValue;

    }
    
    
}
