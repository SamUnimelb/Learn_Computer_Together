package simulatedrpg;

/**
 *
 * @author TR
 */
public class XianjianCharacter extends Character{
    
    public XianjianCharacter(String name, char gender, int age) {
        this(name, gender, age, "仙剑人物");
    }
    
    public XianjianCharacter(String name, char gender, int age, String gang) {
        super(name, gender, age, gang);
    }
    
    @Override
    public String toString(){
        return "游戏人物名称：" + this.getName() + "，所属剧情：" + this.getGanster();
    }
    
}
