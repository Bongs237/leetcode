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
        if (queue1.empty()) {
            while (!queue2.empty()) {
                int front = queue2.front();
                queue2.pop();
                queue1.push(front);
            }
        }
        
        while (queue1.size() > 1) {
            int front = queue1.front();
            queue1.pop();
            queue2.push(front);
        }
        int ret = queue1.front();
        queue1.pop();
        return ret;
    }
    
    int top() {
        if (queue1.empty()) {
            while (!queue2.empty()) {
                int front = queue2.front();
                queue2.pop();
                queue1.push(front);
            }
        }

        int front;
        while (!queue1.empty()) {
            front = queue1.front();
            queue1.pop();
            queue2.push(front);
        }
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