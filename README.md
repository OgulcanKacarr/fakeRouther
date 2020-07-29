# fakeRouther

## Amaç

Merhaba,<br/> bu program ile kendiniz bir şifresiz wifi yayını yayacaksınız.<br/> Böylece sizin yaydığınız wifi ağına bağlanan tüm kullanıcıların internnete yaptığı aramaları "wireshark" üzerinden izleyebileceksiniz.<br/>

## Ayar
öncelikle dns.conf dosyasında "interface" kısmının "wlan0" olup olmadığını kontrol ediniz. Bu kısım sizin interface ile aynı olmak zorunda.<br/><br/>
<br/>![MainMenu](https://github.com/OgulcanKacarr/fakeRouther/blob/master/Images/dnsmasq.png)

Daha sonra hostapd.conf dosyasında ise "ssid" kısmına yaymak istediğiniz wifi ismi'ni giriniz.<br/> Bunları kontrol ettikten sonra yapmanız gereken tek şey;<br/>
"python3 fakeRouther.py" komutu ile programı çalıştırmak olacaktır. İyi günler :)<br/><br/>
<br/>![MainMenu](https://github.com/OgulcanKacarr/fakeRouther/blob/master/Images/hostapd.png)
