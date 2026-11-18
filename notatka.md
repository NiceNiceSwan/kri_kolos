### Do przesyłania informacji o topologii sieci ISIS wykorzystuje pakiety:

1. LSP oraz elementy Internal IP Reachability TLV #128 i IS Reachability TLV #2
2. **LSP oraz elementy Extended IP Reachability TLV #135 i Extended IS Reachability TLV #22**
3. LSP oraz elementy LSP Entry TLV #9
4. LSP oraz elementy IS reachability TLV #2 lub Extended IS Reachability TLV #22

### Wiadomość Router LSA pozwala zidentyfikować:

1. Adres podsieci w przypadku łączy transit
2. adres routera DR
3. **router sąsiedni w przypadku łączy punkt-punkt**

### Wiadomości Router LSA są rozgłaszane:

1. Tylko przez routery ASBR w obrębie obszaru szkieletowego
2. tylko przez routery w obrębie obszaru szkieletowego
3. **tylko w obrębie obszaru do którego należy router będący ich źródłem**
4. tylko przez routery ABR w podległych im obszarach

### Adresowanie multicast GLOP polega na:

1. Użyciu adresów IP o prefiksie 233 i zastąpieniu środkowych bajtów losową wartością
2. użycia adresó IP klasy D i zastąpieniu środkowych bajtów numerem systemu AS operatora
3. użycia adresów IP klasy D i zastąpieniu środkowych bajtów losową wartością
4. **użycia adresów IP o prefiksie 233 i zastąpieniu środkowych bajtów numerem systemu AS operatora**

### Pakiet IS-IS IIH point-to-point Hello zawiera:

1. IS Reachability TLV #2
2. Extended IS Reachability TLV #22
3. **Adjacency State TLV #240**
4. IS Neighbor TLV #6

### Wiadomość Inter-Area-Router LSA służy do:

1. przesyłania informacji o lokalizacji routera ABR pomiędzy obszarami
2. przesyłania informacji o lokalizacji routera ABR wewnątrz obszaru
3. **przesyłania informacji o lokalizacji routera ASBR pomiędzy obszarami**
4. przesyłania informacji o lokalizacji routera ASBR wewnątrz obszaru

### Zasada RPF oznacza, że:

1. pakiety multicast z danego źródła nigdy nie są przesyłane na interfejs RPF
2. pakiety multicast są wysyłane wyłącznie na interfejsy oznaczone jako RPF
3. pakiety multicast nigdy nie są przesyłane na interfejs pełniący rolę interfejsu RPF
4. **pakiety multicast są wysyłane tylko na interfejsy oznaczone jako RPF jeśli przyjdą na interfejs prowadzący do źródła**

### Do dystrybucji adresów sieciowych wewnątrz obszaru protokół OSPFv3 wykorzystuje:

1. **Intra-Area-Prefix LSA**
2. Router LSA
3. Inter-Area-Prefix LSA
4. Network LSA

### W architekturze DiffServ tzw. reguła PHB EF korzysta z:

1. **jednego kodu DSCP**
2. dwunastu kodów DSCP
3. trzech kodów DSCP
4. czterech kodów DSCP

### Zaznacz sekwencję pakietów IS-IS odpowiadającą synchronizacji baz LSDB na łączach punkt-punkt

1. R1 -> CSNP -> R2, R2 -> PSNP -> R1, R1 -> LSP -> R2
2. R1 -> PSPN -> R2, R2 -> LSP -> R1, R1 -> CSPN -> R2
3. R1 -> CSPN -> R2, R1 -> LSP -> R2, R1 -> PSPN -> R2
4. **R1 -> CSNP -> R2, R2 -> LSP -> R1, R1 -> PSPN -> R2**

### Wiadomości Summary LSA typ 3 przekazują:

1. Informacje o lokalizacji róuterów ASBR
2. Informacje o podsieciach dostępnych w tym samym obszarze co router rozgłaszający
3. **informacje o podsieciach dostępnych w innych obszarach niż router rozgłaszający**
4. informacje o lokalizacji routerów ABR

### WFQ jest to:

