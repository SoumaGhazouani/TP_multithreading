#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <string>
#include <fstream>
#include <nlohmann/json.hpp> // JSON library
#include <cpr/cpr.h>         // cpr library for HTTP requests
#include <Eigen/Dense>       // Eigen library for linear algebra

using json = nlohmann::json; // Alias for convenience

class Task {
public:
    int identifier;
    int size;
    std::vector<std::vector<double>> a;
    std::vector<double> b;
    std::vector<double> x;
    double time;

    Task(int id = 0, int size_param = -1) : identifier(id), time(0.0) {
        size = (size_param == -1) ? randomInt(300, 3000) : size_param;
        a = randomMatrix(size, size);
        b = randomVector(size);
        x.resize(size, 0.0);
    }
    Task(const json& j) {
            identifier = j["identifier"];
            size = j["size"];
            a = randomMatrix(size, size);
            b = randomVector(size);
            x.resize(size, 0.0);
            time = j["time"];
        }

    void work() {
        auto start = std::chrono::high_resolution_clock::now();
        x = solveLinearSystem(a, b);
        auto end = std::chrono::high_resolution_clock::now();
        time = std::chrono::duration<double>(end - start).count();
        std::cout << time << std::endl;
    }

    json to_json() const {
        return {
            {"identifier", identifier},
            {"size", size},
            {"a", a},
            {"b", b},
            {"x", x},
            {"time", time}
        };
    }

    static Task from_json(const std::string& json_str) {
        json j = json::parse(json_str);
        Task task(j["identifier"], j["size"]);
        task.a = j["a"].get<std::vector<std::vector<double>>>();
        task.b = j["b"].get<std::vector<double>>();
        task.x = j["x"].get<std::vector<double>>();
        task.time = j["time"];
        return task;
    }

private:
    static int randomInt(int min, int max) {
        static std::random_device rd;
        static std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(min, max);
        return dis(gen);
    }

    static std::vector<std::vector<double>> randomMatrix(int rows, int cols) {
        std::vector<std::vector<double>> matrix(rows, std::vector<double>(cols));
        for (auto& row : matrix) {
            for (auto& val : row) {
                val = static_cast<double>(rand()) / RAND_MAX;
            }
        }
        return matrix;
    }

    static std::vector<double> randomVector(int size) {
        std::vector<double> vec(size);
        for (auto& val : vec) {
            val = static_cast<double>(rand()) / RAND_MAX;
        }
        return vec;
    }

    static std::vector<double> solveLinearSystem(const std::vector<std::vector<double>>& a, const std::vector<double>& b) {
        int n = a.size();
        Eigen::MatrixXd A(n, n);
        Eigen::VectorXd B(n);

        // Fill Eigen matrices
        for (int i = 0; i < n; ++i) {
            B(i) = b[i];
            for (int j = 0; j < n; ++j) {
                A(i, j) = a[i][j];
            }
        }

        // Solve the system Ax = B using Eigen's solver
        Eigen::VectorXd X = A.colPivHouseholderQr().solve(B);

        // Convert Eigen vector back to std::vector
        return std::vector<double>(X.data(), X.data() + X.size());
    }
};

int main() {
    // GET Request Example
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});
    //std::cout << "GET response: " << r.text << std::endl;

    if (r.status_code == 200) {
        //std::cout << "Response from server:\n" << r.text << std::endl;

        // Parse JSON response
        nlohmann::json json_data = nlohmann::json::parse(r.text);
        //std::cout << "JSON parsed: " << json_data.dump(4) << std::endl;
        std::cout << "test1"<< std::endl;

        // Créer un objet Task à partir de json_data
        Task task(json_data); // Utilisation du constructeur avec json
        std::cout << "test2"<< std::endl;
        task.work();           // Résoudre Ax = b

        //std::cout << "Task computed. Result: " << task.to_json().dump(4) << std::endl;

        // POST Request Example
        cpr::Response postResponse = cpr::Post(
            cpr::Url{"http://localhost:8000"},
            cpr::Body{task.to_json().dump()},
            cpr::Header{{"Content-Type", "application/json"}}
        );

        // Vérifier la réponse du POST
        if (postResponse.status_code == 200) {
            std::cout << "\nPOST Response from server:\n" << postResponse.text << std::endl;
        } else {
            std::cerr << "Failed to send Task data: " << postResponse.error.message << std::endl;
        }
    } else {
        std::cerr << "Failed to connect: " << r.error.message << std::endl;
    }

    return 0;
}
