# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import csv
import subprocess
# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('help')
@listen_to('help')
def help_func(message):
    message.reply('''`pi_name:`あるいは `パイの名前は` と` /boot/mypiname.csv `に記載した名前を入力してIPアドレスを調べる
ロボットの名前がUEC_robotのときの例:
`@ipbot pi_name:UEC_robot`
`@ipbot パイの名前はUEC_robot`
    ''')

# @listen_to('リッスン')
# def listen_func(message):
#     message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#     message.reply('君だね？')
def read_pi_name(filepath="/boot/mypiname.csv"):
    piname = ""
    try:
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                piname = row[0]
            return piname
    except:
        print('Can not get pi name\nPlease check your /boot/mypiname.csv file')
        return 'Can not get pi name\nPlease check your /boot/mypiname.csv'

def sub_exec(command):
    exec_result = subprocess.check_output(command)
    result_decoded = exec_result.decode('utf-8')
    return result_decoded

def get_my_local_ip():
    try:
        ipconfig = sub_exec(["ifconfig"])
        ipconfig = ipconfig.split("\n")
        for i in ipconfig:
            if "inet" in i and "inet6" not in i and '127' not in i:
                return i[i.find('inet'):]
    except:
        print("Error occurred!")
        return "Can not get ip addr!\t学生講師と相談してください"



my_pi_name = read_pi_name()
pi_ip = get_my_local_ip()
print(my_pi_name)

@respond_to("pi_name:"+str(my_pi_name))
@respond_to("piname:"+str(my_pi_name))
@respond_to("パイの名前は"+str(my_pi_name))
def tell_me_ipAddr(message):
    message.reply(my_pi_name+"のIPアドレスは以下のようになります\n"+pi_ip)
