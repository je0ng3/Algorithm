class Solution {
    public long solution(int n, int[] times) {
        long left = 0;
        
        long right = 0;
        for (int time: times) {
            right = Math.max(right, (long) time);
        }
        right *= n;
        
        long mid = (left + right)/2;
        
        while (left <= right) {
            mid = (left + right)/2;
            
            long count = 0;
            for (int time: times) {
                count += mid/time;
            }
            if (count >= n){
                right = mid-1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}