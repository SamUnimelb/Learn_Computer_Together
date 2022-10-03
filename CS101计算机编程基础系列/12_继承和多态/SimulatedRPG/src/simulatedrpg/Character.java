package simulatedrpg;

/**
 *
 * @author TR
 */
public class Character {
    private String name;
    private char gender;
    private int age;
    
    //ganster表示RPG游戏中人物所属门派/组织
    private String ganster;
    
    public Character(String name, char gender, int age, String ganster){
        this.name = name;
        this.gender = gender;
        this.age = age;
        this.ganster = ganster;
    }
    
    public String getName(){
        return name;
    }
    
    public char getGender(){
        return gender;
    }
    
    public int getAge(){
        return age;
    }
    
    public String getGanster(){
        return ganster;
    }
    
    
    
}
