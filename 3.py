#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

struct Client {
    int arrival_time;
    int service_time;
    int window_id;
};

struct Window {
    int id;
    int free_time;
    

    bool operator>(const Window& other) const {
        return free_time > other.free_time;
    }
};

void simulate_bank(int windows_count, int service_time_per_client) {
    std::queue<Client> client_queue;
    std::priority_queue<Window, std::vector<Window>, std::greater<Window>> windows;
    
    for (int i = 0; i < windows_count; ++i) {
        windows.push({i, 0});
    }
    
    int total_wait_time = 0;
    int clients_served = 0;
    int max_queue_length = 0;
    std::vector<int> window_busy_time(windows_count, 0);
    int current_time = 0;
    int next_client_id = 1;
    
    const int SIMULATION_TIME = 100; // минут
    
    for (int time = 0; time < SIMULATION_TIME; ++time) {
        Client new_client = {time, service_time_per_client, -1};
        client_queue.push(new_client);
        
        max_queue_length = std::max(max_queue_length, (int)client_queue.size());
        
        while (!windows.empty() && windows.top().free_time <= time) {
            Window free_window = windows.top();
            windows.pop();
            
            if (!client_queue.empty()) {
                Client current_client = client_queue.front();
                client_queue.pop();
                
                int wait_time = time - current_client.arrival_time;
                total_wait_time += wait_time;
                clients_served++;
                
                window_busy_time[free_window.id] += service_time_per_client;
                
                free_window.free_time = time + service_time_per_client;
                windows.push(free_window);
            } else {
                windows.push(free_window);
            }
        }
    }
    
    std::cout << "=== Результаты симуляции ===" << std::endl;
    std::cout << "Всего окон: " << windows_count << std::endl;
    std::cout << "Время обслуживания клиента: " << service_time_per_client << " мин" << std::endl;
    std::cout << "Обслужено клиентов: " << clients_served << std::endl;
    
    if (clients_served > 0) {
        double avg_wait_time = static_cast<double>(total_wait_time) / clients_served;
        std::cout << "Среднее время ожидания: " << avg_wait_time << " мин" << std::endl;
    }
    
    std::cout << "Максимальная длина очереди: " << max_queue_length << std::endl;
    
    std::cout << "\nЗагрузка окон:" << std::endl;
    for (int i = 0; i < windows_count; ++i) {
        double utilization = static_cast<double>(window_busy_time[i]) / SIMULATION_TIME * 100;
        std::cout << "Окно " << i + 1 << ": " << utilization << "%" << std::endl;
    }
}

int main() {
    std::cout << "Задача 1. RLE-архиватор" << std::endl;
    std::string original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB";
    std::string compressed = compress_rle(original);
    std::string decompressed = decompress_rle(compressed);
    
    std::cout << "Исходная: " << original << std::endl;
    std::cout << "Сжатая: " << compressed << std::endl;
    std::cout << "Восстановленная: " << decompressed << std::endl;
    std::cout << std::endl;
    
    std::cout << "Задача 2. Итератор простых чисел" << std::endl;
    PrimeIterator primes(30);
    for (int p : primes) {
        std::cout << p << " ";
    }
    std::cout << std::endl << std::endl;
    
    std::cout << "Задача 3. Симуляция банка" << std::endl;
    simulate_bank(3, 5); // 3 окна, 5 минут на клиента
    
    return 0;
}
