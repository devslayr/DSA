package Java;
import java.util.Queue;
import java.util.LinkedList;

public class queue {
    public static void main(String[] args) {
        
        // Queue = FIFO data structure. First-In First_out (ex. A line of people)
        //         A collection designed for holding elements prior to processing
        //         Linear data structure

        //         add    = enqueue, offer()
        //         remove = dequeue, poll()

        Queue<String> queue = new LinkedList<String>();

        // System.out.println(queue.isEmpty());
        
        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Steve");
        queue.offer("Harold");

        // System.out.println(queue.isEmpty());
        // System.out.println(queue.size());
        System.out.println(queue.contains("Harold"));

        // System.out.println(queue.peek());
        // queue.poll();
        // queue.poll();
        

        System.out.println(queue);

        // Where are queues useful?
        // 1. Keyboard Buffer (letters should appear on the screen in the orderr they're pressed)
        // 2. Printer Queue (Print jobs should be completed in order)
        // 3. Used in LinkedLists, PriorityQueues, Breadth-first search
    }
}
