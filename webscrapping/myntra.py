from playwright.sync_api import sync_playwright

url = "https://www.myntra.com/men-tshirts"
product ={}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    
    products = page.locator(".product-base")
    
    for i in range(products.count()):
        prod = products.nth(i)
        brand = prod.locator(".product-productMetaInfo .product-brand").inner_text()
        print(brand)
        price_locator = prod.locator(".product-productMetaInfo .product-price")
        price = price_locator.inner_text()
        #price = prod.locator(".product-productMetaInfo .product-price").inner_text()
        #discounted_price =price_locator.locator(".product-discountedPrice")
        discounted_price =price_locator.locator(".product-discountedPrice")
        dp = discounted_price.inner_text() if discounted_price.count()>0 else "N/A"
        print(price," - ",dp)
        # if discounted_price.count()>0:
        #     print(price," -",discounted_price.inner_text())
        # else:
        #     print("N/A")            
            
        
        
        
        
    
    
    browser.close()