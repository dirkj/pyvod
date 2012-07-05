<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1338641929868" ID="ID_404258814" MODIFIED="1338641977900" TEXT="Optische Gleisbelegtmeldung">
<font ITALIC="true" NAME="SansSerif" SIZE="12"/>
<node CREATED="1338642003736" ID="ID_235238846" MODIFIED="1338642031067" POSITION="right" TEXT="Gleis-LEDs">
<node CREATED="1338642061205" ID="ID_858108877" MODIFIED="1338642071281" TEXT="LEDs einzeln ansteuerbar"/>
<node CREATED="1338642072581" ID="ID_1144011466" MODIFIED="1338642082578" TEXT="Leuchten gesteuert kurz auf"/>
<node CREATED="1338642084733" ID="ID_637563143" MODIFIED="1338642088058" TEXT="Mehrere je Gleis"/>
<node CREATED="1338642089660" ID="ID_1879899097" MODIFIED="1338642106976" TEXT="2-4 LEDs zur Kalibierung --&gt; automatische Kalibrierung"/>
</node>
<node CREATED="1338642031966" ID="ID_28840520" MODIFIED="1338642041746" POSITION="right" TEXT="Bilderfassung mit IP-Camera">
<node CREATED="1338642116163" ID="ID_1715456606" MODIFIED="1338642123719" TEXT="Kann gezielt LEDs ein- und ausschalten"/>
<node CREATED="1338642124828" ID="ID_1792226353" MODIFIED="1338642132489" TEXT="Anschlie&#xdf;end werden die Bilder ausgewertet"/>
<node CREATED="1338642133764" ID="ID_6204699" MODIFIED="1338642149862" TEXT="Bestimmter Farbkanal? Bestimmte Helligkeit? Grenzen? --&gt; Experimente"/>
<node CREATED="1338642170258" ID="ID_1695903842" MODIFIED="1338642183216" TEXT="Infrarot-LEDs besser als Farb-LEDs geeignet?"/>
<node CREATED="1338642184074" ID="ID_389984357" MODIFIED="1338642194741" TEXT="Kann verhindert werden, dass das menschliche Auge das Flackern sieht?"/>
<node CREATED="1338642206641" ID="ID_1263330717" MODIFIED="1338642228334" TEXT="Position der LEDs im Rahmen eines Kalibrierungsprozesses im Bild automatisch ermitteln"/>
<node CREATED="1338642271760" ID="ID_897627214" MODIFIED="1338642284013" TEXT="Gleisplan muss hinterlegt werden, LED-Positionen im Gleisplan vermerkt werden"/>
</node>
<node CREATED="1338642329294" ID="ID_113382575" MODIFIED="1338642332523" POSITION="right" TEXT="TODOs">
<node CREATED="1338642333478" ID="ID_1699584562" MODIFIED="1338642376675" TEXT="Beschreibungsformat f&#xfc;r Gleisplan und LED-Positionen sowie Adressierung/Ein-/Ausschaltung definieren"/>
<node CREATED="1338642768827" FOLDED="true" ID="ID_116053257" LINK="#ID_749367097" MODIFIED="1338670355274" TEXT="Beschreibungsformat f&#xfc;r Konfiguration, z.B. Adresse bzw. Zugriff auf die IP-Camera">
<icon BUILTIN="button_ok"/>
<node CREATED="1338643012652" ID="ID_899939142" MODIFIED="1338643067537" TEXT="import ConfigParser, os&#xa;config = ConfigParser.ConfigParser()&#xa;config.readfp(open(&apos;defaults.cfg&apos;))&#xa;config.read([&apos;site.cfg&apos;, os.path.expanduser(&apos;~/.myapp.cfg&apos;)])"/>
<node CREATED="1338643170512" ID="ID_1467553689" MODIFIED="1338643258071" TEXT="Example of writing config file:&#xa;&#xa;import ConfigParser&#xa;&#xa;config = ConfigParser.RawConfigParser()&#xa;&#xa;# When adding sections or items, add them in the reverse order of&#xa;# how you want them to be displayed in the actual file.&#xa;# In addition, please note that using RawConfigParser&apos;s and the raw&#xa;# mode of ConfigParser&apos;s respective set functions, you can assign&#xa;# non-string values to keys internally, but will receive an error&#xa;# when attempting to write to a file or when you get it in non-raw&#xa;# mode. SafeConfigParser does not allow such assignments to take place.&#xa;config.add_section(&apos;Section1&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;int&apos;, &apos;15&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;bool&apos;, &apos;true&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;float&apos;, &apos;3.1415&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;baz&apos;, &apos;fun&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;bar&apos;, &apos;Python&apos;)&#xa;config.set(&apos;Section1&apos;, &apos;foo&apos;, &apos;%(bar)s is %(baz)s!&apos;)&#xa;&#xa;# Writing our configuration file to &apos;example.cfg&apos;&#xa;with open(&apos;example.cfg&apos;, &apos;wb&apos;) as configfile:&#xa;    config.write(configfile)&#xa;"/>
<node CREATED="1338643281501" ID="ID_732296654" MODIFIED="1338643586639" TEXT="[camera]&#xa;url: http://192.168.0.202/picture.jpg&#xa;&#xa;[stationscheme]&#xa;file: weitingen-scheme.xml&#xa;&#xa;[locationsmap]&#xa;file: weitingen-locations.xml&#xa;&#xa;[led-access]&#xa;"/>
</node>
<node CREATED="1338642384716" ID="ID_1400795039" MODIFIED="1338642396138" TEXT="HW f&#xfc;r LED-Ansteuerung entwerfen"/>
<node CREATED="1338642398309" ID="ID_1937332781" MODIFIED="1338642411384" TEXT="SW-Schnittstelle f&#xfc;r LED-Ansteuerung entwerfen"/>
<node CREATED="1338642602111" FOLDED="true" ID="ID_559711908" MODIFIED="1338643609958" TEXT="Bedienoberfl&#xe4;che und Funktionen der PC-Software entwerfen">
<node CREATED="1338642625951" ID="ID_557150538" MODIFIED="1338642638450" TEXT="Interaktion nur f&#xfc;r Experimente notwendig (zun&#xe4;chst)"/>
<node CREATED="1338642639254" ID="ID_146156489" MODIFIED="1338642644475" TEXT="Permanente Bilddarstellung"/>
<node CREATED="1338642645470" ID="ID_1347511573" MODIFIED="1338642650731" TEXT="&#xdc;berlagerung mit Gleisplan"/>
<node CREATED="1338642651589" ID="ID_1490887035" MODIFIED="1338642659531" TEXT="Separate Schemadarstellung des Gleisplans"/>
<node CREATED="1338642690277" ID="ID_1373193533" MODIFIED="1338642706826" TEXT="LED-Lichtabdeckung im Schema und im Bild zeigen"/>
<node CREATED="1338642711332" ID="ID_1255951064" MODIFIED="1338642718448" TEXT="Logfile / Protokoll anzeigen"/>
<node CREATED="1338642721812" ID="ID_986376575" MODIFIED="1338642730312" TEXT="Button zum Start der Kalibrierung"/>
<node CREATED="1338642733516" ID="ID_1655752198" MODIFIED="1338642747323" TEXT="Button zum Exit"/>
</node>
<node CREATED="1338643611333" ID="ID_1138213341" MODIFIED="1338643618314" TEXT="Python">
<node CREATED="1338643618660" ID="ID_749367097" LINK="#ID_116053257" MODIFIED="1338670294387" TEXT="Config file">
<arrowlink DESTINATION="ID_116053257" ENDARROW="Default" ENDINCLINATION="384;0;" ID="Arrow_ID_1898186478" STARTARROW="None" STARTINCLINATION="384;0;"/>
<icon BUILTIN="button_ok"/>
</node>
<node CREATED="1338643739073" FOLDED="true" ID="ID_1159214284" MODIFIED="1338670304282" TEXT="XML">
<node CREATED="1338643983403" ID="ID_1246896514" MODIFIED="1338644009646" TEXT="Beispiel: XML-Datei lesen mit DOM:&#xa;&#xa;def lade_dict(dateiname): &#xa;    d = {} &#xa;    baum = dom.parse(dateiname)&#xa;&#xa;    for eintrag in baum.firstChild.childNodes: &#xa;        if eintrag.nodeName == &quot;eintrag&quot;: &#xa;            schluessel = wert = None&#xa;&#xa;            for knoten in eintrag.childNodes: &#xa;                if knoten.nodeName == &quot;schluessel&quot;: &#xa;                    schluessel = _knoten_auslesen(knoten) &#xa;                elif knoten.nodeName == &quot;wert&quot;: &#xa;                    wert = _knoten_auslesen(knoten)&#xa;&#xa;            d[schluessel] = wert &#xa;    return d&#xa;"/>
<node CREATED="1338644211445" ID="ID_1012850827" MODIFIED="1338644224899" TEXT="Alternative ElementTree --&gt; aber kein Standard :-("/>
</node>
<node CREATED="1338643745593" ID="ID_918386945" MODIFIED="1338643775957" TEXT="PIL, scipy, numpy --&gt; imaging"/>
<node CREATED="1338643755817" ID="ID_1288694728" MODIFIED="1338643813549" TEXT="User Interface Qt? TK?">
<node CREATED="1338649639695" ID="ID_208975190" MODIFIED="1338649643188" TEXT="Gtk"/>
<node CREATED="1338649643965" ID="ID_1433050054" MODIFIED="1338649647221" TEXT="Glade3"/>
<node CREATED="1338649661373" ID="ID_72473027" MODIFIED="1338649667387" TEXT="Design / Widgettree">
<node CREATED="1338649669741" ID="ID_1415608529" MODIFIED="1338649673363" TEXT="Window">
<node CREATED="1338649673363" ID="ID_753017808" MODIFIED="1338649692088" TEXT="VBox">
<node CREATED="1338649692089" ID="ID_727809284" MODIFIED="1338649770233" TEXT="MenuBar"/>
<node CREATED="1338649696236" ID="ID_109977544" MODIFIED="1338649698331" TEXT="Toolbar"/>
<node CREATED="1338649702619" ID="ID_1145364874" MODIFIED="1338649705835" TEXT="HBox">
<node CREATED="1338649707108" ID="ID_1419077264" MODIFIED="1338649748690" TEXT="VBox">
<node CREATED="1338649730379" ID="ID_855097572" MODIFIED="1338649816329" TEXT="LivePicture Viewport">
<node CREATED="1338649825161" ID="ID_375438737" MODIFIED="1338649827872" TEXT="Alignement">
<node CREATED="1338649831208" ID="ID_1916064407" MODIFIED="1338649832873" TEXT="Frame">
<node CREATED="1338649835504" ID="ID_352021834" MODIFIED="1338649837736" TEXT="DrawingArea"/>
</node>
</node>
</node>
<node CREATED="1338649735299" ID="ID_33016093" MODIFIED="1338649820680" TEXT="SchemaPicture Viewport">
<node CREATED="1338649840080" ID="ID_1287214952" MODIFIED="1338649842956" TEXT="Alignement">
<node CREATED="1338649842957" ID="ID_767384204" MODIFIED="1338649844566" TEXT="Frame">
<node CREATED="1338649844566" ID="ID_251932390" MODIFIED="1338649847024" TEXT="DrawingArea"/>
</node>
</node>
</node>
</node>
<node CREATED="1338649714892" ID="ID_852598813" MODIFIED="1338649726274" TEXT="LogView"/>
</node>
<node CREATED="1338649755787" ID="ID_1153023836" MODIFIED="1338649758296" TEXT="Status"/>
</node>
</node>
</node>
</node>
<node CREATED="1338644353634" ID="ID_1453344748" MODIFIED="1338644356406" TEXT="Klassen">
<node CREATED="1338644518708" ID="ID_1532570566" MODIFIED="1338644527098" TEXT="Model">
<node CREATED="1338644357449" ID="ID_1657183927" MODIFIED="1338644372407" TEXT="Gleisplan"/>
<node CREATED="1338644376983" ID="ID_480717047" MODIFIED="1338644381382" TEXT="Position"/>
<node CREATED="1338644381857" ID="ID_453175855" MODIFIED="1338644385095" TEXT="LED"/>
<node CREATED="1338644404727" ID="ID_1435178704" MODIFIED="1338644409990" TEXT="RawPicture"/>
<node CREATED="1338644413231" ID="ID_526185105" MODIFIED="1338644443675" TEXT="LEDPositionInPicture"/>
<node CREATED="1338644453558" ID="ID_245837334" MODIFIED="1338644486842" TEXT="CalibrationPoints = LEDs an Kalibrationspositionen"/>
</node>
<node CREATED="1338644528109" ID="ID_1769845529" MODIFIED="1338644529985" TEXT="View">
<node CREATED="1338644562692" ID="ID_1254678878" MODIFIED="1338644597320" TEXT="LivePictureDisplay"/>
<node CREATED="1338644572948" ID="ID_1396189366" MODIFIED="1338644577762" TEXT="SchemaDisplay"/>
<node CREATED="1338644579027" ID="ID_1289740923" MODIFIED="1338644592264" TEXT="LivePictureOverlay"/>
<node CREATED="1338644699488" ID="ID_1096657109" MODIFIED="1338644708012" TEXT="LogDisplay"/>
</node>
<node CREATED="1338644530492" ID="ID_1009297994" MODIFIED="1338644532875" TEXT="Controller">
<node CREATED="1338644719183" ID="ID_1102088289" MODIFIED="1338644730638" TEXT="ActionController">
<node CREATED="1338644733447" ID="ID_861280876" MODIFIED="1338644746382" TEXT="ExitAction"/>
<node CREATED="1338644747631" ID="ID_635773312" MODIFIED="1338644753067" TEXT="StartCalibrationAction"/>
<node CREATED="1338644774606" ID="ID_637198706" MODIFIED="1338644802700" TEXT="TimerAction --- evtl. nicht n&#xf6;tig, weil dauernd untersucht werden k&#xf6;nnte"/>
</node>
</node>
</node>
</node>
</node>
</node>
</map>
