## Webコンテンツの取得

pythonを使ってWebコンテンツを取得するプログラムを書く。
標準ライブラリのみでも不可能ではないが、requestsモジュールを
使って書くと記述が大幅に簡略化されるので、それを使うことに
する。

    $python3
    >>> import requests (と入力する)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'requests'

といわれたらrequestモジュールが入っていないのでインストールする。

    $ pip3 install requests --user
    (正常にセットされたかどうかインタラクティブシェルを起動して確認する)
    $ python3
    Python 3.7.3 (default, Apr 10 2019, 12:54:05)
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import requests (と入力する)
    >>> (正常ならプロンプト (>>>) のみが表示される。

プログラムは2行だけである。

このあと取得できたhtmlを解析し、必要な部分をとりだしたりして
利用する。htmlの解析にはBeautilfulSoupモジュールを使うことが
できる。BeautilfulSoupモジュールも標準ライブラリには入っていないので
pip3コマンドでセットする。例としてex5で東海村の最高、最低気温の
抜き出しを行う。

