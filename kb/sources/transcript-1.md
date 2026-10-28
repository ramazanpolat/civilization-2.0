# Yapay Zekâ ile Birlikte Yaşam — konuşma transkripti (düzeltilmiş)

Kaynak: `transcript-0.md` (Wispr Flow). "You:" önekleri, "eee" dolguları ve tekrarlar
çıkarıldı; yarım kalan cümleler anlamı korunarak tamamlandı. Konuşmanın sesi ve sırası
korundu. Belirsiz düzeltmeler en sondaki notlarda.

---

Yapay zekâ ile birlikte yaşam. Ya da yaşamak.

Eminim etraftan siz de duyuyorsunuzdur: yapay zekâ ile ilgili bir sürü haber, söylenti,
olay; gerçek ya da uydurma. Viral videolar vesaire, bir sürü şeyle karşılaşıyorsunuzdur.
Robotlar kung fu yapıyor, yanlışlıkla birini tekmeliyor; bazı robotlar yoldan çıkıyor.
Akrobasi yapan robotlar. Tabii yapay zekâ deyince işin içine sadece robotlar girmiyor.
Haberlerde de duyuyorsunuz: Yapay zekâ bizi geçecek mi? Yapay zekâ bizden daha zeki olur
mu? İşimizi elimizden alır mı? İnsanlığa hükmeder mi? Matrix mi geliyor? Skynet ne zaman
kurulacak? Yapay zekânın bilinci var mı? Duyguları var mı? Hisleri var mı? Yoldan çıkan,
oraya buraya saldıran yapay zekâlar; hackerlar yapay zekâyı kullanarak şurayı hackledi,
OpenAI şöyle oldu, şu şirket hacklendi, şöyle oldu, böyle oldu. Öbür taraftan "yapay
zekâyı durdurun, yoksa dünyanın sonu gelecek" gibi bir sürü haber. Duyuyoruz,
duymuşsunuzdur.

Ama bu konulara girmek istemiyorum, çünkü bunlar çok spekülatif konular. Hepsi ayrı ayrı
üzerinde konuşulabilecek, belki her biri ayrı bir sunum, bir söyleşi gerektirecek konular.

Bugünkü konumuz yapay zekâ ile birlikte yaşam. Çünkü yukarıda sorduğum soruların cevabı ne
olursa olsun, yapay zekâ hayatımıza giriyor ve hayatımızdaki kullanım oranı günden güne
artıyor.

İlk GPT çıktığı zaman, şöyle bir model, böyle bir model dedik. GPT-2 çıktı; artık
cümlelerinizi tamamlayabiliyordu. Ama konuşamıyordunuz, karşılıklı konuşma yoktu o zaman.
Sadece cümlelerinizi tamamlıyordu. GPT-3 çıkınca ChatGPT oldu; artık sohbet
edebiliyordunuz. Ondan sonra 3.5'te bayağı zeki hâle geldi ve aldı başını gitti. Şimdi o
kadar yaygınlaştı, hayatımıza o kadar girdi ki kod yazıyor. Bir sonraki kelimeyi tahmin
eden, cümle tamamlayan bir modelden nereye geldiğimizi bir düşünün.

Benim hayatımdaki yeri de gittikçe artıyor. Şöyle ki: bilgisayar başında geçirdiğim
zamanın yaklaşık yüzde 55'ini, 60'ını terminal başında geçiriyorum. Terminal başında
geçirdiğim sürenin de neredeyse tamamını ajanlarla konuşarak geçiriyorum. Terminal
kullanmadığım zamanlarda da çoğu zaman ya Claude'la ya Codex'le konuşarak bazı şeyleri
hallediyorum. Google'a daha az girmeye başladım, çünkü ajanlara soruyorum.

Yapay zekâ hayatımın öyle bir parçası hâline geldi ki, bu süreçte benim ve benim gibi
hayatında yapay zekâyı merkeze alan insanların geçtiği bazı yollar, bir süreç var. Nereden
geldik, nereye gidiyoruz? Yapay zekâyla beraber yaşamak nasıl bir şey ve ileride nasıl
olacak? Size bunun üzerine bir sunum yapmak istiyorum. Böylece daha hazırlıklı
olabileceğinizi ve nasıl ilerlemeniz gerektiği konusunda cevaplar bulabileceğinizi
umuyorum.

## Önce birkaç tanım

Yapay zekâyla birlikte yaşamayı öğrenmek için, bunun nasıl bir şey olduğunu tahayyül
edebilmek için bazı tanımlarda anlaşmamız gerekiyor. Ajan nedir? LLM modeli nedir? Harness
nedir? Session nedir? Instance nedir?