1. Mechanizm klasyfikacji pakietów IP na brzegu sieci DiffServ
2. Mechanizm zarządzania buforem w routerze IP
3.** mechanizm szeregowania pakietów w routerze IP**
4. mechanizm kontroli pakietów IP w routerze brzegowym DiffServ

### W architekturze DiffServ przypisanie pakietów do klas (klasyfikacja):

1. Odbywa się w aplikacji hosta
2. Odbywa się w routerze szkieletowym
3. **Odbywa się w routerze brzegowym**

### Główną zaletą mechanizmu CIDR jest:

1. obsługa subnetingu adresów sieciowych IP
2. **agregacja adresów IP zwiększająca efektywność routingu hierarchicznego**
3. hierarchizacja formatu adresów IP
4. hierarchizacja topologii sieci IP

### W przypadku źródłowego drzewa multicast pakiety IP komutowane są na podstawie:

1. **adresu źródła oraz adresu grupy multicast**
2. adresu źródła
3. adresu grupy multicast

### W routerze szkieletowym DiffServ sposób kolejkowania pakietu zależy od:

1. **wartości pola DSCP w nagłówku IP pakietu**
2. wyniku analizy pola danych pakietu IP (ang. Deep Packet Inspection)
3. zawartości pola QoS wiersza tablicy routingu odpowiadającego adresowi IP pakietu

### Którą komendą można sprawdzić stan sesji BGP z sąsiadami?

1. **show ip bgp summary**
2. show ip bgp paths
3. show ip community
4. show ip route

### Atrybut CLUSTER_LIST służy do:

1. blokowania tranzytu między określonymi systemami autonomicznymi przez sieć ISP
2. tworzenia konfederacji systemów autonomicznych
3. **wykrywania pętli w systemach autonomicznych wykorzystujących technikę Route Reflector**
4. realizacji połączeń międzyoperatorskich w węzłach IXP

### W sieci MPLS Layer 3 VPN, do sterowania importem prefiksów (ścieżek) do właściwych instancji VRF wykorzystuje się:

1. VRF ID
2. Route Distinguisher
3. **Route Target**
4. Next-hop ID

### Pakiet IPv4 jest przesyłany przez sieć MPLS VPN:

1. z adresami VPNv4 w nagłówku
2. **z dwoma nagłówkami MPLS, zawierającymi etykietę wewnętrzną (VPN) i zewnętrzną (transportową)**
3. z jednym nagłówkiem MPLS, zawierającym globalnie unikalną etykietę, zapewniającą transport we właściwym tunelu i określającą przynależność do sieci VPN
4. z adresami VPNv4 i jednym nagłówkiem, zawierającym etykietę tunelu transportowego

### BGP Community jest to:

1. organizacja zrzeszająca operatorów ISP Tier-1, nadzorująca rozwój protokołu BGP
2. **atrybut ścieżki, wykorzystywany powszechnie do tworzenia reguł routingu**
3. atrybut identyfikujący przynależność prefiksu do określonej sieci VPN
4. zbiór systemów autonomicznych, zrzeszonych w jednym nadrzędnym AS

### Do obsługi ruchu typu BUM w sieci VxLAN można zastosować mechanizm:

1. **replikacji do wszystkich urządzeń w sieci, które pełnią rolę VTEP (head-end replication)**
2. **multicast**
3. Split Horizon
4. tunelowania NVGRE

### Stworzenie ścieżki statycznej powiązanej z interfejsem null0 jest używane przy BGP aby:

1. **można było rozgłosić adres zagregowany, którego nie ma w tablicy routingu**
2. można było przekierować cały ruch przychodzący z innego AS do lokalnej podsieci
3. umożliwić redystrybucję prefiksów rozgłaszanych przez sąsiadów w tym samym AS do protokołu IGP (np. OSPF), działającego w tym AS
4. zapewnić ścieżkę domyślną dla prefiksów przychodzących z innych systemów autonomicznych

### Adresy VPNv4 są przesyłane:

1. **w atrybucie MP_REACH protokołu MP-BGP**
2. w atrybucie extended community protokołu MP-BGP
3. w nagłówku protokołu IPv4
4. przy użyciu protokołu Targeted LDP

