from selenium import webdriver

from Scraping_methods import *

# {'label': 'title', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 0, 'offset': 0, 'get_what': 'tag'}
# {'label': 'title', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 0, 'offset': 0, 'get_what': 'text'}
# {'label': 'x', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 1, 'start': 0, 'end': 4, 'get_what': 'attr', 'attr': 'class'}

# giant = "Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Cakes,Cupcake & Muffins_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesCakes-Cupcake-Muffins/c/F1710100?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Coated Biscuits & Wafers_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesCoated-Biscuits-Wafers/c/F1710200?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Crackers & Crispbread_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesCrackers-Crispbread/c/F1710300?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Filled Biscuits_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesFilled-Biscuits/c/F1710500?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Rusk_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesRusk/c/F1710600?currentPage=0&filter=product_category_external_id%3A%27Rusk%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Biscuits, Crackers & Cakes_DELM_Digestives & Assorted Biscuits_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Biscuits-Crackers-CakesDigestives-Assorted-Biscuits/c/F1710400?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Breakfast Cereals & Bars_DELM_Cereals_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Breakfast-Cereals-BarsCereals/c/F1720200?currentPage=1&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Breakfast Cereals & Bars_DELM_Puffs_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Breakfast-Cereals-BarsPuffs/c/F1720100?currentPage=0&filter=product_category_external_id%3A%27Puffs%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Breakfast Cereals & Bars_DELM_Muesli_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Breakfast-Cereals-BarsMuesli/c/F1720500?currentPage=0&filter=product_category_external_id%3A%27Muesli%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Breakfast Cereals & Bars_DELM_Granola_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Breakfast-Cereals-BarsGranola/c/F1720300?currentPage=0&filter=product_category_external_id%3A%27Granola%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Breakfast Cereals & Bars_DELM_Oats_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Breakfast-Cereals-BarsOats/c/F1720400?currentPage=0&filter=product_category_external_id%3A%27Oats%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chips, Dips & Snacks_DELM_Canister & Puffs_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chips-Dips-SnacksCanister-Puffs/c/F1730100?currentPage=0&filter=product_category_external_id%3A%27Canister%20%7C%20Puffs%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chips, Dips & Snacks_DELM_Pop Corn_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chips-Dips-SnacksPop-Corn/c/F1730400?currentPage=0&filter=product_category_external_id%3A%27Pop%20Corn%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chips, Dips & Snacks_DELM_Chips_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chips-Dips-SnacksChips/c/F1730200?currentPage=0&filter=product_category_external_id%3A%27Chips%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chips, Dips & Snacks_DELM_Tortilla & Nacho_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chips-Dips-SnacksTortilla-Nacho/c/F1730300?currentPage=0&filter=product_category_external_id%3A%27Tortilla%20%7C%20Nacho%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chocolate & Confectionery_DELM_Candy_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chocolate-ConfectioneryCandy/c/F1740100?currentPage=0&filter=product_category_external_id%3A%27Candy%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chocolate & Confectionery_DELM_Chocolates (1)_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chocolate-ConfectioneryChocolates/c/F1740200?currentPage=0&filter=product_category_external_id%3A%27Chocolates%27&maxPrice=12&minPrice=0.5&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chocolate & Confectionery_DELM_Chocolates (2)_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chocolate-ConfectioneryChocolates/c/F1740200?currentPage=0&filter=product_category_external_id%3A%27Chocolates%27&maxPrice=300&minPrice=12.01&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Chocolate & Confectionery_DELM_Gums & Mints_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Chocolate-ConfectioneryGums-Mints/c/F1740300?currentPage=0&filter=product_category_external_id%3A%27Gums%20%7C%20Mints%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Condiments, Dressings & Marinades_DELM_Salad Dressings & Vinaigrettes_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Condiments-Dressings-MarinadesSalad-Dressings-Vinaigrettes/c/F1750200?currentPage=0&filter=product_category_external_id%3A%27Salad%20Dressings%20%7C%20Vinaigrettes%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Condiments, Dressings & Marinades_DELM_Sauces & Condiments_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Condiments-Dressings-MarinadesSauces-Condiments/c/F1750100?currentPage=0&filter=product_category_external_id%3A%27Sauces%20%7C%20Condiments%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Breadcrumbs_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsBreadcrumbs/c/F1760500_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Cooking Sauces & Pastes_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsCooking-Sauces-Pastes/c/F1760100?currentPage=0&filter=product_category_external_id%3A%27Cooking%20Sauces%20%7C%20Pastes%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Gravy & Stock_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsGravy-Stock/c/F1760600?currentPage=0&filter=product_category_external_id%3A%27Gravy%20%7C%20Stock%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Herbs, Spices & Seasoning (1)_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsHerbs-Spices-Seasoning/c/F1760300?currentPage=0&filter=product_category_external_id%3A%27Herbs%3E%20Spices%20%7C%20Seasoning%27&maxPrice=10&minPrice=0.35&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Herbs, Spices & Seasoning (2)_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsHerbs-Spices-Seasoning/c/F1760300?currentPage=0&filter=product_category_external_id%3A%27Herbs%3E%20Spices%20%7C%20Seasoning%27&maxPrice=1000&minPrice=10.01&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Cooking Ingredients_DELM_Oils & Ghee_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Cooking-IngredientsOils-Ghee/c/F1760400?currentPage=0&filter=product_category_external_id%3A%27Oils%20%7C%20Ghee%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Coconut Powder_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCoconut-Powder/c/F1714211?currentPage=0&filter=product_category_external_id%3A%27Coconut%20Powder%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Coconut Cream_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCoconut-Cream/c/F1714212?currentPage=0&filter=product_category_external_id%3A%27Coconut%20Cream%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Canned Meat_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCanned-Meat/c/F1714500?currentPage=0&filter=product_category_external_id%3A%27Canned%20Meat%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Canned Fruits_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCanned-Fruits/c/F1714300?currentPage=0&filter=product_category_external_id%3A%27Canned%20Fruits%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Canned Vegetables_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCanned-Vegetables-/c/F1714100?currentPage=0&filter=product_category_external_id%3A%27Canned%20Vegetables%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Coconut Milk_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsCoconut-Milk/c/F1714200?currentPage=0&filter=product_category_external_id%3A%27Coconut%20Milk%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Powdered Milk_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsPowdered-Milk/c/F1714600?currentPage=0&filter=product_category_external_id%3A%27Powdered%20Milk%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Pickles & Olives_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsPickles-Olives/c/F1714400?currentPage=0&filter=product_category_external_id%3A%27Pickles%20%7C%20Olives%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Tuna & Seafood_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsTuna-Seafood/c/F1714900?currentPage=0&filter=product_category_external_id%3A%27Tuna%20%7C%20Seafood%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Tins, Jars & Packets_DELM_Soup & Instant Noodles_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Tins-Jars-PacketsSoup-Instant-Noodles/c/F1714800?currentPage=0&filter=product_category_external_id%3A%27Soup%20%7C%20Instant%20Noodles%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Jams, Honey & Spreads_DELM_Honey_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Jams-Honey-SpreadsHoney/c/F1700200?currentPage=0&filter=product_category_external_id%3A%27Honey%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Jams, Honey & Spreads_DELM_Jams_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Jams-Honey-SpreadsJams/c/F1700300?currentPage=0&filter=product_category_external_id%3A%27Jams%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Jams, Honey & Spreads_DELM_Spreadables_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Jams-Honey-SpreadsSpreadables/c/F1700100?currentPage=0&filter=product_category_external_id%3A%27Spreadables%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Nuts, Dates & Dried Fruits_DELM_Dates_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Nuts-Dates-Dried-FruitsDates/c/F1780100?currentPage=0&filter=product_category_external_id%3A%27Dates%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Nuts, Dates & Dried Fruits_DELM_Dried Fruits_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Nuts-Dates-Dried-FruitsDried-Fruits/c/F1780300?currentPage=0&filter=product_category_external_id%3A%27Dried%20Fruits%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Nuts, Dates & Dried Fruits_DELM_Nuts & Seeds_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Nuts-Dates-Dried-FruitsNuts-Seeds/c/F1780200?currentPage=0&filter=product_category_external_id%3A%27Nuts%20%7C%20Seeds%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Rice, Pasta & Pulses_DELM_Pasta_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Rice-Pasta-PulsesPasta/c/F1701220?currentPage=0&filter=product_category_external_id%3A%27Pasta%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Rice, Pasta & Pulses_DELM_Pulses, Grains & Couscous_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Rice-Pasta-PulsesPulses-Grains-Couscous/c/F1701230?currentPage=0&filter=product_category_external_id%3A%27Pulses%3E%20Grains%20%7C%20Couscous%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Rice, Pasta & Pulses_DELM_Rice_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Rice-Pasta-PulsesRice/c/F1701240?currentPage=0&filter=product_category_external_id%3A%27Rice%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Sugar & Home Baking_DELM_Baking Ingredients_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Sugar-Home-BakingBaking-Ingredients/c/F1701320?currentPage=0&filter=product_category_external_id%3A%27Baking%20Ingredients%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Sugar & Home Baking_DELM_Condensed Milk_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Sugar-Home-BakingCondensed-Milk/c/F1701340?currentPage=0&filter=product_category_external_id%3A%27Condensed%20Milk%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Sugar & Home Baking_DELM_Flour & Bread Mixes_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Sugar-Home-BakingFlour-Bread-Mixes/c/F1701360?currentPage=0&filter=product_category_external_id%3A%27Flour%20%7C%20Bread%20Mixes%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_Sugar & Home Baking_DELM_Sugar & Sweeteners_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Sugar-Home-BakingSugar-Sweeteners/c/F1701350?currentPage=0&filter=product_category_external_id%3A%27Sugar%20%7C%20Sweeteners%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Chinese Food_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesChinese/c/F1790700?currentPage=0&filter=&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Bangladesh_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesBangladesh/c/F1790020?currentPage=0&filter=product_category_external_id%3A%27Bangladesh%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_French_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesFrench/c/F1790170?currentPage=0&filter=product_category_external_id%3A%27French%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Eastern Europe_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesEastern-Europe/c/F1790160?currentPage=0&filter=product_category_external_id%3A%27Eastern%20Europe%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Indian_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesIndian/c/F1790200?currentPage=0&filter=product_category_external_id%3A%27Indian%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Japanese_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesJapanese/c/F1790025?currentPage=0&filter=product_category_external_id%3A%27Japanese%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Italy_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesItaly/c/F1790180?currentPage=0&filter=product_category_external_id%3A%27Italy%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Korean_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesKorean/c/F1790024?currentPage=0&filter=product_category_external_id%3A%27Korean%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Mexican_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesMexican/c/F1790400?currentPage=0&filter=product_category_external_id%3A%27Mexican%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Philippines_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesPhilippines/c/F1790600?currentPage=0&filter=product_category_external_id%3A%27Philippines%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Pakistan_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesPakistan/c/F1790300?currentPage=0&filter=product_category_external_id%3A%27Pakistan%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Sri-Lanka_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesSri-Lanka/c/F1790800?currentPage=0&filter=product_category_external_id%3A%27Sri-Lanka%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_Thai_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesThai/c/F1790900?currentPage=0&filter=product_category_external_id%3A%27Thai%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_UK_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesUK/c/F1790140?currentPage=0&filter=product_category_external_id%3A%27UK%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Food Cupboard_DELM_World Specialities_DELM_USA_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/World-SpecialitiesUSA/c/F1790021?currentPage=0&filter=product_category_external_id%3A%27USA%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Juices_DELM_Chilled & Fresh Juices_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/JuicesFreshly-Squeezed-Juices/c/F1520100?currentPage=0&filter=product_category_external_id%3A%27Chilled%20%7C%20Fresh%20Juices%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Juices_DELM_Coconut Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/JuicesCoconut-Flavored-Water/c/F1520400?currentPage=0&filter=product_category_external_id%3A%27Coconut%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Juices_DELM_Long Life Juices & Smoothies_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/JuicesLong-Life-Juices-Smoothies/c/F1520200?currentPage=0&filter=product_category_external_id%3A%27Long%20Life%20Juices%20%7C%20Smoothies%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Juices_DELM_Syrups & Concentrate_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/JuicesSyrups-Concentrate/c/F1520300?currentPage=0&filter=product_category_external_id%3A%27Syrups%20%7C%20Concentrate%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Coffee_DELM_Ground Coffee & Beans_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/CoffeeGround-Coffee-Beans/c/F1510300?currentPage=0&filter=product_category_external_id%3A%27Ground%20Coffee%20%7C%20Beans%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Coffee_DELM_Capsules_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/CoffeeCapsules/c/F1510600?currentPage=0&filter=product_category_external_id%3A%27Capsules%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Coffee_DELM_Decaffeinated Coffee_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/CoffeeDecaffeinated-Coffee/c/F1510200?currentPage=0&filter=product_category_external_id%3A%27Decaffeinated%20Coffee%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Coffee_DELM_Pods_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/CoffeePods/c/F1510900?currentPage=0&filter=product_category_external_id%3A%27Pods%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Coffee_DELM_Instant Coffee & Sachets_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/CoffeeInstant-Coffee-Sachets/c/F1510500?currentPage=0&filter=product_category_external_id%3A%27Instant%20Coffee%20%7C%20Sachets%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Kids Drinks_DELM_Kids Juices_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Kids-DrinksKids-Juices/c/F1530100?currentPage=0&filter=product_category_external_id%3A%27Kids%20Juices%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Powdered Drinks_DELM_Hot Chocolate & Melts_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Powdered-DrinksHot-Chocolate-Melts/c/F1540200?currentPage=0&filter=product_category_external_id%3A%27Hot%20Chocolate%20%7C%20Melts%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Powdered Drinks_DELM_Powdered Juices_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Powdered-DrinksPowdered-Juices/c/F1540100?currentPage=0&filter=product_category_external_id%3A%27Powdered%20Juices%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Powdered Drinks_DELM_Nourishing & Healthy Instant_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Powdered-DrinksNourishing-Healthy-Instant/c/F1540300?currentPage=0&filter=product_category_external_id%3A%27Nourishing%20%7C%20Healthy%20Instant%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Soft Drinks_DELM_Carbonated Drinks_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Soft-DrinksCarbonated-Drinks/c/F1550100?currentPage=0&filter=product_category_external_id%3A%27Carbonated%20Drinks%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Soft Drinks_DELM_Vitamins, Sports & Energy Drinks_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/Soft-DrinksVitamins-Sports-Energy-Drinks/c/F1550200?currentPage=0&filter=product_category_external_id%3A%27Vitamins%3E%20Sports%20%7C%20Energy%20Drinks%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Tea_DELM_Iced Tea_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/TeaIced-Tea/c/F1560100?currentPage=0&filter=product_category_external_id%3A%27Iced%20Tea%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Tea_DELM_Loose Leaf & Tea Bags_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/TeaLoose-Leaf-Tea-Bags/c/F1560200?currentPage=0&filter=product_category_external_id%3A%27Loose%20Leaf%20%7C%20Tea%20Bags%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Tea_DELM_Tea Sachets_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/TeaTea-Sachets/c/F1560300?currentPage=0&filter=product_category_external_id%3A%27Tea%20Sachets%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Water_DELM_Alkaline Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/WaterAlkaline-Water/c/F1570600?currentPage=0&filter=product_category_external_id%3A%27Alkaline%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Water_DELM_Flavoured Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/WaterFlavoured-Water/c/F1570100?currentPage=0&filter=product_category_external_id%3A%27Flavoured%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Water_DELM_Mineral Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/WaterMineral-Water/c/F1570300?currentPage=0&filter=product_category_external_id%3A%27Mineral%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Water_DELM_Still Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/WaterStill-Water/c/F1570400?currentPage=0&filter=product_category_external_id%3A%27Still%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance_DELMX_Beverages_DELM_Water_DELM_Sparkling Water_DELM_https://www.carrefouruae.com/mafuae/en/Beverages/WaterSparkling-Water/c/F1570200?currentPage=0&filter=product_category_external_id%3A%27Sparkling%20Water%27&nextPageOffset=0&pageSize=600&sortBy=relevance"
giant = "Food Cupboard_DELM_Rice, Pasta & Pulses_DELM_Pasta_DELM_https://www.carrefouruae.com/mafuae/en/Food-Cupboard/Rice-Pasta-PulsesPasta/c/F1701220?currentPage=0&filter=product_category_external_id%3A%27Pasta%27&nextPageOffset=0&pageSize=600&sortBy=relevance"
links = []

