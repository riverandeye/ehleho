import platform, subprocess

applescript = """
display dialog "되로 끝나는 단어나 문장은 없습니다." ¬
with title "맞춤법을 지키는 좋은 하루 되세요 :)" ¬
with icon stop ¬
buttons {"OK"}
"""

def do_alert():
    # If current operating system is Mac OS X, open dialog
    if platform.system() == 'Darwin':
        subprocess.call("osascript -e '{}'".format(applescript), shell=True)