### Zasada Split Horizon w zastosowaniu do sesji iBGP oznacza, że:

1. **routery nie rozgłaszają do pozostałych sąsiadów w tym samym AS prefiksów otrzymanych w sesji iBGP**
2. routery BGP w ramach tego samego AS komunikują się tylko z sąsiadami przyłączonymi bezpośrednio
3. routery nie rozsyłają do sąsiadów iBGP prefiksów pochodzących z innych AS
4. routery nie rozsyłają atrybutu Community w ramach sesji iBGP

### Technika VxLAN polega na:

1. dodaniu do ramki Ethernet dodatkowego pola z identyfikatorem tunelu transportowego w sieci IP MPLS
2. dodaniu do ramki Ethernet nagłówka z identyfikatorem wirtualnej sieci LAN oraz enkapsulacji w pakietach protokołu TCP
3. przesłaniu identyfikatora wirtualnej sieci LAN jako atrybutu protokołu MP-BGP
4. **dodaniu do ramki Ethernet nagłówka z identyfikatorem wirtualnej sieci LAN oraz enkapsulacji w pakietach protokołu UDP**

### Route Target jest przesyłany:

1. **w atrybucie extended community protokołu MP-BGP**
2. przy użyciu protokołu Targeted LDP
3. przy użyciu protokołu RSVP-TE

### Obiekt ERO (Explicit Route Object) przesyłany przy zestawianiu sesji RSVP-TE służy do:

1. **wymuszenia określonego trasowania zestawianego tunelu MPLS**
2. wymuszenia, by odpowiedź od routera eLER wróciła tą samą drogą
3. sygnalizacji priorytetu ścieżki
4. uruchomienia mechanizmu Fast Reroute w przypadku awarii łącza

### Na ruch przychodzący do danego AS wpływa skonfigurowany w protokole BGP atrybut:

1. Origin
2. Inbound Priority
3. **MED (Multi Exit Discriminator)**
4. Local Preference

### Który mechanizm/protokół jest wykorzystywany do inżynierii ruchu w sieci IP/MPLS?

1. MP-BGP (Multi-Protocol BGP)
2. **CSPF (Constrained Shortest Path First)**
3. LDP (Label Distribution Protocol)
4. BGP-LS (BGP Link State)

### Który mechanizm/protokół jest wykorzystywany do inżynierii ruchu w sieci IP/MPLS?

1. BGP-LS (BGP Link State)
2. MP-BGP (Multi-Protocol BGP)
3. **RSVP-TE**
4. LDP (Label Distribution Protocol)

### W technice Segment Routing z data plane opartym na protokole MPLS wykorzystuje się:

1. **etykiety globalne - określające segment najkrótszej ścieżki między dwoma routerami**
2. etykiety globalne - określające router
3. etykiety lokalne (tylko w routerach PCC), określające porty na których przyłączone są urządzenia klienckie
4. **etykiety lokalne - określające interfejs danego routera**

### Zaznacz wszystkie rozwiązania, które umożliwiają ograniczenie liczby sesji iBGP w dużych sieciach ISP:

1. **BGP free core**
2. Extended Community
3. Path Prepending
4. **Route Reflector**
5. **AS Confederation**
6. AS Aggregation

### Do obsługi ruchu typu BUM w sieci VxLAN można zastosować mechanizm:

1. **multicast**
2. tunelowania NVGRE
3. **replikacji do wszystkich urządzeń w sieci, które pełnią rolę VTEP (head-end replication)**
4. Split Horizon

### Route Distinguisher to:

1. identyfikator instancji VRF (wirtualnej tablicy routingu) w routerze PE
2. wartość numeryczna, przenoszona w protokole T-LDP, identyfikujaca router PE, który jest źródłem tunelu MPLS
3. **jeden z atrybutów określających preferencję ścieżek w protokole BGP**
4. atrybut dodawany do prefiksów klienckich w sieciach MPLS L3 VPN, aby zapewnić unikalność adresów w sieci operatora

### Stan po poprawnym nawiązaniu sesji BGP z danym sąsiadem to:

1. Active
2. **Established**
3. Confirmed
4. Open

