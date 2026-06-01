class Singleton {
private:
    static Singleton *unique_instance_;
    string value;

    Singleton() {}

public:

    static Singleton *getInstance() {
        if (unique_instance_ == nullptr) {
            unique_instance_ = new Singleton();
        }
        return unique_instance_;        
    }

    string getValue() {
        return value;
    }

    void setValue(string &value) {
        this->value = value;
    }
};

Singleton* Singleton::unique_instance_ = nullptr;