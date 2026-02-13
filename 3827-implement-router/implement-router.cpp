class Router {
private:
    struct Packet {
        int source, destination, timestamp;
    };

    int memoryLimit;
    queue<Packet> q;
    unordered_set<string> seen;
    unordered_map<int, vector<int>> mp;

    string makeKey(int s, int d, int t) {
        return to_string(s) + "#" + to_string(d) + "#" + to_string(t);
    }

public:
    Router(int memoryLimit) {
        this->memoryLimit = memoryLimit;
    }

    bool addPacket(int source, int destination, int timestamp) {
        string key = makeKey(source, destination, timestamp);

        if (seen.count(key)) return false;

        // Remove oldest if memory full
        if (q.size() == memoryLimit) {
            Packet old = q.front();
            q.pop();

            string oldKey = makeKey(old.source, old.destination, old.timestamp);
            seen.erase(oldKey);

            // Remove timestamp from mp
            auto &vec = mp[old.destination];
            vec.erase(lower_bound(vec.begin(), vec.end(), old.timestamp));
        }

        Packet p = {source, destination, timestamp};
        q.push(p);
        seen.insert(key);
        mp[destination].push_back(timestamp);

        return true;
    }

    vector<int> forwardPacket() {
        if (q.empty()) return {};

        Packet p = q.front();
        q.pop();

        string key = makeKey(p.source, p.destination, p.timestamp);
        seen.erase(key);

        auto &vec = mp[p.destination];
        vec.erase(lower_bound(vec.begin(), vec.end(), p.timestamp));

        return {p.source, p.destination, p.timestamp};
    }

    int getCount(int destination, int startTime, int endTime) {
        if (!mp.count(destination)) return 0;

        auto &vec = mp[destination];

        auto left = lower_bound(vec.begin(), vec.end(), startTime);
        auto right = upper_bound(vec.begin(), vec.end(), endTime);

        return right - left;
    }
};
