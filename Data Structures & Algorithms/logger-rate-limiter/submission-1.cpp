class Logger {
private:
    unordered_map<string, int> msg_dict;

public:
    Logger() {
        
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if (this->msg_dict.find(message) == this->msg_dict.end()){
            this->msg_dict[message] = timestamp;
            return true;
        }
        int old_timestamp = this->msg_dict[message];
        if (timestamp - old_timestamp >= 10) {
            this->msg_dict[message] = timestamp;
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
