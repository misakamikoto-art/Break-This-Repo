import os
from ui import clear_screen,show_banner,declaration
from core import start
from history import init_history,save_record,get_history,show_history,clear_history
from config import load_config,change
from music import music
config = load_config()
max_history = config["history_limit"]
music(config["music_name"],config["music_volume"],config["music_model"])
def question():#start已包含
    q=input(str('question：'))
    if len(q)==0:
        print('question为空')
        print('这样玩会坏掉的口牙')
        the_last=10
    else:
        the_last=len(q)
    w_final, s_final, m_final,w,s,m=start(the_last)
    print('\n' + '=' * 40)
    print('女人',w_final,'决策值',round(w,2)*100)
    print('科学家',s_final,'决策值',round(s,2)*100)
    print('母亲',m_final,'决策值',round(m,2)*100)
    if w_final == 'Approved' and s_final == 'Approved' and m_final == 'Approved':
        print('最终决议：执行')
    else:
        print('最终决议：否决')
    save_record(q,w_final, s_final, m_final,w,s,m)
def mune():
    global max_history
    while True:
        show_banner()
        print('1:向magi提问')
        print('2:展示历史问题')
        print('3:清空历史问题')
        print('4:作者声明')
        print('5:config change')
        print('6:show config')
        print('7:退出')
        choice=input('请选择：')
        if choice=='1':
            question()
            input('\n按回车键继续...')
            clear_screen()
        elif choice=='2':
            show_history(max_history)
            input('\n按回车键继续...')
            clear_screen()
        elif choice=='3':
            clear_history()
            input('\n按回车键继续...')
            clear_screen()
        elif choice=='4':
            clear_screen()
            declaration()
            input('\n按回车键继续...')
            clear_screen()
        elif choice=='5':
            name=input('名称：')
            if name in config and not name=="music_name" and not name=="user_name":
                try:
                    number = int(input('改值：'))
                except ValueError:
                    print('请输入数字')
                change(name,number)
                print(f'已将{name}改为{number}')
                input('\n按回车键继续...')
                clear_screen()
                continue
            elif name=="user_name":
                number = input('改值：')
                change(name,number)
                print(f'已将{name}改为{number}')
                input('\n按回车键继续...')
                clear_screen()
                continue
            else:
                print('键不存在')
                input('\n按回车键继续...')
                clear_screen()
                continue
            clear_screen()
        elif choice=='6':
            print('格式 键 说明 值')
            print(f'user_name用户名:{config["user_name"]}')
            print(f'music_volume音乐音量：{config["music_volume"]}')
            print(f'music_model音乐模式：{config["music_model"]}  0为单次 -1为循环(默认)')
            print(f'history_limit历史记录上线：{config["history_limit"]}')
            input('\n按回车键继续...')
            clear_screen()  
        elif choice=='7':
            break
        else:
            print('此操作不合法')
            input('\n按回车键继续...')
            clear_screen()
if __name__ == "__main__":#主程序
    init_history()
    clear_screen()
    os.system('color 0A')
    mune()
    input('\n按回车键退出...')
#####变量解析 bar1，2，3为显示进度条 w,s,m为决策值 emotion_w,s,m为情感波动 reason_w,s,m为理智 w,s,m_final为最终结果(通过与否) the_last为情感波动上限
