import subprocess

applescript = """
display dialog "되로 끝나는 문장은 없습니다!!" ¬
with title "맞춤법을 지킵시다!" ¬
with icon stop ¬
buttons {"OK"}
"""

subprocess.call("osascript -e '{}'".format(applescript), shell=True)