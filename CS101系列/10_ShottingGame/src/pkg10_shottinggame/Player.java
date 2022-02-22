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
    
    public AttackEvent attack(Player to, String equip){
        boolean attackedSuccessfully = (int)(Math.random() * 10) >= 3;
        //In python: return (self, to, equip, attackedSuccessfully)
        return new AttackEvent(this, to, equip, attackedSuccessfully);
    }
    
    public static boolean onlyPlayer(){
        return numOfPlayers == 1;
    }
    
    public boolean isCool(){
        return !(this.blood > 0);
    }
    
    @Override
    public String toString(){
        return userName;
    }
 
}