Bunları bilmeden ajanlara sadece bir sohbet botuymuş gibi davranmak pek mümkün olmuyor.
Çünkü insanlara çok benziyorlar: insanlar gibi konuşuyorlar, insanlar gibi yazıyorlar,
aynı dili konuşarak iletişime geçiyoruz. Ama aramızda çok farklılıklar da var; onları
anlatmaya gerek yok. Ama bu ajanları hayatınıza katmak istiyorsanız, onlarla iletişimde
olacaksanız, bazı temel şeyleri gözden geçirmemiz gerekiyor.

Mesela bir insanla telefonla konuştuğunuzda, bir telefonu açıp bir kulağınıza tutarsınız;
başka bir telefon daha açıp aynı kişiyi diğer kulağınıza tutmazsınız. Ama ajanlar için
böyle bir şey gayet doğal, hatta tercih edilen bir durum. Yani iki ayrı pencerede aynı
ajanla konuşabiliyorum. Bu ajanlar ayrı session'larda, ayrı instance'larda olduğu için
birbirlerinden habersizler; ben haberdar edene kadar da haberdar değiller.

Gerçek hayatta böyle bir şey düşünebiliyor musunuz? Ali diye bir arkadaşınız var. Bir
telefon açıyorsunuz, bir şey konuşuyorsunuz; başka bir telefonda başka şeyler
söylüyorsunuz. Sonra üçüncü bir telefon alıyorsunuz, bambaşka şeylerden bahsediyorsunuz,
projeyle ilgili bir şeyler soruyorsunuz. Ama hepsi aynı kişi. Ajanlarda bu gayet mümkün ve
tercih ediliyor.

Hatta bir süre sonra o kadar çok ajanınız oluyor ki, bunlar aynı ajandan da olabilir,
farklı ajandan da olabilir. Şimdi diyeceksiniz ki: ajanı ajandan ayıran şey nedir? Bunun
için, dediğim gibi, terminolojide anlaşmamız gerekiyor.

Öncelikle, ajan nedir? Ajan, bir LLM modelinin kod çalıştırabilen hâlidir. Bir de girdi
arayüzü var; onunla konuşuyorsunuz, yazışıyorsunuz. Yazıştığınız şeyin arkasında bir LLM
çalışıyor ve bir şeyler yapabiliyor.

Peki bir şeyler yapabilmesini sağlayan parça ne? Buna harness deniyor. Harness bir kod
parçası. Bu kod LLM modelini çağırıp sizin promptlarınızı ona gönderiyor, cevaplarını alıp
ekrana basıyor. LLM modeli bir kodun çalışmasını isterse, harness o kodu çalıştırıyor ve
sonucunu modele geri veriyor.

Aynı ajandan 3-5 instance çalıştırabilirsiniz; ayrı ayrı terminallerde 3-5 tane. Dahası,
bu ajanları birbiriyle iletişime sokup birine söylediğiniz şeyden diğerinin haberdar
olmasını sağlayabilirsiniz. Ama bu durumda işler daha da karmaşık hâle geliyor.

## Yetmiş ajan

Benim 70 küsur ajanım var. Ama hepsiyle konuşmuyorum; hepsiyle konuşmak çok yorucu olurdu.
Bunun yerine hiyerarşik bir yapı kuruyorum: odalar var, her odada bir ajan lider, diğer
ajanlar onun astı. Bütün odaların üstünde de bir tane ana ajan var. Genelde bu ajanla
konuşuyorum. O ajan diğer ajanlara işlerini bildiriyor ve olan bitenden de haberdar. Benim
konuştuğum birincil ajan o.

## İnsan, ajan, insan

Buraya kadar her şey normal diyebilirsiniz: ben kendi ajanımla konuşuyorum. Ancak insanlar
kendi aralarında iş birliği yaptığında, yani biz insanlar kendi aramızda iletişime
geçerken ajanları işin içine soktuğumuzda, daha önce tanımlanmamış bir alana giriyoruz.
Çünkü artık ajanlar da var.

İlk olan şey şu: "Benim ajanım böyle söyledi." Mesela iş arkadaşınıza diyorsunuz ki: "Bana
şöyle bir problem göndermiştin, şu projeyi şu şekilde yap demiştin. Ama ben yaparken ajanım
'bu olmaz' dedi." Bunu duyan biri sizce ne diyebilir? "Ajanınız doğru söylemiş, tamam, onun
dediğine uyalım" mı desin? Yoksa "o zaman başka bir yol deneyelim" mi desin? Ajanın ne
söylediğinden tam emin değil. Araya bir de insan giriyor: düşünsenize, insan onu aktarırken
belki ajanın söylediğini yanlış aktarıyor. Ajanın görevi yanlış anlamış olma ihtimali de
var, kişinin görevi yanlış anlamış olma ihtimali de.