for big in giant.split("_DELMX_"):
    t = big.split("_DELM_")
    links.append([f"{t[0::2]}", t[3]])

browser = webdriver.Chrome(executable_path="chromedriver.exe")
target = {}
done_targets = []
redo_targets = []
options: list = [0, 1, 2, 3]
x = {}
for link in links:
    browser.get(link[1])
    isDone = input("enter any key") or ""
    soup = BeautifulSoup(browser.page_source, "lxml")
    desc = {'label': link[0] + " desc", 'type': 'selector', 'name': '.css-12fzzt2', 'exists': True, 'isRange': 1,
            'start': 0,
            'end': 0, 'get_what': 'text'}
    desc['end'] = len(soup.select(desc['name'])) + 1
    img = {'label': link[0] + " img", 'type': 'selector', 'name': '.css-1bu2zfe', 'exists': True, 'isRange': 1,
           'start': 0,
           'end': 0, 'get_what': 'attr', 'attr': 'src'}
    img['end'] = len(soup.select(img['name'])) + 1
    size = {'label': link[0] + " size", 'type': 'selector', 'name': '.css-4yob99', 'exists': True, 'isRange': 1,
            'start': 0,
            'end': 0, 'get_what': 'text'}
    size['end'] = len(soup.select(size['name'])) + 1
    price = {'label': link[0] + " price", 'type': 'selector', 'name': '.css-1m492cm', 'exists': True, 'isRange': 1,
             'start': 0,
             'end': 0, 'get_what': 'text'}
    price['end'] = len(soup.select(price['name'])) + 1
    options[0] = desc
    options[1] = size
    options[2] = price
    options[3] = img
    target = scraper(soup, options, target)
    ds = len(soup.select(desc['name']))
    ss = len(soup.select(size['name']))
    ps = len(soup.select(price['name']))
    isize = len(soup.select(img['name']))
    print(f"desc: {ds }")
    print(f"size: { ss}")
    print(f"price: {ps}")
    print(f"img: {isize}")
    target[link[0] + " price"] = str(target[link[0] + " price"])
    p = ""
    for z in str(target[link[0] + " price"]).split(','):
        if len(z.split('AED')) > 2:
            z = z.split('AED')[1] + " AED"
            z = f"'{z}'"
        if p == "":
            p += z
        else:
            p += ", " + z
    target[link[0] + " price"] = p
    convert_dict_to_json(target, name=f"{link[0]}")
    if not (ds == ss == ps == isize):
        redo_targets.append(link)
print(target)
for i in redo_targets:
    print(i)