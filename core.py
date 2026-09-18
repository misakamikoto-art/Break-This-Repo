import random
import time
w_reason=0.3
s_reason=0.7
m_reason=0.5
def get_ui_screen(w_final, s_final, m_final):
    return f"""
    +---------------------+           +---------------------+
    |                     |           |                     |
    |      MELCHIOR-1     |           |     BALTHASAR-2     |
    |{s_final:^21}|-----------|{m_final:^21}|
    |                     |           |                     |
    |                     |           |                     |
    +---------------------+           +---------------------+
                 \\                               /
                  \\                             /
                   \\                           /
                    \\                         /
                     \\                       /
                      +---------------------+
                      |                     |
                      |      CASPER-3       |
                      |{w_final:^21}|
                      |                     |
                      |                     |
                      +---------------------+
"""
def start(high):
    s_final='In progress'
    m_final='In progress'
    w_final='In progress'
    w_emotion=random.uniform(0.5,high)
    s_emotion=random.uniform(0.7,high)
    m_emotion=random.uniform(0,high)
    w=w_emotion*w_reason
    s=s_emotion*s_reason
    m=m_emotion*m_reason
    print('magi思考中...')
    for women in range(0,101,1):
        time.sleep(0.02)
        bar1=women*'/'+(100-women)*' '
        print(f'\r 女人[{bar1}]{women}%', end='', flush=True)
    if w>0.2*high or w==0.2*high:
        w_final='Approved'
    else:
        w_final='Rejected'
    get_ui_screen(w_final, s_final, m_final)
    print(get_ui_screen(w_final, s_final, m_final), end='', flush=True)
    print()
    for scientist in range(0,101,1):
        time.sleep(0.02)
        bar2=scientist*'/'+(100-scientist)*' '
        print(f'\r 科学家[{bar2}]{scientist}%', end='', flush=True)
        if s>0.2*high or s==0.2*high:
            s_final='Approved'
        else:
            s_final='Rejected'
    print(get_ui_screen(w_final, s_final, m_final), end='', flush=True)
    print()
    for mother in range(0,101,1):
        time.sleep(0.02)
        bar3=mother*'/'+(100-mother)*' '
        print(f'\r 母亲[{bar3}]{mother}%', end='', flush=True)
    if m>0.2*high or m==0.2*high:
        m_final='Approved'
    else:
        m_final='Rejected'
    print(get_ui_screen(w_final, s_final, m_final), end='', flush=True)
    print()
    return w_final, s_final, m_final,w,s,m
##已完
##革命还未结束，战斗任需继续
