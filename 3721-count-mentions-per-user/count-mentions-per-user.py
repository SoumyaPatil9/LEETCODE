class Solution:
    def countMentions(self, numberOfUsers, events):
        # Sort events:
        # 1) by timestamp
        # 2) OFFLINE before MESSAGE if same timestamp
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers
        
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            
            # Bring users back online first
            for i in range(numberOfUsers):
                if offline_until[i] != 0 and offline_until[i] <= timestamp:
                    offline_until[i] = 0
            
            if event_type == "OFFLINE":
                user_id = int(event[2])
                offline_until[user_id] = timestamp + 60
            
            else:  # MESSAGE
                mention_str = event[2]
                
                if mention_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                
                elif mention_str == "HERE":
                    for i in range(numberOfUsers):
                        if offline_until[i] == 0:
                            mentions[i] += 1
                
                else:
                    for token in mention_str.split():
                        user_id = int(token[2:])
                        mentions[user_id] += 1
        
        return mentions
