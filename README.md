# RestCRUD


## RESTful service with SQLlite DB
 - use flask api
 - use sqlite
 
## HTTP End point 

		GET  
		/market/search/<marketname>

		DELETE
		/market/delete/

		POST
		/market/create/

		PUT
		/market/update/

## HTTP request payload sample

```json
	[
		 {
		   "FMID": 1018261,
		   "MarketName": " Caledonia Farmers Market Association - Danville",
		   "Website": "https://sites.google.com/site/caledoniafarmersmarket/",
		   "Facebook": "https://www.facebook.com/Danville.VT.Farmers.Market/",
		   "Twitter": "",
		   "Youtube": "",
		   "OtherMedia": "",
		   "street": "",
		   "city": "Danville",
		   "County": "Caledonia",
		   "State": "Vermont",
		   "zip": "05828",
		   "Season1Date": "06/14/2017 to 08/30/2017",
		   "Season1Time": "Wed: 9:00 AM-1:00 PM;",
		   "Season2Date": "09/06/2017 to 10/18/2017",
		   "Season2Time": "Wed: 2:00 PM-6:00 PM;",
		   "Season3Date": "",
		   "Season3Time": "",
		   "Season4Date": "",
		   "Season4Time": "",
		   "x": -72.140337,
		   "y": 44.411036,
		   "Location": "",
		   "Credit": "Y",
		   "WIC": "Y",
		   "WICcash": "N",
		   "SFMNP": "Y",
		   "SNAP": "N",
		   "Organic": "Y",
		   "Bakedgoods": "Y",
		   "Cheese": "Y",
		   "Crafts": "Y",
		   "Flowers": "Y",
		   "Eggs": "Y",
		   "Seafood": "N",
		   "Herbs": "Y",
		   "Vegetables": "Y",
		   "Honey": "Y",
		   "Jams": "Y",
		   "Maple": "Y",
		   "Meat": "Y",
		   "Nursery": "N",
		   "Nuts": "N",
		   "Plants": "N",
		   "Poultry": "Y",
		   "Prepared": "Y",
		   "Soap": "Y",
		   "Trees": "Y",
		   "Wine": "N",
		   "Coffee": "Y",
		   "Beans": "Y",
		   "Fruits": "Y",
		   "Grains": "N",
		   "Juices": "N",
		   "Mushrooms": "Y",
		   "PetFood": "Y",
		   "Tofu": "N",
		   "WildHarvested": "N",
		   "updateTime": "6/20/2017 10:43:57 PM"
		 }
	]
```

## HTTP response code
	200
	201
	400
	404
