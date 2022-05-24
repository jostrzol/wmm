<div style="padding: 2% 5%;">

<h1 style="text-align: center;">
<div style="color:grey; font-size: 0.6em;">Jakub Ostrzołek</div>
<!-- TODO: tytuł -->
<div>WMM - lab. 3 - dźwięk, </div>
</h1>

## Zadanie 1
Przy oryginalnym filtrze dźwięk gitary był mocniejszy i bardziej pełny. Po zadanej filtracji, tak jak napisano w instrukcji, stał się lżejszy i bardziej "dzwoniący". Wynika to z faktu, że zostały wycięte niskie tony (stąd dźwięk mniej pełny), a podbite tony wysokie (stąd mocniejsze "dzwonienie").

## Zadanie 2
### Pogłos
#### Lektor
Głos lektora przy splocie z odpowiedzią impulsową "Vocal room" 40% jest wyraźny i brzmi naturalnie. Natomiast przy splocie z odpowiedzią impulsową "Big vocal hall" 80% głos jest trudno zrozumiały, a efekt echa jest tak mocny, że aż brzmi nienaturalnie.

Spadek w poziomie wyraźności mowy jest spowodowany nakładaniem się w danym momencie próbek pochodzących z poprzednich momentów, przez co głos brzmi "rozmycie" i trudno zidentyfikować poszczególne fonemy. Jak nazwa wskazuje, odpowiedź impulsowa "Big vocal hall" została z pewnością nagrana w większym pomieszczeniu niż "Vocal room", a więc efekt echa musiał tam być mocniejszy i dłuższy. Oprócz tego zwiększenie DRY/WET dwukrotnie również spotęgowało zaobserwowany efekt, ponieważ waga przy sumowaniu wersji z pogłosem w stosunku do oryginału była większa.

#### Chór
Nagranie chóru brzmiało dla mnie "kościelnie", dlatego wybrałem odpowiedź impulsową "Hall/Cathedral", a DRY/WET ustawiłem na ok. 30%.

Po dodaniu pogłosu, chór brzmiał pełniej i jeszcze bardziej "kościelnie". Odniosłem wrażenie, jakby składał się z większej liczby osób niż w oryginale. Wrażenie to może wynikać z faktu, że naturalnie im większy chór, tym trudniej idealnie się zsynchronizować. Dlatego po wprowadzeniu pogłosu, który rozmywa każdy dźwięk w czasie, występuje omawiany efekt.

### Kompresja dynamiki
Orygninał
![](drums_unfreezed.png)

Freezed
![](drums_freezed.png)

Jak słychać i widać na wykresie sygnału, po użyciu kompresora pierwsza połowa nagrania została bardziej wzmocniona niż druga. Oprócz tego chwile między uderzeniami w talerze w drugiej części nagrania zostały bardziej wzmocnione niż same uderzenia w talerze.

Zadaniem kompresora jest tłumienie głośniejszych sygnałów, a zatem w wyniku jego działania zmniejsza się różnica natężenia dźwięku między cichymi a głośnymi momentami w nagraniu. Oprócz tego make-up został tak dobrany, żeby kompresor zamiast po prostu ściszać głośne sygnały, to efektywnie wzmacniał ciche sygnały, a głośne zostawiał praktycznie nienaruszone. Stąd wynikają zaobserwowane efekty.

Efekt ten jest przydatny np. w branży reklamy telewizyjnej. Z oczywistych powodów twórcy reklam chcą odtwarzać swoje reklamy jak najgłośniej, jednak nie mogą przekroczyć pewnego limitu natężenia dźwięku narzuconego ustawowo. Jeżeli po prostu wzmocniliby nagranie, to nie wykorzystaliby limitu natężenia dźwięku przez cały czas trwania reklamy, ponieważ naturalnie w nagraniu występują chwile cichsze i głośniejsze. Dlatego przed wzmocnieniem, nagranie przepuszczane jest przez kompresor, aby wyrównać głośności w całym nagraniu i maksymalnie wykorzystać limity natężenia dźwięku.

## Zadanie 3
Kierunek dźwięku w płaszczyźnie azymutu jest głównie wyznaczany na podstawie różnicy w czasie pomiędzy sygnałem odbieranym z prawego ucha, a sygnałem odbieranym z ucha lewego.

Jednak sam ten efekt nie wystarcza do dokładnej lokalizacji źródła dźwięku, ponieważ jedna wartość różnicy w czasie na tych dwóch kanałach określa 2 półproste, z których może dochodzić dźwięk, a nie 1. Dlatego człowiek wspomaga się drugim mechanizmem - zmienną charakterystyką wrażliwości ucha na dane częstotliwości w zależności od położenia jego źródła (np. dźwięki dochodzące bezpośrednio z tyłu będą miały bardziej przytłumione wysokie tony niż te, dochodzące z przodu). Dokładny przebieg tej charakterystyki jest zmienny dla każdego człowieka i zależy m.in. od kształtu uszu.

