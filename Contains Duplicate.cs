public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Hashtable h=new Hashtable();
        foreach(int i in nums){
            if(!h.ContainsKey(i)){
                h.Add(i,0);
            }
            if(Convert.ToInt32(h[i])>=1){
                return true;
            }
            else{
                int x=Convert.ToInt32(h[i])+1;
                h[i]=x;
            }
        }
        return false;
        }
    }
