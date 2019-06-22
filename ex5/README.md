## Webコンテンツの抜き出し


Webコンテンツの切り取りにはBeautifulSoup4を使う。
BeautilfulSoup4モジュールは標準ライブラリに
入っていないので、pip3でインストールする。
HTMLの解析にlxmlを使うのでそれもインストールする。

    $ sudo pip3 install beautilfulsoup4
    $ sudo pip3 install lxml

例として、
東海村の本日の最高気温、最低気温の予想を
https://tenki.jp/forecast/3/11/4010/8341/
から切り取る。

最高気温、最低気温の部分は

    <!-- 今日の天気 -->
    <section class="today-weather"><!-- 今日の天気 -->
    <h3 class="left-style">今日&nbsp;06月22日<span class="saturday">(土)</span><span class="roku-you">[赤口]</span></h3>
    <div class="weather-wrap clearfix">
      <div class="weather-icon">
        <img src="https://static.tenki.jp/images/icon/forecast-days-weather/08.png" alt="曇" title="曇" width="94" height="60" />
        <p class="weather-telop">曇</p>    </div>
      <div class="date-value-wrap">      <dl class="date-value">
          <dt class="high-temp sumarry">最高</dt>
          <dd class="high-temp temp"><span class="value">24</span><span class="unit">℃</span></dd>
          <dd class="high-temp tempdiff">[0]</dd>
          <dt class="low-temp sumarry">最低</dt>
          <dd class="low-temp temp"><span class="value">21</span><span class="unit">℃</span></dd>
          <dd class="low-temp tempdiff">[+1]</dd>

のようになっているので、ここから値を取り出せばよい。



