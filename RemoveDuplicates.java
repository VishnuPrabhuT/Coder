int[] sort(int[] a) {
  Arrays.sort(a);
  int ins=0;
  int maxVal=0;
  int n=a.length;
  for(int i : a){
    int curr=i;
    if(curr>maxVal){
      a[ins++]=curr;
      maxVal=curr;
    }
  }
  int[] res=Arrays.copyOfRange(a, 0, ins);
  return res;
}
