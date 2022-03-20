package statpackage;

/**
 *
 * @author Sam Y
 */

public class ComputeMode {

    private class NumFreqMap{
        int num = 0;
        int freq = 0;
        //Record for numbers of the same frequency, who appears earlier. 
        int timeStamp = 0;
        boolean initialized = false;
    }
    
    private static void intializeMapEle(NumFreqMap map, int num, 
            int timeStamp) {
        map.num = num;
        map.freq = 1;
        map.initialized = true;
        map.timeStamp = timeStamp;
    }
    
    private static void manageCollision(NumFreqMap[] numMap, int num, 
            int timeStamp){
        //It's just a collision element appeared again.
        for(int i = 0; i < numMap.length; i++){
            if(numMap[i].num == num){
                numMap[i].freq += 1;
                return;
            }
        }
        
        //The collision element not yet initialized.
        for(int i = 0; i < numMap.length; i++){
            if(!numMap[i].initialized){
                intializeMapEle(numMap[i], num, timeStamp);
            }
        }
    }
    
    public void initializeMap(NumFreqMap[] map){
        for(int i = 0; i < map.length; i++)
            map[i] = new NumFreqMap();
    }
    
    public static int mode(int[] nums){
        if(nums.length == 0)
            return -1;
        
        ComputeMode funC = new ComputeMode();
        int mapLength = nums.length;
        NumFreqMap[] numMap = new NumFreqMap[mapLength];
        funC.initializeMap(numMap);
          
        for(int i = 0; i < mapLength; i++){
            int loc = Math.abs(nums[i]) % mapLength;
            if(!numMap[loc].initialized)
                intializeMapEle(numMap[loc], nums[i], i);
            else if(numMap[loc].num == nums[i] && numMap[loc].initialized)
                numMap[loc].freq += 1;
            else
                manageCollision(numMap, nums[i], i);
        }
         
        int modeNum = 0, freq = 0, timeStamp = 0;
        for(NumFreqMap map : numMap){
            if(map.freq > freq){
                freq = map.freq;
                modeNum = map.num;
                timeStamp = map.timeStamp;
            }else if(map.freq == freq){
                if(map.timeStamp < timeStamp){
                    freq = map.freq;
                    modeNum = map.num;
                    timeStamp = map.timeStamp;
                }
            }
        }
        
        return modeNum;
                
    }
    
}
