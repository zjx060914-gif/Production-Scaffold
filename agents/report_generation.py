class ReportGenerationAgent:
    def __init__(self, company, signals):
        self.company = company
        self.signals = signals

    def run(self):
        return f"""
# {self.company} 投研自动分析初稿

## 核心判断
- 系统识别到若干值得关注的变化

## 关键变化
{self.signals}

## 风险提示
- 本报告为 AI 自动生成初稿
"""