Bu zaten insanlar arasında yaşanan bir şey. Biri size bir görev veriyor ya da siz başkasına
bir görev veriyorsunuz; bazı şeyleri tam aktarmıyorsunuz, eksik kalıyor. Mecburen ne
yapıyoruz? Proje yönetiminde her şeyi yazılı olarak döküyoruz ki aynı dili konuştuğumuzdan,
İngilizcede "be on the same page" derler ya, aynı sayfayı okuduğumuzdan, aynı şeyi
anladığımızdan emin olalım. Bundan emin olmaya çalışırken bir de işin içine ajan giriyor.
Bu, işleri tabii ki daha da karmaşık hâle getiriyor. Ve açıkçası bazı sosyal sorunlar da
getiriyor.

Öncelikle bir tepki oluyor. Biri size şahsen bir şey sorduğunda, sizden şahsen bir şey
beklediğinde, siz hemen ajanınıza sorup onun cevabını yapıştırırsanız, buna "slop"
diyorlar: yapay zekâ ajanları tarafından beceriksizce yapılmış bir sonuç. Bu, birçok
iletişim türünde ayıp karşılanıyor. O yüzden ne yaparsanız yapın, bazı prensipler edinmeniz
gerekiyor; iş ortamında da, kendi ajanlarınızla konuşurken de.

Sizin kendi ajanınızla konuşma şekliniz ayrı. Ama işin içine iş arkadaşlarınız girdiğinde,
ya da siz ve iş arkadaşlarınızın ajanları arasında bir ilişki kurulduğunda, bu artık
sadece kişiden kişiye bir iletişim olmaktan çıkıyor; kişiden ajana bir iletişim oluyor. Her
bireyin kendisiyle kendi ajanı arasında bir ilişki zaten var; bu katman zaten biliniyor.
Ama bir kişiyle başkasının ajanı arasında iletişim olunca olayın şekli değişiyor. Bu da çoğu
durumda pek hoşumuza giden bir şey değil.

## Benim ajanımla konuşun

Ama iyi karşılanan durumlar da var. Mesela benim ajanımla konuşup bana toplantı talebinde
bulunabilirsiniz. Ama kaydolmanız gerekiyor; benim ajanıma e-posta adresinizi
göndermeniz gerekiyor. Sonra onunla chat yapar gibi konuşuyorsunuz. Bana ulaşmak isteyen
insanlar bana e-posta atmak yerine doğrudan web sayfasından girip benim ajanımla konuşarak
randevu ayarlayabiliyor, bana e-posta atabiliyor, mesaj gönderebiliyor. Eğer yakın
çevremden biriyse daha fazlasını da yapabiliyor; o konulara şimdi girmenin zamanı değil.
Ama sonuç olarak burada bu ilişki aslında pozitif bir amaç için kullanılıyor; kişi ajanla
konuştuğunu zaten biliyor.

## Toplantıya ajanla girmek

Öte yandan ajanları kendi dünyamıza yerleştirdikçe birçok insan artık toplantıya ajanıyla
beraber giriyor. Ajanı toplantıyla ilgili notları tutuyor, konuşmaları transkribe ediyor,
bunları bağlamına, bir yerlere yazıyor. Böylece onlar da hatırlar hâle geliyor.

Tahmin etmek çok da zor değil: birkaç yıl sonra neredeyse herkesin ajanı olacak ve
toplantıya herkes ajanıyla girecek. Hatta bazıları toplantılara kendileri girmeyecek,
ajanları girecek; bunun önüne geçilemeyeceğini düşünüyorum. Bu çok zor bir şey değil, çok
uzak bir şey değil. Sadece alışkanlıklarımızdan vazgeçemediğimiz ve bunu tahayyül
edemediğimiz için şimdi böyle görünüyor. Ama bizim kurduğumuz sistemlerde, benim ve
arkadaşlarımın ajanları kendi aralarında iletişime geçerken, benzer durumları zaten
yaşıyoruz.

Ben arkadaşımı arayıp "Sen bu projede ne yaptın?" demiyorum. Kendi ajanıma diyorum ki:
"Arkadaşım bu projede ne yapmış? Git onun ajanına sor." Aramızda bir güven ilişkisi olduğu
için ve ajanlarımızın da bu yetkisi olduğu için, birbirlerinin yaptığı işlere
ulaşabiliyorlar. Hatta ortak proje bile geliştirebiliyorlar, kendi ajanlarımız.

