#include <vector>
#include <algorithm>

class PrimeIterator {
private:
    std::vector<int> primes;
    size_t index;
    int limit;
    
    void generate_primes() {
        if (limit < 2) return;
        
        std::vector<bool> is_prime(limit + 1, true);
        is_prime[0] = is_prime[1] = false;
        
        for (int i = 2; i * i <= limit; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        
        for (int i = 2; i <= limit; ++i) {
            if (is_prime[i]) {
                primes.push_back(i);
            }
        }
    }
    
public:

    using iterator_category = std::input_iterator_tag;
    using value_type = int;
    using difference_type = std::ptrdiff_t;
    using pointer = const int*;
    using reference = const int&;
    
    PrimeIterator(int limit = 0) : limit(limit), index(0) {
        generate_primes();
    }
    

    static PrimeIterator begin(int limit) {
        PrimeIterator it(limit);
        it.index = 0;
        return it;
    }
    
    // end() iterator
    static PrimeIterator end(int limit) {
        PrimeIterator it(limit);
        it.index = it.primes.size();
        return it;
    }
    
    // Операторы для input iterator
    reference operator*() const {
        return primes[index];
    }
    
    pointer operator->() const {
        return &primes[index];
    }
    
    PrimeIterator& operator++() {
        ++index;
        return *this;
    }
    
    PrimeIterator operator++(int) {
        PrimeIterator tmp = *this;
        ++index;
        return tmp;
    }
    
    bool operator==(const PrimeIterator& other) const {
        return index == other.index;
    }
    
    bool operator!=(const PrimeIterator& other) const {
        return !(*this == other);
    }
    
    // Для range-based for loop
    PrimeIterator begin() const {
        PrimeIterator it = *this;
        it.index = 0;
        return it;
    }
    
    PrimeIterator end() const {
        PrimeIterator it = *this;
        it.index = primes.size();
        return it;
    }
};
