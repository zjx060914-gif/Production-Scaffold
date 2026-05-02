class LongReasoningAgent:
    def __init__(self, docs, memory):
        self.docs = docs
        self.memory = memory

    def run(self):
        # TODO: delta detection, anomaly scoring, confidence rating
        return {
            "key_changes": [],
            "financial_anomalies": [],
            "confidence": 0.75
        }