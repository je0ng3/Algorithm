import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int s: scoville) {
            heap.offer(s);
        }
        while (!heap.isEmpty()) {
            int a = heap.poll();
            if (a>=K) {
                break;
            }
            if (heap.isEmpty()) {
                return -1;
            }
            int b = heap.poll();
            int c = a + (b*2);
            heap.offer(c);
            answer++;
        }
        return answer;
    }
}