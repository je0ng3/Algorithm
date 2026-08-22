import java.util.*;

class Solution {
    static class Job {
        int start;
        int length;
        Job(int start, int length) {
            this.start = start;
            this.length = length;
        }
    }
    
    public int solution(int[][] jobs) {
        int answer = 0;
        int n = jobs.length;
        int now = 0;
        int i = 0;
        
        Arrays.sort(jobs, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Job> disk = 
            new PriorityQueue<>((a, b) -> Integer.compare(a.length, b.length));
        while (i<n || !disk.isEmpty()) {
            while (i<n && jobs[i][0] <= now) {
                disk.offer(new Job(jobs[i][0], jobs[i][1]));
                i++;
            }
        
            if (!disk.isEmpty()) {
                Job job = disk.poll();  
                now += job.length;
                answer += now-job.start;
            } else {
                now = jobs[i][0];
            }
        }
    return answer/n;
    }
}