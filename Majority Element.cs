public class Solution {
    public int MajorityElement(int[] nums) {
        string s = string.Empty;
            
            int ans=0;
            Hashtable sl = new Hashtable();
            foreach (int i in nums)
            {
                if (!sl.ContainsKey(i))
                {
                    
                    sl.Add(i, 1);
                }
                else
                {
                    Console.WriteLine(i);
                    sl[i] = Convert.ToInt32(sl[i])+1;
                }
                if(Convert.ToInt32(sl[i])>nums.Length/2){
                    ans=i;
                    break;
                }
            }
            return ans;
        }
    }
