package Java;
import java.util.Stack;

public class stack {
    public static void main(String[] args) {

        // stack = LIFO data structure. Last-In First-Out
        //         stores objects into a sort of "vertical tower"
        //         push() to add to the top
        //         pop() to remove from the top

        // uses of stacks?
        // 1. undo/redo features in text editors
        // 2. moving back/forward through browser history
        // 3. backtracking alogrithms (maze, file directories)
        // 4. calling functions (cal)

        Stack<String> stack = new Stack<String>();

        stack.push("Minecraft");
        stack.push("Skyrim");
        stack.push("DOOM");
        stack.push("Borderlands");
        stack.push("FFVII");

        // stack.pop();
        // stack.pop();
        
        // String myFavGame = stack.pop();
        // System.out.println(myFavGame);

        // System.out.println(stack.empty());
        
        // System.out.println(stack.peek());
        // System.out.println(stack);

        System.out.println(stack.search("FFVII"));
        System.out.println(stack.search("Minecraft"));
        System.out.println(stack.search("Fallout76"));

        // for(int i = 0; i < 1000000000; i++){
        //     stack.push("Fallout76");
        // }
    }
}
