class MyStack {
private:
    queue<int> queue1;
    queue<int> queue2;
public:
    MyStack() {}
    
    void push(int x) {
        queue1.push(x);
    }
    
    int pop() {
        while (queue1.size() > 1) {
            int front = queue1.front();
            queue1.pop();
            queue2.push(front);
        }
        int ret = queue1.front();
        queue1.pop();

        // Swap references (this is allowed cuz you're not making another object, it's still 2 queues)
        queue<int> temp = queue1;
        queue1 = queue2;
        queue2 = temp;

        return ret;
    }
    
    int top() {
        int front;
        while (!queue1.empty()) {
            front = queue1.front();
            queue1.pop();
            queue2.push(front);
        }

        // Swap references
        queue<int> temp = queue1;
        queue1 = queue2;
        queue2 = temp;

        return front;
    }
    
    bool empty() {
        return queue1.empty() && queue2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */