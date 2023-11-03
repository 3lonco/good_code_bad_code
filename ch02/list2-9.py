# Pythonには、Javaのようなstatic final修飾子は存在しません。
# しかし、Pythonでは以下の方法で類似の動作を模倣することができます：
# 
# クラス変数: 
# Pythonのクラス変数は、Javaのstatic変数に似ています。
# 上記のMINやMAXのように、クラスのすべてのインスタンスで共有されます。
# 
# Immutable性: Pythonにはfinalキーワードはありませんが、値の再代入を避けることで、
# 変数を事実上finalのように扱うことができます。
# ただし、これはプログラマーの自己制御に依存するため、強制的には行われません。
# 
# 名前付け規則: 定数を大文字で命名することは、Pythonの慣習です。
# これにより、変数が定数であることを示唆し、再代入しないようにすることが暗黙の了解となっています。

class HitPoint:
    MIN = 0
    MAX = 999

    def __init__(self, value):
        self.value = value