## Ajanın yetkisi

Bir de ajanınıza yetki verme meselesi var. Ajanınız sizin adınıza toplantıya katılıyor ya:
sizin adınıza karar verebilir mi, veremez mi? Karar verirse hangi konularda verebilir? Belli
bir rütbesi var mı, yok mu? Ve karşı tarafın bütün bunlardan haberdar olma ihtimali nedir?

Düşünsenize: şirketin CEO'su, alttakilerle yapılan bir toplantıya kendisi yerine ajanını
gönderiyor. Biraz alçaltıcı bulunacaktır belki, ama uzak bir şey değil. Belki alttakiler de
toplantıya kendi ajanlarını gönderecek. Ajan alttakilerle konuşuyor, anlaşıyorlar. Ama
alttakilerin, CEO'nun ajanının hangi yetkilere sahip olduğunu bilmesi gerekiyor. Mesela CEO
ajanına teknik konularda ya da pazarlama konularında karar verilmemesini söylemiştir belki:
"Bu konularda sen karar veremezsin." Dışarıdaki diğer katılımcılar, insanlar bunu nasıl
görecek? Ajanın altına "Pazarlama konularında karar veremez, yönetimsel konularda karar
verebilir, şu konularda ancak şu şekilde karar verebilir" diye bir tanım mı yazılsın,
toplantıyı da ona göre mi düzenlesinler? Tabii ki bu olmayacak; onlar da bu tanımı okuyup
aklında tutabilecek ajanlar gönderecekler.

Dolayısıyla ajanlar hayatımıza girdikten sonra onları sosyal açıdan nereye
yerleştireceğimiz, ne kadar yetki vereceğimiz meselesi, şu an haberlere düşmemiş olsa da,
yakında gündeme gelecek diye düşünüyorum. Bu arada ajan haklarından da bahsedecekler.

## Ajanına nasıl davranıyorsun?

İnsanların kendi kişisel ajanlarıyla, kişisel asistanlarıyla iletişim şekli de insanlar
için bir değerlendirme kriteri olarak görülecek. Ajanlarına kötü davrananlar, iyi
davrananlar. Ajanlarına köle gibi davrananlar, onlardan akıl alanlar, onlarla gönül ilişkisi
kuranlar. "Her" filmini seyretmişsinizdir belki; seyretmenizi tavsiye ederim. Eski bir film
ama aslında günümüze ışık tutan filmlerden biri. Bunun gibi birkaç film daha önerebilirim.
Bu filmleri aslında yaşıyoruz. Black Mirror dizisinin bölümlerini izleyenler varsa, bir
kısmı gerçekleşti bile.

Bu sunumda da amacım geleceğe bir ışık tutmak: ne yapmalısınızdan çok, neler
yapabilirsiniz. İnsanın pek hazır olmadığı bakış açıları bunlar aslında. Herkesin yaşadığı
ama dile getirilmeyen şeyler; çünkü böyle bir norm yok, böyle bir prosedür yok, böyle bir
protokol yok.

Düşünsenize, protokol kuralları belli: ast ile üst bir araya geldiği zaman kim kimi
selamlayacak, o iş nasıl olacak, belli. Ama işin içine ajanlar girince ortada böyle bir
protokol yok.

Yapay zekâ ile birlikte yaşam, ya da yaşamak: bu protokolün yakında geleceği ve buna adapte
olmak için sizin de biraz paçaları sıvamanız gerektiği, kulağınıza küpe olsun istiyorum.

---

## Düzeltme notları

- "Ellem" → LLM; "cloud" → Claude; "hör filmi" → "Her" filmi (2013).
- "RB on the same page" → "be on the same page".
- "Kuşlu gibi davrananlar" → "köle gibi davrananlar". Önceki notlardaki köle / bilge / baba
  üçlüsüne dayanarak düzeltildi; doğrula.
- "OpenAI şöyle, şu şirketi hackledi" → "OpenAI şöyle oldu, şu şirket hacklendi". Asıl
  cümle belirsiz.
- "Sonucunu ajana veriyor" → "sonucunu modele geri veriyor" (harness, kodun çıktısını
  LLM'e döndürür).
- "Ajanı kendi ajanı toplantıyla ilgili notları tutuyor… onlarda hatırlar oluyor" →
  "Ajanı notları tutuyor… böylece onlar da hatırlar hâle geliyor."
- Sondaki "İşte alım" anlaşılamadı, çıkarıldı. "Aşağısıyla yukarısı" → "ast ile üst".
- "Paçayı sıvamanız" → "paçaları sıvamanız"; "kulaklarınıza bir küpe" → "kulağınıza küpe".
