# Proje 1: E-Ticaret Satış Veri Analizi 📊

Bu proje, Python (Pandas, Numpy, Matplotlib) kullanarak bir e-ticaret satış veri seti üzerinde gerçekleştirilen Keşifsel Veri Analizi (EDA) çalışmasını içermektedir.

**Projenin Amacı:**
Bir e-ticaret sitesine ait satış verilerini analiz ederek şirketin satış performansını, popüler ürünlerini ve bölgesel dağılımını anlamak. Bu analizle birlikte yönetime "hangi ürünlere odaklanmalı" ve "hangi şehirlerde pazarlama artırılmalı" gibi konularda içgörüler sunmaktır.

---

## 🚀 Başlarken

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Teknik Gereksinimler

Proje, **Python 3.12.4** kullanılarak geliştirilmiştir. Çalıştırmak için aşağıdaki kütüphanelere ihtiyacınız vardır:

* python 3.12.4
* Pandas 2.3.3
* Numpy 1.26.3
* Matplotlib 3.10.7
 (Analiz kodlarını çalıştırmak için vscode)

Tüm bağımlılıklar `requirements.txt` dosyasında listelenmiştir.

### 2. Veri Seti

proje1'de kullanılan "E-Commerce Sales Dataset" veri seti Kaggle'dan temin edilmiştir.
* **Veri Seti Linki:** [https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data](https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data)
proje2'de kullanılan:Hava Durumu Veri seti drive üzerinden elde edilmiştir
* **Veri Seti Linki** [https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link](https://drive.google.com/file/d/1hAaU2BrJJwvkPA9PGCC3LCAjjx2N23B0/view?usp=drive_link)
proje3'te kullanılan: IMDb Film Veri Seti kaggle'dan temin edilmiştir
* **Veri Seti Linki:** [https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis](https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis)

Lütfen veri setini (`.csv` dosyasını) bu projenin ilgili klasörünün içine indirin.

---

## 🛠️ Kurulum ve Çalıştırma Adımları

Bir terminal veya komut istemcisi açarak aşağıdaki adımları izleyin:

1. Proje Reposunu Klonlayın (Clone):Bu reponun dosyalarını bilgisayarınıza indirin. (Eğer git kullanmıyorsanız, "Download ZIP" seçeneğini de kullanabilirsiniz.)
projeyi klonla: `git clone https://github.com/bora-EEM/yzt_hafta1.git`
klasöre git: `cd yzt_hafta1`
2. Sanal Ortam (Virtual Environment) Oluşturun: Bu adım, projenizin bağımlılıklarını sisteminizin genel Python kurulumundan izole eder. (Şiddetle tavsiye edilir.)
`python -m venv venv`
3. Sanal Ortamı Aktifleştirin:
windows(cmd): `.\venv\Scripts\activate`
MacOS/linux: `source venv/bin/activate`
4. Gerekli Kütüphaneleri Yükleyin: Projenin ihtiyaç duyduğu tüm kütüphaneleri requirements.txt dosyasından otomatik olarak yükleyin.
`pip install -r requirements.txt`
5. Veri Setini İndirin: Bu analiz için gereken Veri Setini indirin. indirdiğiniz .csv dosyasını ilgili klasörün içine taşıyın. (Analiz kodunun veriyi bulabilmesi için bu önemlidir.)
