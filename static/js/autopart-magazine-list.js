const stores = [
    {
        name: "Avto 101",
        description: "Avto 101 mağazası 2015-ci ildən fəaliyyət göstərir. Monitor və kameraların quraşdırılması təcrübəli ustalarımız tərəfindən həyata keçirilir.",
        phoneNumber: "(050) 300-70-75",
        image: "./img/avtologo.jpg",
        category: "Ban",
        views: "13 057"
    },
    {
        name: "Avto Start",
        description: "2005-ci ildən fəaliyyət göstərən “Avto Start” mağazası (Alman, Yapon, Koreya və Amerika) avtomobilləri üçün orijinal və firma ehtiyat hissələrinin servisini həyata keçirir.",
        phoneNumber: "(055) 387-03-33",
        image: "./img/autologo.jpg",
        category: "Texniki",
        views: "10 616"
    },
    {
        name: "Volt Akkumulyator Mərkəzi",
        description: "Ağır texnika, uşaq avtomobilləri, günəş panelləri və yeni nəsil avtomobillər üçün istənilən brendə məxsus akkumulyatorların, eləcə də mühərrik yağlarının satışı.",
        phoneNumber: "(051) 785-50-50",
        image: "./img/voltlogo.jpg",
        category: "Texniki",
        views: "5 428"
    },
    {
        name: "Avto Mega",
        description: "Mercedes-Benz, Hyundai, KIA, Chevrolet, BMW, Toyota, Nissan, Mitsubishi, Infiniti, Lexus, Jeep, Volkswagen ehtiyat hissələrinin topdan və pərakəndə satışı. Xüsusi endirimlər! BirKart (2, 3, 6 ay taksit).",
        phoneNumber: "(050) 299-84-05",
        image: "./img/logogo (19).jpg",
        category: "Ban",
        views: "27 570"
    },
    {
        name: "Avto Store 333",
        description: "Mağazamızda istədiyiniz bütün aksesuarları münasib qiymətə tapacaqsınız. Məqsədimiz Sizi zövqünüzə uyğun aksesuarlarla təmin edərək razı salmaqdır.",
        phoneNumber: "(055) 905-33-33",
        image: "./img/avtologo (1).jpg",
        category: "Salon",
        views: "257 842"
    },
    {
        name: "BMW Box Baku",
        description: "BMW aksesuar və ehtiyat hissələrinin satışı və yerində quraşdırılması.",
        phoneNumber: "(055) 685-00-90",
        image: "./img/logo (135).jpg",
        category: "Ban",
        views: "14 161"
    }
    
];

const storeList = document.getElementById("storeList");
const searchInput = document.getElementById("searchInput");
const categorySelect = document.getElementById("categorySelect");

function updateStoreList() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedCategory = categorySelect.value;

    storeList.innerHTML = "";

    stores.forEach(store => {
        if (selectedCategory === "all" || store.category === selectedCategory) {
            if (store.name.toLowerCase().includes(searchTerm)) {
                const storeItem = document.createElement("div");
                storeItem.className = "grid-item";
                const image = document.createElement("img");
                image.className = "store-image";
                image.src = store.image;
                const storeInfo = document.createElement("div");
                storeInfo.className = "store-info";
                const name = document.createElement("div");
                name.className = "store-name";
                name.textContent = store.name;
                const description = document.createElement("div");
                description.textContent = store.description;

                const phoneNumber = document.createElement("div");
                phoneNumber.className = "phone-number";
                phoneNumber.innerHTML = '<img class="tel-img" src="./img/tel.png">' + store.phoneNumber;

                const views = document.createElement("div");
                views.className = "views";
                views.innerHTML = '<img class="views-img" src="./img/views.png">' + store.views;

                storeInfo.appendChild(name);
                storeInfo.appendChild(description);
                storeInfo.appendChild(phoneNumber);
                storeInfo.appendChild(views);
                storeItem.appendChild(image);
                storeItem.appendChild(storeInfo);
                storeList.appendChild(storeItem);
            }
        }
    });
}

searchInput.addEventListener("input", updateStoreList);
categorySelect.addEventListener("change", updateStoreList);

updateStoreList();