Drugi mechanizm jest również wykorzystywany przy namierzaniu źródła dźwięku w płaszczyźnie elewacji i jest to jedyny mechanizm działający w tej płaszczyźnie.

Z powyższych zależności wynika, że najłatwiej będzie rozpoznać, czy dźwięk dochodzi z prawej czy z lewej strony, trochę trudniej czy dźwięk dochodzi z przodu czy z tyłu, a najtrudniej będzie określić kąt elewacji źródła dźwięku. Moje obserwacje potwierdzają te zależności.

Na trudność w lokalizacji dźwięku wpływa też fakt, że, jak wcześniej wspomniałem, każdy posiada inną charakterystykę wrażliwości na konkretne częstotliwości w zależności od kierunku dochodzenia dźwięku. A zatem nie istnieje model symulacji tego wrażenia, który sprawdzałby się idealnie dla wszystkich. W rzeczywistości wykorzystuje się uśrednione modele, opracowane po zmierzeniu tej charekterystyki wielu osobom.

## Zadanie 4
### OSC1/OSC2
Kanał OSC1 daje niższy ton niż kanał OSC2. Na obu kanałach da się usłyszeć charakterystyczną, agresywną barwę fali kwadratowej. Złączenie obu kanałów daje dużo bardziej interesujący i mniej agresywny dźwięk niż każdy z kanałów osobno.

### Obwiednia
Obwiednia kontroluje zachowanie filtra w czasie - im wyżej jest punkt na obwiedni tym więcej wyższych tonów słychać w danym momencie i vice versa. Dla każdego granego dźwięku przebieg jest odtwarzany od nowa oraz jest on zapętlony.

### Ścieżka 2
Tutaj słychać łagodniejsze od fal kwadratowych fale typu sawtooth, a przebieg czasowy charakterystyki filtra jest dużo wolniejszy. Zastosowałem preset "ARP 2050 Punk TAL", który zgodnie z nazwą dodaje pankowego klimatu do syntezatora.

Podobało mi się takie brzmienie, więc zamiast zmieniać melodię tej ścieżki, to dodalem nową ścieżkę (5) wraz z instrumentem oraz nową melodią.

### Ścieżka 3
Na tę ścieżkę wybrałem preset "BS Bass Deep TAL".

Wzmacniacz:
* Za pomocą pokrętła GAIN ustalany jest poziom natężenia dźwięku wchodzącego do wzmacniacza. Jego zmiana wpływa na barwę brzmienia dźwięku, ale nie moduluje bezpośrednio natężenia dźwięku wychodzącego ze wzmacniacza.
* Pokrętło DRIVE reguluje poziom przesteru. Ustawienie tego pokrętła w pozycję minimalną daje nam czysty dźwięk basu z syntezatora, a podkręcanie go sprawia że brzmienie jest coraz bardziej agresywne, robotyczne (coraz bardziej przypominające falę kwadratową).
* Pokrętła BASS, MID i TREBLE pozwalają regulować poziom odpowiednio niskich, średnich i wysokich tonów.
* Pokrętło TONE zmienia barwę dźwięku. Tym mocniejsze jest wycinanie wysokich tonów, im bliżej pokrętło jest wartości 0%.
* Pokrętło VOLUME reguluje poziom natężenia dźwięku wychodzącego ze wzmacniacza bez zmiany jego barwy (oczywiście dopóki sygnał na wyjściu nie staje się przesterowany).

### Ścieżka 4
Na tę ścieżkę wybrałem preset "Nice Studio Kit", ponieważ brzmi on dosyć surowo w porównaniu z innymi presetami, co pasuje do piosenki.

Do ścieżki dodałem m.in. tomy zaraz przed połową utworu oraz talerze w niektórych miejscach.

Kompresor:
* Kręcąc pokrętłem COMPRESS w lewo zmniejszamy poziom kompresji głośnych dźwięków, a w prawo zwiększamy.
* Suwak TIME CONSTANTS pozwala ustalić, czy kompresor będzie szybko reagował na zmiany głośności, czy wolno. Jego działanie widać po prędkości wskazówki (szczególnie przy pierwszym werblu - po dźwięku werbla, gdy suwak jest w pozycji FAST, wskazówka szyciej wraca na pozycję 0, niż gdy suwak jest w pozycji SLOW).
* Pokrętłem MAKE-UP regulujemy wzmocnienie na wyjściu z kompresora.

Uznałem, że do piosenki pasuje mocna kompresja perkusji, dlatego ustawiłem pokrętło COMPRESS na ok. 36, MAKE-UP na 24, a TIME CONSTANTS na FAST.



</div>