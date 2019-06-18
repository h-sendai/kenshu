## Webコンテンツの取得

pythonを使ってWebコンテンツを取得するプログラムを書く。
標準ライブラリのみでも不可能ではないが、requestsモジュールを
使って書くと記述が大幅に簡略化されるので、それを使うことに
する。

    $ sudo pip3 install requests
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
pip3コマンドでセットする。今回は時間の都合でBeautilfulSoupを使った
htmlの解析は行わない。
