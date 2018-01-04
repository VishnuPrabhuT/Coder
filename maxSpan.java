public int maxSpan(int[] nums) {
  HashMap<Integer,Integer> al=new HashMap<Integer,Integer>();
  int maxSpan=0;
  if(nums.length==0){
    return 0;
  }
  for(int i=0;i<nums.length;i++){
    if(!al.containsKey(nums[i])){
      al.put(nums[i],i);
    }
    else{
      int diff=i-al.get(nums[i]);
      if(maxSpan<diff){
        maxSpan=diff;
      }
    }
  }
  return maxSpan+1;
}
