import json
import os
from datetime import datetime
HISTORY_FILE = "history.json"
def init_history():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE,'w',encoding='utf-8')as f:
            json.dump([],f,ensure_ascii=False, indent=2)
def save_record(question,w_final, s_final, m_final,w,s,m):

    init_history()
    if w_final == '通过' and s_final == '通过' and m_final == '通过':
        final='通过'
    else:
        final='否决'
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
    record = {
        "id": len(history) + 1,
        "时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "问题": question,
        "女人": {"结果": w_final, "得分": round(w * 100, 1)},
        "科学家": {"结果": s_final, "得分": round(s * 100, 1)},
        "母亲": {"结果": m_final, "得分": round(m * 100, 1)},
        "最终决议": final
    }
    history.append(record)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
def get_history(limit):
    init_history()
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        history = json.load(f)
        if limit and limit > 0:
            return history[-limit:]
    return history
def show_history(max_history):
    history = get_history(max_history)
    if not history:
        print("\n暂无历史记录")
        return
    print("\n" + "=" * 65)
    print("历史决策记录")
    print("=" * 65)
    print(f"{'ID':<4} {'时间':<17} {'问题':<22} {'结果':<6}")
    print("-" * 65)
    for r in reversed(history):
        q = r["问题"][:19] + "..." if len(r["问题"]) > 22 else r["问题"]
        print(f"{r['id']:<4} {r['时间']:<17} {q:<22} {r['最终决议']:<6}")
    print("-" * 65)
    print(f"共 {len(history)} 条记录（显示最近{max_history}条）")
    print("=" * 65)
def clear_history():
    confirm = input("确定要清空所有历史记录吗？(y/n)：")
    if confirm[0] == 'y':
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        print("历史记录已清空")
##已完
##革命还未结束，战斗任需继续
