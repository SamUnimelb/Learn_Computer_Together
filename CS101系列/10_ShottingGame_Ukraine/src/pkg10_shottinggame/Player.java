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
        //加入扣血指数，范围从伤害值的0.2-1.7（不含），增加了很大不确定性
        double attackedHarmRate = Math.random() * 1.5 + 0.2;
        //In python: return (self, to, equip, attackedSuccessfully)
        return new AttackEvent(this, to, equip, attackedHarmRate);
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
