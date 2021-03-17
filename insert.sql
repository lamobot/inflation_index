BEGIN;
USE inflation_index;

INSERT IGNORE INTO categories (name) VALUES ("globus products");
INSERT IGNORE INTO categories (name) VALUES ("vprok products");
INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/moloko-otbornoe-domik-v-derevne-pasterizovannoe-3-7-4-5-930-ml/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

# INSERT IGNORE INTO links (link, categories_id, typical)
# VALUES (
#     'https://online.globus.ru/products/kombinirovannyy-rassolnyy-produkt-smeshannogo-sostava-sirtaki-original-55-200-g/',
#     (SELECT id FROM categories WHERE name = "globus products"), TRUE
# );

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/shokolad-molochnyy-alenka-s-fundukom-100-g/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/tort-pesochnyy-persidskaya-noch-cheryemushki-s-fundukom-660-g/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/makaronnye-izdeliya-makfa-perya-riflenye-450-g/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/makaronnye-izdeliya-makfa-spagetti-500-g/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/maslo-olivkovoe-filippo-berio-extra-virgin-500-ml/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/maslo-podsolnechnoe-zolotaya-semechka-rafinirovannoe-1-l/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/maslo-podsolnechnoe-oleyna-klassicheskaya-bez-zapakha-1-l/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/muka-pshenichnaya-makfa-vysshiy-sort-2-kg/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/sakhar-pesok-1-kg/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/sok-sady-pridonya-yabloko-vinograd-1-l/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://online.globus.ru/products/voda-artezianskaya-svyatoy-istochnik-negazirovannaya-5-l/',
    (SELECT id FROM categories WHERE name = "globus products"), TRUE
);

-- Vprok Products
INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/domik-v-derevne-dom-v-der-moloko-der-otb-3-5-4-5-930ml--310789',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/sloboda-sloboda-mayonez-provans-olivk-67-230ml--306165',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/alenka-shokolad-alenka-s-fundukom-mol-100g--309352',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/cheremushki-tort-persidskaya-noch-pesochnyy-660g--306748',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/makfa-makfa-makarony-perya-450g--306735',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/makfa-makfa-vermishel-dlinnaya-500g--306732',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/filippo-berio-f-berio-maslo-ex-virgin-oliv-stb-500ml--312170',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/zolotaya-semechka-zol-semechka-maslo-podsol-raf-1l--307905',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/oleyna-oleyna-maslo-pods-rafdezod-1s-1l--305037',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/makfa-makfa-muka-vs-2kg--304611',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/agroperspektiva-tender-sahar-pesoksahar-belyy-1kg--305660',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/sady-pridonya-sady-pridonya-sok-yabl-vinograd-osvet-1l--309568',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

INSERT IGNORE INTO links (link, categories_id, typical)
VALUES (
    'https://www.vprok.ru/product/svyatoy-istochnik-svyat-ist-voda-prirodnaya-pit-negaz-pet-5l--307268',
    (SELECT id FROM categories WHERE name = "vprok products"), TRUE
);

COMMIT;