### W usłudze AToM (Any Transport over MPLS) do przenoszenia informacji identyfikującej pseudolącze L2:

1. wykorzystuje się protokół UDP
2. **wykorzystuje się protokół Targeted LDP**
3. wykorzystuje się protokół ARP
4. wykorzystuje się protokół OSPF TE

### Atrybut AS_PATH:

1. **zawiera listę numerów AS, przez które przeszła wiadomość rozgłaszająca dany prefiks**
2. jest rozgłaszany tylko w sesjach iBGP
3. zawiera prefiks rozgłaszany w wiadomości Update
4. jest rozgłaszany tylko w sesjach, w których uczestniczy Route Reflector

### Atrybut AS_PATH: (powtórzenie pytania)

1. **jest wykorzystywany do eliminacji pętli routingowych**
2. zawiera prefiks rozgłaszany w wiadomości Update
3. jest rozgłaszany tylko w sesjach iBGP
4. jest rozgłaszany tylko w sesjach, w których uczestniczy Route Reflector

### W protokole BGP decyzje routingowe podejmowane są:

1. tylko na podstawie odległości sieciowej (liczby "skoków") między systemami autonomicznymi
2. **na podstawie atrybutów ścieżek, rozgłaszanych wraz z prefiksem**
3. w oparciu o metryki łączy, rozgłaszane wraz z prefiksem
4. autonomicznie, w każdym routerze w danym AS, w oparciu o zdefiniowane reguły

### Podstawową funkcją sesji iBGP jest:

1. synchronizacja zegara między routerami połączonymi sesją BGP
2. **zapewnienie, że wszystkie routery wewnątrz AS mają te same informacje dotyczące podsieci osiągalnych poza tym systemem**
3. wymiana informacji routingowej między różnymi systemami autonomicznymi (AS) zarządzanymi przez jednego operatora
4. rozsyłanie kopii danych otrzymywanych z sesji eBGP dla zwiększenia niezawodności

### Które z poniższych stwierdzeń dotyczących etykiety MPLS (MPLS label) jest prawdziwe?

1. **Etykieta MPLS ma wyłącznie znaczenie lokalne – jej wartość nie określa jednoznacznie ścieżki LSP**
2. Etykiety MPLS wykorzystywane dla danej ścieżki LSP muszą być manualnie przydzielone przez administratora sieci
3. Wartość każdej etykiety MPLS jest powiązana z odpowiednim interfejsem routera LER i LSR
4. Wartości etykiet są przenoszone w wiadomości PATH protokołu RSVP

### VTEP jest to:

1. zakończenie tunelu MPLS, zestawionego przez protokół RSVP-TE
2. identyfikator tablicy adresów MAC, właściwej dla określonej instancji sieci eVPN
3. **zakończenie tunelu zestawionego w technice VxLAN**
4. identyfikator instancji VRF (wirtualnej tablicy routingu) w routerze PE

### Systemy autonomiczne (AS) przy użyciu protokołu BGP wymieniają informacje o:

1. stanie routingu wewnętrznego w każdym z AS
2. wybranych prefiksach oraz stanie łączy wewnątrz AS
3. **wybranych prefiksach i atrybutach prowadzących do nich ścieżek**
4. adresach klienckich oraz topologii sieci w każdym AS

### AFI/SAFI są to:

1. identyfikatory sposobu enkapsulacji danych w sieci eVPN/VxLAN
2. **identyfikatory w protokole MP-BGP, wskazujące rodzaj i typ wymienianej informacji routingowej (rodzinę adresów)**
3. identyfikatory wskazujące na przynależność prefiksu do określonej instancji sieci VPN

### Router szkieletowy MPLS podejmuje decyzje dotyczące kierowania pakietów IP na podstawie
1. wartości etykiety MPLS (MPLS Label) zawartej w dodatkowych polach nagłówka ramki Ethernet
2. adresu docelowego IP w nagłówku pakietu IP
3. **wartości etykiety zawartej w dodatkowym nagłówku protokołu MPLS**
4. dodatkowych informacji zawartych w nagłówku ramki Ethernet , w której zawarty jest pakiet IP
